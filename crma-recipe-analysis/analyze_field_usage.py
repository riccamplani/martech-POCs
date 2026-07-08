import json
import re
import os
import copy
from collections import defaultdict
from datetime import datetime, timezone
from html import unescape

DATA_DIR = "data"
OUTPUT_DIR = "output"

TARGET_OBJECTS = {
    "Account", "Account_Structure__c", "Account_Summary__c",
    "Subscription", "Subscription_Item", "Agreement__c", "Agreement_Item__c",
    "Account_Location__c", "BSS_Event__c", "Contact",
    "Shortcut_to_Product_Offer_ID__c", "Payment_Status__c", "User",
    "Terminated_Subscription__c", "Suspect__c", "External_User__c",
}


def get_load_fields(node):
    fields = node.get("parameters", {}).get("fields", [])
    result = []
    for f in fields:
        if isinstance(f, dict):
            result.append(f.get("name", f.get("fieldName", "")))
        elif isinstance(f, str):
            result.append(f)
    return result


def extract_sql_field_refs(expr):
    expr = unescape(expr)
    expr = re.sub(r"'[^']*'", "", expr)
    expr = re.sub(r"\b\d+\.?\d*\b", "", expr)
    tokens = re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\b", expr)
    sql_keywords = {
        "case", "when", "then", "else", "end", "and", "or", "not", "in",
        "is", "null", "true", "false", "like", "between", "as", "cast",
        "select", "from", "where", "group", "by", "order", "asc", "desc",
        "contains", "array_contains", "array_join", "concat", "coalesce",
        "if", "ifnull", "isnull", "length", "len", "trim", "ltrim", "rtrim",
        "upper", "lower", "substring", "substr", "replace", "left", "right",
        "to_date", "to_timestamp", "date_diff", "date_add", "date_sub",
        "datediff", "dateadd", "year", "month", "day", "hour", "minute",
        "now", "current_date", "current_timestamp", "today",
        "sum", "count", "avg", "min", "max", "abs", "round", "floor", "ceil",
        "row_number", "rank", "dense_rank", "over", "partition", "rows",
        "unbounded", "preceding", "following", "current", "row",
        "int", "integer", "float", "double", "decimal", "number", "text",
        "string", "varchar", "boolean", "date", "datetime", "timestamp",
        "yes", "no",
        "to_number", "to_text", "to_char", "instr", "regexp", "regexp_extract",
        "split", "array_length", "array_sort", "first", "last",
        "lag", "lead", "nth_value", "ntile",
    }
    return [t for t in tokens if t.lower() not in sql_keywords]


def extract_fields_from_node(node):
    action = node.get("action", "")
    params = node.get("parameters", {})
    referenced = set()
    created = set()

    if action == "filter":
        for expr in params.get("filterExpressions", []):
            field = expr.get("field", "")
            if field:
                referenced.add(field)

    elif action in ("formula", "computeRelative"):
        for f in params.get("fields", []):
            new_name = f.get("name", "")
            if new_name:
                created.add(new_name)
            expr = f.get("formulaExpression", "")
            if expr:
                referenced.update(extract_sql_field_refs(expr))
        for ob in params.get("orderBy", []):
            fn = ob.get("fieldName", "")
            if fn:
                referenced.add(fn)
        for pb in params.get("partitionBy", []):
            if pb:
                referenced.add(pb)

    elif action == "join":
        for k in params.get("leftKeys", []):
            referenced.add(k)
        for k in params.get("rightKeys", []):
            referenced.add(k)
        schema = node.get("schema", {})
        for f in schema.get("slice", {}).get("fields", []):
            referenced.add(f)
        for f in schema.get("fields", []):
            if isinstance(f, dict):
                referenced.add(f.get("name", ""))
            else:
                referenced.add(f)

    elif action == "aggregate":
        for g in params.get("groupings", []):
            referenced.add(g)
        for agg in params.get("aggregations", []):
            src = agg.get("source", "")
            if src:
                referenced.add(src)
            new_name = agg.get("name", "")
            if new_name:
                created.add(new_name)

    elif action == "extractGrains":
        for ge in params.get("grainExtractions", []):
            fn = ge.get("fieldName", "")
            if fn:
                referenced.add(fn)

    elif action == "schema":
        slice_info = params.get("slice", {})
        mode = slice_info.get("mode", "")
        # Only SELECT mode fields are actively used; DROP mode fields are being discarded
        if mode == "SELECT":
            for f in slice_info.get("fields", []):
                referenced.add(f)
        for f in params.get("fields", []):
            if isinstance(f, dict):
                name = f.get("name", "")
                new_name = f.get("newProperties", {}).get("name", "")
                if name:
                    referenced.add(name)
                if new_name:
                    created.add(new_name)

    elif action == "appendV2":
        for fm in params.get("fieldMappings", []):
            top = fm.get("top", "")
            bottom = fm.get("bottom", "")
            if top:
                referenced.add(top)
            if bottom:
                referenced.add(bottom)

    elif action == "typeCast":
        for f in params.get("fields", []):
            name = f.get("name", "")
            if name:
                referenced.add(name)
            new_name = f.get("newProperties", {}).get("name", "")
            if new_name:
                created.add(new_name)

    elif action == "save":
        for f in params.get("fields", []):
            if isinstance(f, dict):
                referenced.add(f.get("name", ""))
            else:
                referenced.add(f)

    return referenced, created


def build_dag(nodes):
    forward = defaultdict(list)
    for name, node in nodes.items():
        for src in node.get("sources", []):
            forward[src].append(name)
    return forward


def trace_used_fields(load_name, load_fields, nodes, forward):
    load_field_set = set(load_fields)
    used_fields = set()
    visited = set()
    queue = [load_name]

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        node = nodes.get(current, {})
        if current != load_name:
            referenced, _ = extract_fields_from_node(node)
            for f in referenced:
                if f in load_field_set:
                    used_fields.add(f)
                elif "." in f:
                    base = f.rsplit(".", 1)[-1]
                    if base in load_field_set:
                        used_fields.add(base)

        for downstream in forward.get(current, []):
            queue.append(downstream)

    return used_fields


def find_field_usage_locations(load_name, load_fields, nodes, forward):
    load_field_set = set(load_fields)
    field_usage = defaultdict(list)
    visited = set()
    queue = [load_name]

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        node = nodes.get(current, {})
        action = node.get("action", "")
        if current != load_name:
            referenced, _ = extract_fields_from_node(node)
            for f in referenced:
                if f in load_field_set:
                    field_usage[f].append((current, action))
                elif "." in f:
                    base = f.rsplit(".", 1)[-1]
                    if base in load_field_set:
                        field_usage[base].append((current, action))

        for downstream in forward.get(current, []):
            queue.append(downstream)

    return field_usage


def get_nodes(data):
    """Extract nodes dict from either raw recipe or API export format."""
    if "recipeDefinition" in data:
        return data["recipeDefinition"]["nodes"]
    return data["nodes"]


def build_cleaned(data, results, forward):
    """Build cleaned recipe with only used fields in load nodes.
    A field is only removed if unused across ALL load nodes for the same
    object in this recipe (CRMA validates fields at the object level).
    Also cleans up downstream DROP schemas to stay consistent."""
    cleaned = copy.deepcopy(data)
    nodes = get_nodes(cleaned)

    # Build per-object union of used fields across all load nodes
    obj_used_fields = defaultdict(set)
    for load_name, result in results.items():
        obj_used_fields[result["sourceObject"]] |= set(result["usedFields"])

    for load_name, result in results.items():
        orig_fields = nodes[load_name]["parameters"]["fields"]
        keep_set = obj_used_fields[result["sourceObject"]]
        removed = set(result["unusedFields"]) - keep_set

        nodes[load_name]["parameters"]["fields"] = [
            f for f in orig_fields
            if (f if isinstance(f, str) else f.get("name", f.get("fieldName", ""))) in keep_set
        ]

        # Clean up downstream DROP schemas: remove references to fields
        # that no longer exist in the data flow
        if not removed:
            continue
        visited = set()
        queue = [load_name]
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            node = nodes.get(current, {})
            if current != load_name and node.get("action") == "schema":
                slice_info = node.get("parameters", {}).get("slice", {})
                if slice_info.get("mode") == "DROP":
                    orig_drop = slice_info.get("fields", [])
                    slice_info["fields"] = [
                        f for f in orig_drop
                        if (f.rsplit(".", 1)[-1] if "." in f else f) not in removed
                    ]
            for downstream in forward.get(current, []):
                queue.append(downstream)

    if "recipeDefinition" in cleaned:
        return cleaned["recipeDefinition"]
    return cleaned


def analyze_recipe(input_path):
    """Analyze a single recipe and return (results, data, nodes) or None if not a valid recipe."""
    with open(input_path) as f:
        data = json.load(f)

    try:
        nodes = get_nodes(data)
    except (KeyError, TypeError):
        return None

    if not isinstance(nodes, dict):
        return None

    forward = build_dag(nodes)

    load_info = {}
    for name, node in nodes.items():
        if node.get("action") == "load":
            dataset = node.get("parameters", {}).get("dataset", {})
            source_obj = dataset.get("sourceObjectName", dataset.get("label", "unknown"))
            if source_obj not in TARGET_OBJECTS:
                continue
            load_info[name] = {
                "sourceObject": source_obj,
                "connection": dataset.get("connectionName", ""),
                "type": dataset.get("type", ""),
                "fields": get_load_fields(node),
            }

    results = {}
    for load_name, info in load_info.items():
        fields = info["fields"]
        used_fields = trace_used_fields(load_name, fields, nodes, forward)
        field_usage = find_field_usage_locations(load_name, fields, nodes, forward)
        results[load_name] = {
            "sourceObject": info["sourceObject"],
            "connection": info["connection"],
            "type": info["type"],
            "totalFields": len(fields),
            "usedFields": sorted(used_fields),
            "unusedFields": sorted(set(fields) - used_fields),
            "fieldUsage": {f: locs for f, locs in field_usage.items()},
        }

    return results, data, nodes, forward


def generate_report(recipe_name, nodes, results):
    """Generate markdown report for a single recipe."""
    lines = []
    lines.append(f"# {recipe_name} — Field Usage Report")
    lines.append("")
    lines.append(f"**Recipe:** {recipe_name}")
    lines.append(f"**Total nodes:** {len(nodes)}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |")
    lines.append("|-----------|--------------|------|-------------|------|--------|-----------|")

    total_before = 0
    total_after = 0
    for load_name in sorted(results, key=lambda x: results[x]["sourceObject"]):
        r = results[load_name]
        total = r["totalFields"]
        used = len(r["usedFields"])
        unused = len(r["unusedFields"])
        pct = f"{(unused / total * 100):.0f}%" if total > 0 else "0%"
        total_before += total
        total_after += used
        lines.append(f"| {load_name} | {r['sourceObject']} | {r['type']} | {total} | {used} | {unused} | {pct} |")

    if total_before > 0:
        lines.append(f"| **TOTAL** | | | **{total_before}** | **{total_after}** | **{total_before - total_after}** | **{((total_before - total_after) / total_before * 100):.0f}%** |")
    lines.append("")

    lines.append("## Detail per Source Object")
    lines.append("")
    for load_name in sorted(results, key=lambda x: results[x]["sourceObject"]):
        r = results[load_name]
        lines.append(f"### {r['sourceObject']} (`{load_name}`)")
        lines.append("")
        lines.append(f"- **Connection:** {r['connection'] or 'analyticsDataset (in-org)'}")
        lines.append(f"- **Fields loaded:** {r['totalFields']}")
        lines.append(f"- **Fields used:** {len(r['usedFields'])}")
        lines.append(f"- **Fields unused:** {len(r['unusedFields'])}")
        lines.append("")

        if r["usedFields"]:
            lines.append("#### Fields to KEEP")
            lines.append("")
            lines.append("| Field | Used In |")
            lines.append("|-------|---------|")
            for f in r["usedFields"]:
                locs = r["fieldUsage"].get(f, [])
                loc_str = ", ".join([f"{n} ({a})" for n, a in locs[:5]])
                if len(locs) > 5:
                    loc_str += f" +{len(locs) - 5} more"
                lines.append(f"| `{f}` | {loc_str} |")
            lines.append("")

        if r["unusedFields"]:
            lines.append("#### Fields to ELIMINATE")
            lines.append("")
            for f in r["unusedFields"]:
                lines.append(f"- `{f}`")
            lines.append("")

    return "\n".join(lines), total_before, total_after


def main():
    json_dir = os.path.join(OUTPUT_DIR, "json")
    reports_dir = os.path.join(OUTPUT_DIR, "reports")
    # Clean old output files to avoid stale results
    for d in (json_dir, reports_dir):
        if os.path.exists(d):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

    recipe_files = sorted([
        f for f in os.listdir(DATA_DIR)
        if f.endswith(".json") and not f.startswith(".")
    ])

    print(f"Found {len(recipe_files)} JSON files in {DATA_DIR}/\n")

    grand_total_before = 0
    grand_total_after = 0
    processed = 0
    skipped = 0
    dashboard_recipes = []

    for filename in recipe_files:
        input_path = os.path.join(DATA_DIR, filename)
        result = analyze_recipe(input_path)

        if result is None:
            print(f"SKIP: {filename} (not a valid JSON recipe)")
            skipped += 1
            continue

        results, data, nodes, forward = result
        recipe_name = os.path.splitext(filename)[0]

        # Generate cleaned recipe (always — even if no target objects, for HTML decode)
        cleaned = build_cleaned(data, results, forward)
        output_recipe_path = os.path.join(json_dir, f"clean_{filename}")
        with open(output_recipe_path, "w") as f:
            json.dump(cleaned, f, indent=2, ensure_ascii=False)

        if not results:
            dashboard_recipes.append({
                "name": recipe_name,
                "filename": filename,
                "totalNodes": len(nodes),
                "totalFields": 0,
                "usedFields": 0,
                "unusedFields": 0,
                "loadNodes": [],
                "noTargetObjects": True,
            })
            print(f"OK: {filename} — no target SF objects, cleaned (HTML decode only)")
            processed += 1
            continue

        # Generate report
        safe_name = re.sub(r"[^\w\-]", "_", recipe_name)
        output_report_path = os.path.join(reports_dir, f"{safe_name}_field_usage_report.md")
        report_text, total_before, total_after = generate_report(recipe_name, nodes, results)
        with open(output_report_path, "w") as f:
            f.write(report_text)

        # Collect dashboard data — use per-object conservative logic
        # (matches what build_cleaned actually removes)
        obj_used_union = defaultdict(set)
        for r in results.values():
            obj_used_union[r["sourceObject"]] |= set(r["usedFields"])

        load_nodes_data = []
        dash_total = 0
        dash_used = 0
        for load_name in sorted(results, key=lambda x: results[x]["sourceObject"]):
            r = results[load_name]
            keep = obj_used_union[r["sourceObject"]]
            all_fields = set(r["usedFields"]) | set(r["unusedFields"])
            effective_unused = sorted(all_fields - keep)
            effective_used = sorted(all_fields & keep)
            dash_total += len(all_fields)
            dash_used += len(effective_used)
            load_nodes_data.append({
                "nodeName": load_name,
                "sourceObject": r["sourceObject"],
                "connection": r["connection"],
                "type": r["type"],
                "totalFields": len(all_fields),
                "usedFields": effective_used,
                "unusedFields": effective_unused,
                "fieldUsage": {f: locs for f, locs in r["fieldUsage"].items()},
            })
        dashboard_recipes.append({
            "name": recipe_name,
            "filename": filename,
            "totalNodes": len(nodes),
            "totalFields": dash_total,
            "usedFields": dash_used,
            "unusedFields": dash_total - dash_used,
            "loadNodes": load_nodes_data,
        })

        grand_total_before += total_before
        grand_total_after += total_after
        removed = total_before - total_after
        pct = f"{(removed / total_before * 100):.0f}%" if total_before > 0 else "0%"
        print(f"OK: {filename} — {total_after}/{total_before} fields used, {removed} removed ({pct})")
        processed += 1

    # Write dashboard data
    dashboard_data = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "recipes": dashboard_recipes,
    }
    dashboard_path = os.path.join(json_dir, "dashboard_data.json")
    with open(dashboard_path, "w") as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)

    print(f"\n=== COMPLETE ===")
    print(f"Processed: {processed} recipes")
    print(f"Skipped: {skipped} files")
    if grand_total_before > 0:
        grand_removed = grand_total_before - grand_total_after
        print(f"Total fields: {grand_total_after}/{grand_total_before} used, {grand_removed} removed ({(grand_removed / grand_total_before * 100):.0f}%)")

    print(f"\nOutputs in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
