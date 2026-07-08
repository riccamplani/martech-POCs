# C360_480_-_Rebinding_Forbund__05v7Q000000PYX3QAO — Field Usage Report

**Recipe:** C360_480_-_Rebinding_Forbund__05v7Q000000PYX3QAO
**Total nodes:** 192

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 21 | 21 | 0 | 0% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 5 | 4 | 1 | 20% |
| **TOTAL** | | | **26** | **25** | **1** | **4%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER64 (filter), APPEND26 (appendV2), APPEND27 (appendV2) |
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), JOIN1 (join), FORMULA24 (computeRelative) +37 more |
| `IsDeleted` | FILTER1_copy0 (filter), APPEND26 (appendV2), APPEND26 (appendV2), APPEND27 (appendV2), APPEND27 (appendV2) |
| `MBN_PROD_KO_ACT_DATE__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `Migration_flag__c` | FILTER59_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), DROP_FIELDS25 (schema), FILTER59_copy0_copy0_copy0 (filter) +3 more |
| `Mobile_Segment__c` | APPEND26 (appendV2), APPEND27 (appendV2), DROP_FIELDS25 (schema) |
| `Mobile_Voice_Penetration__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `NBR_MBN_SENTRALBORD__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `NBR_MBN__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `NBR_SAFEZONE_MOBILE__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `NumberOfEmployees` | FILTER3_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2) |
| `OrgNo__c` | JOIN23 (join), APPEND26 (appendV2), APPEND27 (appendV2) |
| `Reservation_Date_MV_Inbound__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | APPEND26 (appendV2), FILTER34_copy0 (filter), APPEND27 (appendV2) |
| `Segment__c` | APPEND26 (appendV2), APPEND27 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2) |
| `SubsMobileVoice__c` | FILTER4 (filter), APPEND26 (appendV2), APPEND27 (appendV2) |
| `TSP_Dealer__c` | FILTER67 (filter), APPEND26 (appendV2), APPEND27 (appendV2) |
| `mobile_service_segment__c` | FILTER3_copy0 (filter), FILTER69 (filter), FILTER3_copy0_copy0 (filter), DROP_FIELDS25 (schema), FILTER69_copy0 (filter) +7 more |

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 4
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0 (formula) +28 more |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0 (formula) +11 more |
| `Migration_flag__c` | FORMULA0_copy0_copy0 (formula), FORMULA0_copy0_copy0_copy0_copy0 (formula) |

#### Fields to ELIMINATE

- `NBR_SAFEZONE_MOBILE__c`
