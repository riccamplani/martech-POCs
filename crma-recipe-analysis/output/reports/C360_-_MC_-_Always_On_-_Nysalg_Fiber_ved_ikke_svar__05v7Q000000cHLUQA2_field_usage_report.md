# C360_-_MC_-_Always_On_-_Nysalg_Fiber_ved_ikke_svar__05v7Q000000cHLUQA2 — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Nysalg_Fiber_ved_ikke_svar__05v7Q000000cHLUQA2
**Total nodes:** 43

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 6 | 5 | 1 | 17% |
| **TOTAL** | | | **6** | **5** | **1** | **17%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 5
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER4 (filter) |
| `Id` | JOIN1 (join) |
| `Segment__c` | FILTER2 (filter) |
| `StatusKURT__c` | FILTER2 (filter) |
| `TSP_Dealer__c` | FILTER3 (filter) |

#### Fields to ELIMINATE

- `KurtID__c`
