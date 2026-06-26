# C360_480_-_Rebinding_Forbund__05v7Q000000PYX3QAO — Field Usage Report

**Recipe:** C360_480_-_Rebinding_Forbund__05v7Q000000PYX3QAO
**Total nodes:** 192

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 21 | 6 | 15 | 71% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 5 | 4 | 1 | 20% |
| **TOTAL** | | | **26** | **10** | **16** | **62%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 6
- **Fields unused:** 15

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), JOIN1 (join), FORMULA24 (computeRelative) +35 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `NumberOfEmployees` | FILTER3_copy0 (filter) |
| `OrgNo__c` | JOIN23 (join) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0 (filter) |

#### Fields to ELIMINATE

- `Forbund_membership__c`
- `MBN_PROD_KO_ACT_DATE__c`
- `MBN_PROD_SVARSGRUPER_ACT_DATE__c`
- `Migration_flag__c`
- `Mobile_Segment__c`
- `Mobile_Voice_Penetration__c`
- `NBR_MBN_AVANSERT_SENTRALBORD__c`
- `NBR_MBN_SENTRALBORD__c`
- `NBR_MBN__c`
- `NBR_SAFEZONE_MOBILE__c`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `Segment__c`
- `SubsMobileVoice__c`
- `TSP_Dealer__c`

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
