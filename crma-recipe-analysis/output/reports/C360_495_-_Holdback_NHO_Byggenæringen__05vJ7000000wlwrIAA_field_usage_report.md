# C360_495_-_Holdback_NHO_Byggenæringen__05vJ7000000wlwrIAA — Field Usage Report

**Recipe:** C360_495_-_Holdback_NHO_Byggenæringen__05vJ7000000wlwrIAA
**Total nodes:** 142

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 22 | 22 | 0 | 0% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 6 | 6 | 0 | 0% |
| **TOTAL** | | | **28** | **28** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 22
- **Fields used:** 22
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` |  |
| `CustomerType__c` |  |
| `Forbund_membership__c` | FILTER2_copy1_copy0 (filter), FILTER4_copy0_copy0 (filter) |
| `Has_Subscriptions__c` |  |
| `Id` | JOIN0 (join), JOIN18 (join), DROP_FIELDS14 (schema), APPEND1 (appendV2), DROP_FIELDS12_copy0_copy0_copy0_copy0 (schema) +22 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `KurtID__c` | JOIN17 (join), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `Mobile_Voice_Penetration__c` |  |
| `NACE_Subclass_Description__c` |  |
| `NBR_VOICE_PAYER__c` |  |
| `Name` |  |
| `NumberOfEmployees` |  |
| `Phonenumber_type__c` |  |
| `Portfolio__c` |  |
| `Reservation_Date_MV_Inbound__c` | FILTER6_copy2_copy0_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | FILTER9_copy0 (filter) |
| `Segment__c` |  |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `SubsMobileVoice__c` | FILTER3_copy0_copy0_copy0 (filter) |
| `TAG_TALKMORE_BEDRIFT__c` |  |
| `TAG_TALKMORE_PRIVATE__c` |  |
| `mobile_service_segment__c` | FILTER3_copy0_copy0 (filter), FILTER3_copy0_copy0_copy0 (filter), FILTER3_copy0_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 6
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` |  |
| `Forbund_membership__c` |  |
| `Has_Subscriptions__c` |  |
| `Id` | FORMULA9_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula) +23 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula) +9 more |
| `NumberOfEmployees` |  |
