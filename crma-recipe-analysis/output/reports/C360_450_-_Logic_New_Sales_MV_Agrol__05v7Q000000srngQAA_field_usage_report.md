# C360_450_-_Logic_New_Sales_MV_Agrol__05v7Q000000srngQAA — Field Usage Report

**Recipe:** C360_450_-_Logic_New_Sales_MV_Agrol__05v7Q000000srngQAA
**Total nodes:** 92

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET16 | Contact | connectedDataset | 4 | 4 | 0 | 0% |
| **TOTAL** | | | **26** | **26** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | DROP_FIELDS14 (schema), FILTER8_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2), FILTER17 (filter) |
| `Company_Family_Name__c` | FILTER4 (filter), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `CustomerType__c` | DROP_FIELDS14 (schema), FILTER7_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `Id` | JOIN19 (join), FILTER40 (filter), JOIN20 (join), DROP_FIELDS14 (schema), JOIN2 (join) +19 more |
| `IsDeleted` | FILTER1_copy0 (filter), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `NACE_Subclass_Description__c` | DROP_FIELDS14 (schema), FILTER6_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `NBR_FIBER_USER__c` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2), FILTER16_copy1 (filter), FILTER16_copy0_copy0 (filter) +2 more |
| `NBR_FIXED_BBB_FIBER__c` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2), FILTER16_copy1 (filter), FILTER16_copy0_copy0 (filter) +2 more |
| `NBR_TBB_MOBIL_USER__c` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2), FILTER16_copy1 (filter), FILTER16_copy0_copy0 (filter) +2 more |
| `NBR_TBB_MOBIL__c` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2), FILTER16_copy1 (filter), FILTER16_copy0_copy0 (filter) +2 more |
| `NBR_VOICE_PAYER__c` | DROP_FIELDS14 (schema), FILTER4_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `NumberOfEmployees` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2), FILTER20 (filter), FILTER15 (filter) |
| `Phonenumber_type__c` | DROP_FIELDS14 (schema), FILTER8_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2), FILTER17 (filter) |
| `Segment__c` | DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0 (filter), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |
| `SubsMobileVoice__c` | DROP_FIELDS14 (schema), FILTER4_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `TAG_TALKMORE_BEDRIFT__c` | DROP_FIELDS14 (schema), FILTER5_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | DROP_FIELDS14 (schema), FILTER5_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `TSP_Dealer__c` | DROP_FIELDS14 (schema), FILTER10_copy0_copy0 (filter), APPEND1 (appendV2), APPEND0 (appendV2) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0 (filter), DROP_FIELDS14 (schema), APPEND1 (appendV2), APPEND0 (appendV2) |

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA10_copy0 (formula), FORMULA10_copy0_copy0 (formula), JOIN18 (join) +2 more |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA11_copy0 (formula), FORMULA11_copy0_copy0 (formula) |

### Contact (`LOAD_DATASET16`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA21 (computeRelative), FORMULA22 (formula) |
| `Birthdate` | FILTER38 (filter) |
| `Id` | FORMULA21 (computeRelative), JOIN20 (join), DROP_FIELDS14 (schema), JOIN2 (join), JOIN0 (join) +18 more |
| `Primary__c` | FILTER37 (filter) |
