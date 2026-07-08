# C360_460_-_Logic_Vekst_to_Verdi_Campaign__05v7Q000000PY0EQAW — Field Usage Report

**Recipe:** C360_460_-_Logic_Vekst_to_Verdi_Campaign__05v7Q000000PY0EQAW
**Total nodes:** 157

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 18 | 15 | 3 | 17% |
| LOAD_DATASET14 | Account | connectedDataset | 4 | 4 | 0 | 0% |
| **TOTAL** | | | **22** | **19** | **3** | **14%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 18
- **Fields used:** 15
- **Fields unused:** 3

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN0 (join), JOIN10 (join), JOIN11 (join), JOIN15 (join), JOIN16 (join) +35 more |
| `Industry__c` | FILTER56 (filter) |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `MBN_PROD_KO_ACT_DATE__c` | FILTER48_copy0_copy0 (filter), FILTER48_copy0_copy0_copy0 (filter), FILTER48_copy0_copy0_copy1 (filter) |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | FILTER48_copy0_copy0 (filter), FILTER48_copy0_copy0_copy0 (filter), FILTER48_copy0_copy0_copy1 (filter) |
| `MPORT_FLG__c` | FILTER65 (filter) |
| `Migration_flag__c` | FILTER54 (filter), APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND7 (appendV2) +2 more |
| `Mobile_Voice_Penetration__c` | FILTER6_copy0_copy0_copy0 (filter), FILTER6_copy0 (filter) |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | FILTER48_copy0_copy0 (filter), FILTER48_copy0_copy0_copy0 (filter), FILTER48_copy0_copy0_copy1 (filter) |
| `NBR_MBN_SENTRALBORD__c` | FILTER48_copy0_copy0 (filter), FILTER48_copy0_copy0_copy0 (filter), FILTER48_copy0_copy0_copy1 (filter) |
| `NBR_MBN__c` | FILTER46_copy0 (filter), FILTER46_copy0_copy0 (filter), FILTER46_copy0_copy1 (filter), FILTER46_copy0_copy0_copy0 (filter) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `TSP_Dealer__c` | FILTER63 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `SUM_POTENTIAL__c`
- `Segment__c`
- `Service_segment__c`

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23_copy0 (formula) |
| `Id` | FORMULA9_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy1 (formula), FORMULA9_copy0_copy1_copy0 (formula), FORMULA10_copy0 (formula) +15 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy1 (formula), FORMULA8_copy0_copy1_copy0 (formula), FORMULA11_copy0 (formula) +3 more |
| `Migration_flag__c` | FORMULA19_copy0 (formula), FORMULA19_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0_copy0 (formula), DROP_FIELDS11_copy0 (schema) +9 more |
