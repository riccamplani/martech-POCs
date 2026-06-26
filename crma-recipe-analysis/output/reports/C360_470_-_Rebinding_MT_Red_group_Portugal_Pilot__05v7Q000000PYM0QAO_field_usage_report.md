# C360_470_-_Rebinding_MT_Red_group_Portugal_Pilot__05v7Q000000PYM0QAO — Field Usage Report

**Recipe:** C360_470_-_Rebinding_MT_Red_group_Portugal_Pilot__05v7Q000000PYM0QAO
**Total nodes:** 129

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 20 | 6 | 14 | 70% |
| LOAD_DATASET14 | Account | connectedDataset | 5 | 3 | 2 | 40% |
| **TOTAL** | | | **25** | **9** | **16** | **64%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 6
- **Fields unused:** 14

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER57 (filter) |
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), APPEND0 (appendV2), JOIN1 (join) +36 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `MBN_PROD_KO_ACT_DATE__c`
- `MBN_PROD_SVARSGRUPER_ACT_DATE__c`
- `Migration_flag__c`
- `Mobile_Voice_Penetration__c`
- `NBR_MBN_AVANSERT_SENTRALBORD__c`
- `NBR_MBN_SENTRALBORD__c`
- `NBR_MBN__c`
- `NBR_SAFEZONE_MOBILE__c`
- `OrgNo__c`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `Segment__c`
- `SubsMobileVoice__c`
- `TSP_Dealer__c`

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 3
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23 (formula) |
| `Id` | FORMULA9_copy0 (formula), FORMULA10_copy0 (formula), JOIN23 (join), DROP_FIELDS17 (schema), AGGREGATE5 (aggregate) +1 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |

#### Fields to ELIMINATE

- `Migration_flag__c`
- `NBR_SAFEZONE_MOBILE__c`
