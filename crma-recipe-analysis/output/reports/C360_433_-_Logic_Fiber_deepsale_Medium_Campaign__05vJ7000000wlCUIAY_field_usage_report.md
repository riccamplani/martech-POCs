# C360_433_-_Logic_Fiber_deepsale_Medium_Campaign__05vJ7000000wlCUIAY — Field Usage Report

**Recipe:** C360_433_-_Logic_Fiber_deepsale_Medium_Campaign__05vJ7000000wlCUIAY
**Total nodes:** 48

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 13 | 7 | 6 | 46% |
| **TOTAL** | | | **13** | **7** | **6** | **46%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 13
- **Fields used:** 7
- **Fields unused:** 6

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DPSS_Segment__c` | FILTER0 (filter) |
| `Id` | JOIN0 (join), JOIN1 (join), JOIN2 (join), JOIN3 (join), DROP_FIELDS29_copy0 (schema) +2 more |
| `IsDeleted` | FILTER0 (filter) |
| `KurtID__c` | DROP_FIELDS29_copy0 (schema), FORMULA20_copy0_copy0_copy0 (formula), FORMULA23_copy0_copy0_copy0 (formula) |
| `NBR_FIXED_BBB_FIBER__c` | FILTER1 (filter) |
| `Name` | FORMULA26_copy0_copy0_copy0 (formula) |
| `StatusKURT__c` | FILTER0 (filter) |

#### Fields to ELIMINATE

- `CompanyFamily__c`
- `NBR_FIBER_PAYER__c`
- `NBR_FIBER_USER__c`
- `NBR_TBB_MOBIL_PAYER__c`
- `NBR_TBB_MOBIL_USER__c`
- `NBR_TBB_MOBIL__c`
