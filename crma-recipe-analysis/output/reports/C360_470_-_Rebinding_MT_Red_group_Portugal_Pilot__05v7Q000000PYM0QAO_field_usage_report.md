# C360_470_-_Rebinding_MT_Red_group_Portugal_Pilot__05v7Q000000PYM0QAO — Field Usage Report

**Recipe:** C360_470_-_Rebinding_MT_Red_group_Portugal_Pilot__05v7Q000000PYM0QAO
**Total nodes:** 129

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET14 | Account | connectedDataset | 5 | 4 | 1 | 20% |
| **TOTAL** | | | **25** | **24** | **1** | **4%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER57 (filter), DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2) +1 more |
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), APPEND0 (appendV2), JOIN1 (join) +45 more |
| `IsDeleted` | FILTER1_copy0 (filter), DROP_FIELDS24 (schema), DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND1 (appendV2) +6 more |
| `MBN_PROD_KO_ACT_DATE__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `Migration_flag__c` | FILTER59 (filter), DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2) +6 more |
| `Mobile_Voice_Penetration__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `NBR_MBN_SENTRALBORD__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `NBR_MBN__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `NBR_SAFEZONE_MOBILE__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy0 (filter) |
| `OrgNo__c` | JOIN24 (join) |
| `Reservation_Date_MV_Inbound__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | DROP_FIELDS24 (schema), FILTER34 (filter), FILTER35 (filter), FILTER33_copy0 (filter), FILTER7_copy0_copy0 (filter) +6 more |
| `Segment__c` | DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2), APPEND4_copy0 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0 (filter), DROP_FIELDS24 (schema), APPEND1 (appendV2), APPEND3_copy0 (appendV2), APPEND2 (appendV2) +1 more |
| `SubsMobileVoice__c` | FILTER4 (filter), DROP_FIELDS24 (schema), FILTER12_copy0 (filter), FILTER13_copy0 (filter), FILTER12_copy1 (filter) +5 more |
| `TSP_Dealer__c` | DROP_FIELDS24 (schema), FILTER10_copy1 (filter), FILTER10_copy0_copy0 (filter), FILTER10_copy0 (filter), FILTER10_copy0_copy1 (filter) +4 more |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0 (filter), APPEND3_copy0 (appendV2), APPEND4_copy0 (appendV2) |

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 4
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23 (formula) |
| `Id` | FORMULA9_copy0 (formula), FORMULA10_copy0 (formula), JOIN23 (join), DROP_FIELDS17 (schema), AGGREGATE5 (aggregate) +1 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |
| `Migration_flag__c` | DROP_FIELDS17 (schema), AGGREGATE5 (aggregate) |

#### Fields to ELIMINATE

- `NBR_SAFEZONE_MOBILE__c`
