# C360_-_MC_-_Always_On_-_Onboarding_ny_Mobil_Tale_kunde__05v7Q000000PYB2QAO — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Onboarding_ny_Mobil_Tale_kunde__05v7Q000000PYB2QAO
**Total nodes:** 153

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 34 | 10 | 24 | 71% |
| LOAD_DATASET11 | Agreement__c | connectedDataset | 50 | 7 | 43 | 86% |
| LOAD_DATASET0_copy0 | Agreement__c | connectedDataset | 8 | 4 | 4 | 50% |
| LOAD_DATASET1 | BSS_Event__c | connectedDataset | 27 | 27 | 0 | 0% |
| LOAD_DATASET13_copy0_copy0 | Contact | connectedDataset | 11 | 11 | 0 | 0% |
| **TOTAL** | | | **130** | **59** | **71** | **55%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 34
- **Fields used:** 10
- **Fields unused:** 24

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | DROP_FIELDS6 (schema), DROP_FIELDS0 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema), APPEND4 (appendV2) |
| `CreatedDate` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Id` | DROP_FIELDS6 (schema), DROP_FIELDS5 (schema), DROP_FIELDS0 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema) +37 more |
| `KurtID__c` | DROP_FIELDS6 (schema), DROP_FIELDS5 (schema), DROP_FIELDS0 (schema), JOIN10 (join), JOIN11 (join) +17 more |
| `MV_FIRST_SALE_DT__c` | FILTER1 (filter), DROP_FIELDS6 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema), APPEND4 (appendV2) |
| `NEW_MV__c` | DROP_FIELDS6 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema), APPEND4 (appendV2) |
| `Name` | DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `StatusKURT__c` | DROP_FIELDS6 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema), APPEND4 (appendV2), FILTER3 (filter) |
| `SubsMobileVoice__c` | FILTER5 (filter), DROP_FIELDS6 (schema), DROP_FIELDS0 (schema), DROP_FIELDS18 (schema), DROP_FIELDS17 (schema) +3 more |
| `mobile_service_segment__c` | DROP_FIELDS0 (schema) |

#### Fields to ELIMINATE

- `Concern__c`
- `Country__c`
- `CustomerType__c`
- `DealerChain__c`
- `DealerID__c`
- `DealerSegment__c`
- `DivisionSPOC__c`
- `E_mail__c`
- `Industry__c`
- `IsDeleted`
- `IsPartner`
- `IsPersonAccount`
- `LevelOfCertification__c`
- `LevelOfComplexity__c`
- `Min_Bedrift__c`
- `NBR_VOICE__c`
- `NumberOfEmployees`
- `OrgNo__c`
- `ParentId`
- `PersonHasOptedOutOfEmail`
- `Phone`
- `Portfolio__c`
- `RecordTypeId`
- `TopLevelAccountID__c`

### Agreement__c (`LOAD_DATASET11`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 50
- **Fields used:** 7
- **Fields unused:** 43

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Agreement_Owner__c` | DROP_FIELDS19 (schema), JOIN12 (join), JOIN13 (join) |
| `Id` | JOIN12 (join), JOIN13 (join), DROP_FIELDS20 (schema), DROP_FIELDS20 (schema), JOIN6 (join) +21 more |
| `Name` | DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Parameter_1_Value__c` | JOIN14 (join) |
| `Parameter_6_Value__c` | DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema), DROP_FIELDS25_copy0 (schema), APPEND5 (appendV2), DROP_FIELDS26_copy1 (schema) +2 more |
| `Product_Name__c` | FILTER18 (filter), DROP_FIELDS19 (schema), FORMULA35 (formula), DROP_FIELDS20 (schema), DROP_FIELDS11 (schema) |
| `Start_Date__c` | FILTER18 (filter) |

#### Fields to ELIMINATE

- `Agreement_Member__c`
- `Agreement_Offer_ID__c`
- `Agreement_Sub_Type__c`
- `Agreement_Type__c`
- `CreatedById`
- `CreatedDate`
- `DRM__c`
- `End_Date__c`
- `IMEI_no__c`
- `IsDeleted`
- `LastModifiedById`
- `LastModifiedDate`
- `LastReferencedDate`
- `LastViewedDate`
- `Monthly_Price_Formatted__c`
- `Monthly_Price__c`
- `OwnerId`
- `Parameter_1_Name__c`
- `Parameter_2_Name__c`
- `Parameter_2_Value__c`
- `Parameter_3_Name__c`
- `Parameter_3_Value__c`
- `Parameter_4_Name__c`
- `Parameter_4_Value__c`
- `Parameter_5_Name__c`
- `Parameter_5_Value__c`
- `Parameter_6_Name__c`
- `Parameter_7_Name__c`
- `Parameter_7_Value__c`
- `Parameter_8_Name__c`
- `Parameter_8_Value__c`
- `Parent_Agreement__c`
- `Product_Desc__c`
- `Product_Group_List__c`
- `Product_Offer_ID__c`
- `Root_Offer_Desc__c`
- `Service_Concept__c`
- `Source_Agreement_ID__c`
- `SystemModstamp`
- `TOSS__c`
- `Terminal__c`
- `Termination_Fee__c`
- `Usage__c`

### Agreement__c (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 8
- **Fields used:** 4
- **Fields unused:** 4

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Agreement_Owner__c` | AGGREGATE1_copy0 (aggregate), AGGREGATE3_copy0 (aggregate), JOIN0_copy0 (join), JOIN1_copy0 (join), DROP_FIELDS0_copy0 (schema) +5 more |
| `Name` | DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Product_Name__c` | FILTER0_copy0 (filter), FORMULA0_copy1 (formula), FORMULA35 (formula), DROP_FIELDS20 (schema), DROP_FIELDS11 (schema) |
| `Start_Date__c` | FILTER1_copy0 (filter) |

#### Fields to ELIMINATE

- `Agreement_Type__c`
- `CreatedDate`
- `LastModifiedDate`
- `OwnerId`

### BSS_Event__c (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 27
- **Fields used:** 27
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS3 (schema), DROP_FIELDS4 (schema) |
| `CreatedById` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `CreatedDate` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Event_Id__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Event_type__c` | FILTER2 (filter), DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Id` | DROP_FIELDS1 (schema), DROP_FIELDS1 (schema), APPEND0 (appendV2), APPEND0 (appendV2), JOIN15 (join) +33 more |
| `LastModifiedById` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `LastModifiedDate` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Name` | DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `OwnerId` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_1_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_1_Value__c` | JOIN0 (join), JOIN1 (join), AGGREGATE1 (aggregate), DROP_FIELDS1 (schema), FORMULA2 (computeRelative) +7 more |
| `Parameter_2_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_2_Value__c` | AGGREGATE1 (aggregate), DROP_FIELDS1 (schema), APPEND0 (appendV2), FORMULA2_copy0 (computeRelative) |
| `Parameter_3_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_3_Value__c` | FORMULA0 (formula), FORMULA9_copy0_copy0 (formula), DROP_FIELDS1 (schema), FORMULA2 (computeRelative), APPEND0 (appendV2) |
| `Parameter_4_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_4_Value__c` | FORMULA10_copy0_copy0 (formula), DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS3 (schema), FORMULA4 (formula) |
| `Parameter_5_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_5_Value__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_6_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_6_Value__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS23 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) +5 more |
| `Parameter_7_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_7_Value__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2), DROP_FIELDS3 (schema), FORMULA5 (formula) |
| `Parameter_8_Name__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `Parameter_8_Value__c` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |
| `SystemModstamp` | DROP_FIELDS1 (schema), APPEND0 (appendV2) |

### Contact (`LOAD_DATASET13_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 11
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | DROP_FIELDS22_copy0_copy0 (schema), JOIN15 (join) |
| `Email` | DROP_FIELDS22_copy0_copy0 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema), DROP_FIELDS24_copy0 (schema) |
| `Has_eMail__c` | DROP_FIELDS22_copy0_copy0 (schema), FILTER21_copy0 (filter), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Id` | DROP_FIELDS22_copy0_copy0 (schema), JOIN15 (join), DROP_FIELDS24 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) +7 more |
| `IsDeleted` | FILTER20_copy0_copy0 (filter) |
| `Marketing_Cloud_Contact2__c` | DROP_FIELDS22_copy0_copy0 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Marketing_Cloud_Email_Bounced__c` | DROP_FIELDS22_copy0_copy0 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Name` | DROP_FIELDS22_copy0_copy0 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Non_Marketable_Contact__c` | DROP_FIELDS22_copy0_copy0 (schema), DROP_FIELDS24 (schema), DROP_FIELDS24_copy0 (schema) |
| `Primary__c` | FILTER20_copy0_copy0 (filter), DROP_FIELDS22_copy0_copy0 (schema), FILTER21 (filter), FILTER21_copy0 (filter), DROP_FIELDS24 (schema) +1 more |
| `StatusKURT__c` | FILTER20_copy0_copy0 (filter) |
