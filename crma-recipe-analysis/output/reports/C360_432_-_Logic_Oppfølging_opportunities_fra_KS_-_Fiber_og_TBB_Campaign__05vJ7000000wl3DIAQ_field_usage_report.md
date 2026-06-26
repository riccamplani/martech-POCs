# C360_432_-_Logic_Oppfølging_opportunities_fra_KS_-_Fiber_og_TBB_Campaign__05vJ7000000wl3DIAQ — Field Usage Report

**Recipe:** C360_432_-_Logic_Oppfølging_opportunities_fra_KS_-_Fiber_og_TBB_Campaign__05vJ7000000wl3DIAQ
**Total nodes:** 55

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET1 | Account | connectedDataset | 7 | 6 | 1 | 14% |
| **TOTAL** | | | **7** | **6** | **1** | **14%** |

## Detail per Source Object

### Account (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 6
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Has_Subscriptions_Actual__c` | FORMULA43 (formula), FORMULA43_copy0 (formula) |
| `Id` | JOIN0 (join), FORMULA21_copy0_copy0 (formula), FORMULA22_copy0_copy0 (formula) |
| `IsDeleted` | FILTER1 (filter) |
| `KurtID__c` | FORMULA20_copy0_copy0 (formula), FORMULA23_copy0_copy0 (formula) |
| `Name` | FORMULA26_copy0_copy0 (formula) |
| `StatusKURT__c` | FILTER1 (filter) |

#### Fields to ELIMINATE

- `DPSS_Segment__c`
