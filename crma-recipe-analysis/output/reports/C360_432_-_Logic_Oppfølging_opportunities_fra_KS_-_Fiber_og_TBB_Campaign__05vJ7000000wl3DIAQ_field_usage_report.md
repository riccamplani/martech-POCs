# C360_432_-_Logic_Oppfølging_opportunities_fra_KS_-_Fiber_og_TBB_Campaign__05vJ7000000wl3DIAQ — Field Usage Report

**Recipe:** C360_432_-_Logic_Oppfølging_opportunities_fra_KS_-_Fiber_og_TBB_Campaign__05vJ7000000wl3DIAQ
**Total nodes:** 55

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET1 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| **TOTAL** | | | **7** | **7** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DPSS_Segment__c` | FILTER0 (filter) |
| `Has_Subscriptions_Actual__c` | DROP_FIELDS0 (schema), FORMULA43 (formula), FORMULA43_copy0 (formula), APPEND0 (appendV2) |
| `Id` | JOIN0 (join), DROP_FIELDS0 (schema), JOIN6 (join), JOIN1 (join), JOIN2 (join) +5 more |
| `IsDeleted` | FILTER1 (filter) |
| `KurtID__c` | DROP_FIELDS0 (schema), APPEND0 (appendV2), FORMULA20_copy0_copy0 (formula), FORMULA23_copy0_copy0 (formula) |
| `Name` | APPEND0 (appendV2), FORMULA26_copy0_copy0 (formula) |
| `StatusKURT__c` | FILTER1 (filter) |
