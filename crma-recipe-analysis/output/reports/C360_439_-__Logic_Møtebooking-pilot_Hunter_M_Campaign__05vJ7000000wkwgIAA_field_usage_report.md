# C360_439_-__Logic_Møtebooking-pilot_Hunter_M_Campaign__05vJ7000000wkwgIAA — Field Usage Report

**Recipe:** C360_439_-__Logic_Møtebooking-pilot_Hunter_M_Campaign__05vJ7000000wkwgIAA
**Total nodes:** 62

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 26 | 25 | 1 | 4% |
| **TOTAL** | | | **26** | **25** | **1** | **4%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 25
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | DROP_FIELDS0 (schema) |
| `COM_CUSTOMER_TM_RESERVATION__c` | DROP_FIELDS0 (schema) |
| `Company_Family_Name__c` | DROP_FIELDS0 (schema), DROP_FIELDS15 (schema) |
| `CustomerType__c` | FILTER41_copy1_copy0 (filter) |
| `Forbund_membership__c` | FILTER38 (filter), FILTER41 (filter), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema), FORMULA14 (formula) |
| `Has_Subscriptions_Actual__c` | DROP_FIELDS0 (schema), FORMULA3 (formula), DROP_FIELDS15 (schema), FORMULA5 (formula), DROP_FIELDS6_copy0 (schema) |
| `Id` | DROP_FIELDS9_copy0 (schema), DROP_FIELDS11_copy0 (schema), DROP_FIELDS9_copy0_copy0 (schema), DROP_FIELDS16 (schema), APPEND0 (appendV2) +14 more |
| `Industry__c` | DROP_FIELDS0 (schema), DROP_FIELDS15 (schema) |
| `Industry_group__c` | DROP_FIELDS0 (schema) |
| `IsDeleted` | DROP_FIELDS0 (schema) |
| `KurtID__c` | DROP_FIELDS0 (schema), DROP_FIELDS15 (schema), FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |
| `Latest_Port_out_date__c` | FILTER37 (filter), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema) |
| `Mobile_Voice_Penetration__c` | FILTER0 (filter) |
| `NACE_Subclass_Code__c` | FILTER41_copy1_copy0 (filter) |
| `Name` | FILTER2_copy0 (filter), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema), FORMULA12_copy0 (formula) |
| `NumberOfEmployees` | FILTER0 (filter), FORMULA0 (formula), DROP_FIELDS0 (schema) |
| `OrgNo__c` | DROP_FIELDS0 (schema), DROP_FIELDS15 (schema) |
| `Phone` | DROP_FIELDS0 (schema) |
| `Phonenumber_type__c` | FILTER3_copy0 (filter), DROP_FIELDS0 (schema) |
| `Reservation_Date_MV_Outbound__c` | FILTER4 (filter) |
| `StatusKURT__c` | FILTER0 (filter), DROP_FIELDS0 (schema) |
| `SubsMobileVoice__c` | FILTER0 (filter), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema), FORMULA5 (formula), DROP_FIELDS6_copy0 (schema) |
| `VisitingCounty__c` | FORMULA1 (formula), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema), FORMULA4 (formula) |
| `alternate_phone__c` | DROP_FIELDS0 (schema) |
| `mobile_service_segment__c` | FILTER0 (filter), DROP_FIELDS0 (schema), DROP_FIELDS15 (schema) |

#### Fields to ELIMINATE

- `NACE_Subclass_Description__c`
