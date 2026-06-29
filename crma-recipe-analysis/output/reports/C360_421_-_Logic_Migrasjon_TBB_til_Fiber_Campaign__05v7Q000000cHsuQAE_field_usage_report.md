# C360_421_-_Logic_Migrasjon_TBB_til_Fiber_Campaign__05v7Q000000cHsuQAE — Field Usage Report

**Recipe:** C360_421_-_Logic_Migrasjon_TBB_til_Fiber_Campaign__05v7Q000000cHsuQAE
**Total nodes:** 88

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET3 | Account_Location__c | connectedDataset | 7 | 7 | 0 | 0% |
| **TOTAL** | | | **11** | **11** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DPSS_Segment__c` | FILTER36 (filter), FILTER36_copy0 (filter), FILTER36_copy1 (filter), APPEND2 (appendV2), APPEND2 (appendV2) +6 more |
| `Id` | JOIN5 (join), JOIN6 (join), JOIN2 (join), FILTER40 (filter), FILTER41 (filter) +21 more |
| `KurtID__c` | APPEND2 (appendV2), APPEND2 (appendV2), DROP_FIELDS2 (schema), DROP_FIELDS2_copy0 (schema), DROP_FIELDS18 (schema) +7 more |
| `NBR_TBB_MOBIL__c` | FILTER39 (filter), APPEND2 (appendV2), APPEND2 (appendV2), DROP_FIELDS18 (schema) |

### Account_Location__c (`LOAD_DATASET3`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Active_subs__c` | FILTER38 (filter), DROP_FIELDS18 (schema) |
| `Building_type__c` | DROP_FIELDS18 (schema) |
| `FAR_ID__c` | JOIN3 (join), DROP_FIELDS18 (schema) |
| `Fiber_cost__c` | FILTER38 (filter), FORMULA1 (formula), DROP_FIELDS18 (schema), DROP_FIELDS1_copy0 (schema), APPEND0 (appendV2) +3 more |
| `Location_Owner__c` | JOIN3 (join), JOIN4 (join), DROP_FIELDS1_copy0 (schema), DROP_FIELDS1_copy0 (schema), FORMULA43 (formula) +6 more |
| `Postal_address__c` | DROP_FIELDS18 (schema) |
| `Street_address__c` | DROP_FIELDS18 (schema) |
