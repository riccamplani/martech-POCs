# C360_-_MC_-_Always_On_-_Fiber_nysalg_-_Har_fiber_gjennom_utleier_3_part__05vJ7000000wkY5IAI — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Fiber_nysalg_-_Har_fiber_gjennom_utleier_3_part__05vJ7000000wkY5IAI
**Total nodes:** 45

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 11 | 11 | 0 | 0% |
| **TOTAL** | | | **11** | **11** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 11
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER4 (filter), DROP_FIELDS1 (schema) |
| `DPSS_Segment__c` | FILTER2 (filter), DROP_FIELDS1 (schema) |
| `Has_Subscriptions_Actual__c` | DROP_FIELDS1 (schema), FORMULA39 (formula) |
| `Id` | FORMULA0_copy0 (formula), JOIN0_copy0 (join), JOIN1 (join), JOIN2 (join), JOIN3 (join) +8 more |
| `KurtID__c` | DROP_FIELDS1 (schema), DROP_FIELDS12 (schema) |
| `NBR_FIBER_USER__c` | FILTER0_copy0 (filter), DROP_FIELDS1 (schema) |
| `NBR_FIXED_BBB_FIBER__c` | FILTER0_copy0 (filter), DROP_FIELDS1 (schema) |
| `NBR_TBB_MOBIL_USER__c` | FILTER0_copy0 (filter), DROP_FIELDS1 (schema) |
| `NBR_TBB_MOBIL__c` | FILTER0_copy0 (filter), DROP_FIELDS1 (schema) |
| `StatusKURT__c` | FILTER2 (filter), DROP_FIELDS1 (schema) |
| `TSP_Dealer__c` | FILTER3 (filter), DROP_FIELDS1 (schema) |
