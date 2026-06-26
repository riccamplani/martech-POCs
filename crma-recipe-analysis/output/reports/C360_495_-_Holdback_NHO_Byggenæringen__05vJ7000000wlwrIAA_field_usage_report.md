# C360_495_-_Holdback_NHO_Byggenæringen__05vJ7000000wlwrIAA — Field Usage Report

**Recipe:** C360_495_-_Holdback_NHO_Byggenæringen__05vJ7000000wlwrIAA
**Total nodes:** 142

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 22 | 9 | 13 | 59% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 6 | 2 | 4 | 67% |
| **TOTAL** | | | **28** | **11** | **17** | **61%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 22
- **Fields used:** 9
- **Fields unused:** 13

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER2_copy1_copy0 (filter), FILTER4_copy0_copy0 (filter) |
| `Id` | JOIN0 (join), JOIN18 (join), DROP_FIELDS14 (schema), APPEND1 (appendV2), DROP_FIELDS12_copy0_copy0_copy0_copy0 (schema) +22 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `KurtID__c` | JOIN17 (join), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `Reservation_Date_MV_Inbound__c` | FILTER6_copy2_copy0_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | FILTER9_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `SubsMobileVoice__c` | FILTER3_copy0_copy0_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0 (filter), FILTER3_copy0_copy0_copy0 (filter), FILTER3_copy0_copy0_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `COM_CUSTOMER_PHONENBR_STATUS__c`
- `CustomerType__c`
- `Has_Subscriptions__c`
- `Mobile_Voice_Penetration__c`
- `NACE_Subclass_Description__c`
- `NBR_VOICE_PAYER__c`
- `Name`
- `NumberOfEmployees`
- `Phonenumber_type__c`
- `Portfolio__c`
- `Segment__c`
- `TAG_TALKMORE_BEDRIFT__c`
- `TAG_TALKMORE_PRIVATE__c`

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 2
- **Fields unused:** 4

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula) +23 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula) +9 more |

#### Fields to ELIMINATE

- `FORBUND_START_DATE__c`
- `Forbund_membership__c`
- `Has_Subscriptions__c`
- `NumberOfEmployees`
