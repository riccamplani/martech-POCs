# C360_493_-_New_Sales_MV_NHO_Service_og_Handel__05v7Q000000cHyJQAU — Field Usage Report

**Recipe:** C360_493_-_New_Sales_MV_NHO_Service_og_Handel__05v7Q000000cHyJQAU
**Total nodes:** 39

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 6 | 6 | 0 | 0% |
| **TOTAL** | | | **26** | **26** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | APPEND0 (appendV2) |
| `CustomerType__c` | APPEND0 (appendV2) |
| `Forbund_membership__c` | FILTER2_copy1_copy0 (filter), FILTER4_copy0_copy0 (filter), APPEND0 (appendV2) |
| `Has_Subscriptions__c` | APPEND0 (appendV2) |
| `Id` | JOIN0 (join), APPEND0 (appendV2), DROP_FIELDS12_copy0 (schema), DROP_FIELDS12_copy0_copy0_copy0 (schema), APPEND1 (appendV2) +2 more |
| `IsDeleted` | FILTER1_copy0 (filter), APPEND0 (appendV2) |
| `Mobile_Voice_Penetration__c` | APPEND0 (appendV2), FILTER5 (filter) |
| `NACE_Subclass_Description__c` | APPEND0 (appendV2) |
| `NBR_VOICE_PAYER__c` | FILTER4_copy0 (filter), FILTER4_copy0_copy1 (filter), APPEND0 (appendV2) |
| `Name` | APPEND0 (appendV2) |
| `Phonenumber_type__c` | APPEND0 (appendV2) |
| `Portfolio__c` | APPEND0 (appendV2) |
| `Reservation_Date_MV_Inbound__c` | FILTER6_copy2_copy0_copy0 (filter), APPEND0 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | FILTER9_copy0 (filter), APPEND0 (appendV2) |
| `Segment__c` | APPEND0 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0 (filter), APPEND0 (appendV2) |
| `SubsMobileVoice__c` | FILTER4_copy0 (filter), FILTER4_copy0_copy1 (filter), APPEND0 (appendV2) |
| `TAG_TALKMORE_BEDRIFT__c` | APPEND0 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | APPEND0 (appendV2) |
| `mobile_service_segment__c` | FILTER3_copy0 (filter), APPEND0 (appendV2), FILTER3_copy0_copy0 (filter), FILTER3_copy0_copy0_copy0 (filter) |

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
| `Id` | FORMULA9_copy0 (formula), FORMULA10_copy0 (formula), JOIN16 (join), FILTER37 (filter) |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |
| `NumberOfEmployees` |  |
