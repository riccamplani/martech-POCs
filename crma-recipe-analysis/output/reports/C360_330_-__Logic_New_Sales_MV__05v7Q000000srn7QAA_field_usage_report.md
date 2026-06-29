# C360_330_-__Logic_New_Sales_MV__05v7Q000000srn7QAA — Field Usage Report

**Recipe:** C360_330_-__Logic_New_Sales_MV__05v7Q000000srn7QAA
**Total nodes:** 68

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 19 | 19 | 0 | 0% |
| **TOTAL** | | | **19** | **19** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 19
- **Fields used:** 19
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER8 (filter), APPEND2 (appendV2), APPEND1 (appendV2) +3 more |
| `CustomerType__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER7 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `Forbund_membership__c` | FILTER2_copy0 (filter), FILTER2_copy1 (filter), APPEND0 (appendV2), FILTER4_copy0 (filter), DROP_FIELDS8 (schema) +2 more |
| `Has_Subscriptions_Actual__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2), FILTER14 (filter) +1 more |
| `Has_Subscriptions__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2) |
| `Id` | APPEND0 (appendV2), JOIN3 (join), DROP_FIELDS0 (schema), DROP_FIELDS8 (schema), DROP_FIELDS3 (schema) +16 more |
| `IsDeleted` | FILTER1 (filter), APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2) |
| `NACE_Subclass_Description__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER6_copy0 (filter), FILTER6 (filter), APPEND2 (appendV2) +1 more |
| `NBR_VOICE_PAYER__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER4 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `Name` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER6 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy1 (filter), APPEND0 (appendV2) |
| `Phonenumber_type__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER8 (filter), APPEND2 (appendV2), APPEND1 (appendV2) +3 more |
| `Portfolio__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER16 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `Segment__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2) |
| `StatusKURT__c` | FILTER1 (filter), APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2) |
| `SubsMobileVoice__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER4 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `TAG_TALKMORE_BEDRIFT__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER5 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | APPEND0 (appendV2), DROP_FIELDS8 (schema), FILTER5 (filter), APPEND2 (appendV2), APPEND1 (appendV2) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy1 (filter), APPEND0 (appendV2), DROP_FIELDS8 (schema), APPEND2 (appendV2), APPEND1 (appendV2) |
