# C360_440_-__Logic_Mobile_Voice_Rebinding__05v7Q000000srnbQAA — Field Usage Report

**Recipe:** C360_440_-__Logic_Mobile_Voice_Rebinding__05v7Q000000srnbQAA
**Total nodes:** 292

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 21 | 21 | 0 | 0% |
| LOAD_DATASET14 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| **TOTAL** | | | **28** | **28** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER57 (filter), DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2) +6 more |
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), APPEND0 (appendV2), JOIN1 (join) +112 more |
| `IsDeleted` | FILTER1_copy0 (filter), DROP_FIELDS24 (schema), DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND15 (appendV2) +16 more |
| `MBN_PROD_KO_ACT_DATE__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `Migration_flag__c` | FILTER59 (filter), DROP_FIELDS1 (schema), DROP_FIELDS24 (schema), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy0_copy0 (schema), APPEND19 (appendV2) +35 more |
| `Mobile_Voice_Penetration__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +5 more |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `NBR_MBN_SENTRALBORD__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `NBR_MBN__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `NBR_OPPDATERT__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +7 more |
| `NBR_SAFEZONE_MOBILE__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +9 more |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy0 (filter) |
| `OrgNo__c` | JOIN23 (join) |
| `Reservation_Date_MV_Inbound__c` | DROP_FIELDS1 (schema), FILTER6_copy0 (filter), DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2) +7 more |
| `Reservation_Date_MV_Outbound__c` | DROP_FIELDS24 (schema), FILTER33 (filter), FILTER7_copy0 (filter), FILTER32 (filter), FILTER34 (filter) +13 more |
| `Segment__c` | DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2), APPEND4 (appendV2) +5 more |
| `StatusKURT__c` | FILTER1_copy0 (filter), DROP_FIELDS24 (schema), APPEND15 (appendV2), APPEND3 (appendV2), APPEND1 (appendV2) +6 more |
| `SubsMobileVoice__c` | FILTER4 (filter), DROP_FIELDS24 (schema), FILTER12_copy0 (filter), FILTER13_copy0 (filter), APPEND15 (appendV2) +10 more |
| `TSP_Dealer__c` | DROP_FIELDS24 (schema), FILTER10 (filter), FILTER10_copy1 (filter), FILTER10_copy0_copy0 (filter), FILTER10_copy0 (filter) +9 more |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0 (filter), DROP_FIELDS1 (schema), FILTER71 (filter), DROP_FIELDS24 (schema), FILTER70 (filter) +9 more |

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy1 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula) +23 more |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy1 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula) +7 more |
| `Migration_flag__c` | FORMULA0 (formula), FORMULA0_copy0 (formula), FORMULA0_copy0_copy0 (formula), FORMULA0_copy0_copy0_copy0 (formula), FORMULA0_copy0_copy1 (formula) +12 more |
| `Mobile_Voice_Penetration__c` | FORMULA30 (formula), FORMULA28 (formula) |
| `NBR_SAFEZONE_MOBILE__c` | FORMULA0 (formula), FORMULA24 (formula), FORMULA27 (formula) |
| `NumberofEmployees_clean__c` | FORMULA29 (formula) |
