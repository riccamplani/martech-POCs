# C360_-_MC_-_Always_On_-_Fiber_nysalg_-_Har_fiber_gjennom_utleier_3_part__05vJ7000000wkY5IAI — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Fiber_nysalg_-_Har_fiber_gjennom_utleier_3_part__05vJ7000000wkY5IAI
**Total nodes:** 45

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 11 | 10 | 1 | 9% |
| **TOTAL** | | | **11** | **10** | **1** | **9%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 10
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER4 (filter) |
| `DPSS_Segment__c` | FILTER2 (filter) |
| `Has_Subscriptions_Actual__c` | FORMULA39 (formula) |
| `Id` | FORMULA0_copy0 (formula), JOIN0_copy0 (join) |
| `NBR_FIBER_USER__c` | FILTER0_copy0 (filter) |
| `NBR_FIXED_BBB_FIBER__c` | FILTER0_copy0 (filter) |
| `NBR_TBB_MOBIL_USER__c` | FILTER0_copy0 (filter) |
| `NBR_TBB_MOBIL__c` | FILTER0_copy0 (filter) |
| `StatusKURT__c` | FILTER2 (filter) |
| `TSP_Dealer__c` | FILTER3 (filter) |

#### Fields to ELIMINATE

- `KurtID__c`
