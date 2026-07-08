# C360_497_-_New_Sales_MV_Campaign_-_Medium__05vdV00000EcBQvQAN — Field Usage Report

**Recipe:** C360_497_-_New_Sales_MV_Campaign_-_Medium__05vdV00000EcBQvQAN
**Total nodes:** 236

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 27 | 11 | 16 | 59% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0 | Account | connectedDataset | 7 | 6 | 1 | 14% |
| LOAD_DATASET0_copy0_copy0 | Account | connectedDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 7 | 6 | 1 | 14% |
| LOAD_DATASET0_copy0_copy5_copy0 | Account | connectedDataset | 24 | 5 | 19 | 79% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 7 | 5 | 2 | 29% |
| LOAD_DATASET0_copy0_copy5_copy0_copy0_copy0 | Account | connectedDataset | 4 | 3 | 1 | 25% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 8 | 3 | 5 | 62% |
| LOAD_DATASET0_copy0_copy5_copy0_copy0_copy1 | Account | connectedDataset | 24 | 5 | 19 | 79% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy1 | Account | connectedDataset | 7 | 5 | 2 | 29% |
| LOAD_DATASET2_copy0_copy1_copy0 | Contact | connectedDataset | 10 | 2 | 8 | 80% |
| LOAD_DATASET2_copy0_copy1_copy0_copy0_copy0 | Contact | connectedDataset | 10 | 2 | 8 | 80% |
| **TOTAL** | | | **139** | **57** | **82** | **59%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 27
- **Fields used:** 11
- **Fields unused:** 16

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` | FILTER5 (filter) |
| `Company_Family_Name__c` | FILTER4_copy0_copy0_copy0 (filter) |
| `Concern__c` | FILTER6 (filter) |
| `Forbund_membership__c` | FILTER4_copy0_copy0_copy0 (filter) |
| `Id` | JOIN0 (join), JOIN32_copy0 (join), DROP_FIELDS12_copy0_copy0_copy0 (schema), JOIN26_copy0_copy0 (join), FILTER107 (filter) |
| `IsDeleted` | FILTER1_copy0_copy0 (filter) |
| `Mobile_Segment__c` | FILTER3_copy0_copy0_copy0 (filter) |
| `Mobile_Voice_Penetration__c` | FILTER4 (filter) |
| `Name` | FILTER2_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | FILTER7_copy1 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `COM_CUSTOMER_PHONENBR_STATUS__c`
- `CustomerType__c`
- `NACE_Subclass_Description__c`
- `NBR_FIBER_USER__c`
- `NBR_FIXED_BBB_FIBER__c`
- `NBR_TBB_MOBIL_USER__c`
- `NBR_TBB_MOBIL__c`
- `NBR_VOICE_PAYER__c`
- `NumberOfEmployees`
- `Phonenumber_type__c`
- `Segment__c`
- `SubsMobileVoice__c`
- `TAG_TALKMORE_BEDRIFT__c`
- `TAG_TALKMORE_PRIVATE__c`
- `TSP_Dealer__c`
- `mobile_service_segment__c`

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 6
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0 (formula), JOIN26_copy0_copy0 (join), FILTER107 (filter) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy0 (formula) |

#### Fields to ELIMINATE

- `OrgNo__c`

### Account (`LOAD_DATASET0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN33 (join), DROP_FIELDS12_copy1_copy0 (schema), JOIN26_copy0_copy0_copy0 (join) |
| `IsDeleted` | FILTER1_copy0_copy0_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | FILTER7_copy1_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 6
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy0 (formula), JOIN26_copy0_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |

#### Fields to ELIMINATE

- `OrgNo__c`

### Account (`LOAD_DATASET0_copy0_copy5_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 24
- **Fields used:** 5
- **Fields unused:** 19

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN1_copy0_copy0 (join), FORMULA1_copy1_copy0 (computeRelative), JOIN33_copy0 (join), FILTER100_copy0 (filter), JOIN35_copy0 (join) +4 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy3_copy0 (filter) |
| `NumberOfEmployees` | FILTER103 (filter), FILTER104 (filter) |
| `Phonenumber_type__c` | FILTER15_copy0_copy2_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy3_copy0 (filter) |

#### Fields to ELIMINATE

- `Account_Owner_Full_Name__c`
- `COM_CUSTOMER_EDM_RESERVATION__c`
- `CompanyFamily__c`
- `Company_Family_Name__c`
- `Concern__c`
- `Forbund_membership__c`
- `Has_Min_Bedrift__c`
- `KurtID__c`
- `Last_Min_Bedrift_Web_Login__c`
- `MV_FIRST_SALE_DT__c`
- `NBR_OPPDATERT__c`
- `NBR_SAFEZONE_MOBILE__c`
- `NBR_SOURCE_ACCOUNT_ID_MOBIL__c`
- `Name`
- `PersonHasOptedOutOfEmail`
- `SOURCE_ACCOUNT_ID_MOBIL__c`
- `SubsMobileVoice__c`
- `TSP_Dealer__c`
- `mobile_service_segment__c`

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 5
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula), JOIN26_copy0_copy0_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0 (formula) |

#### Fields to ELIMINATE

- `FORBUND_START_DATE__c`
- `OrgNo__c`

### Account (`LOAD_DATASET0_copy0_copy5_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 3
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN36_copy0 (join), FILTER105_copy0 (filter), JOIN37_copy0 (join), DROP_FIELDS12_copy0_copy1_copy0_copy1_copy0_copy0 (schema), JOIN39_copy0 (join) +1 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy3_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy3_copy0_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `KurtID__c`

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 8
- **Fields used:** 3
- **Fields unused:** 5

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN38_copy0 (join), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy0 (formula), JOIN39_copy0 (join), FILTER106 (filter) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy0 (formula) |
| `Mobile_Voice_Penetration__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy0 (formula) |

#### Fields to ELIMINATE

- `FORBUND_START_DATE__c`
- `Forbund_membership__c`
- `Has_Subscriptions_Actual__c`
- `NumberOfEmployees`
- `OrgNo__c`

### Account (`LOAD_DATASET0_copy0_copy5_copy0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 24
- **Fields used:** 5
- **Fields unused:** 19

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN1_copy0_copy0_copy0_copy0 (join), FORMULA1_copy1_copy0_copy0_copy0 (computeRelative), JOIN33_copy0_copy0_copy0 (join), FILTER100_copy0_copy0_copy0 (filter), JOIN35_copy0_copy0_copy0 (join) +4 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy3_copy0_copy0_copy1 (filter) |
| `NumberOfEmployees` | FILTER103_copy0_copy0 (filter), FILTER104_copy0_copy0 (filter) |
| `Phonenumber_type__c` | FILTER15_copy0_copy2_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy3_copy0_copy0_copy1 (filter) |

#### Fields to ELIMINATE

- `Account_Owner_Full_Name__c`
- `COM_CUSTOMER_EDM_RESERVATION__c`
- `CompanyFamily__c`
- `Company_Family_Name__c`
- `Concern__c`
- `Forbund_membership__c`
- `Has_Min_Bedrift__c`
- `KurtID__c`
- `Last_Min_Bedrift_Web_Login__c`
- `MV_FIRST_SALE_DT__c`
- `NBR_OPPDATERT__c`
- `NBR_SAFEZONE_MOBILE__c`
- `NBR_SOURCE_ACCOUNT_ID_MOBIL__c`
- `Name`
- `PersonHasOptedOutOfEmail`
- `SOURCE_ACCOUNT_ID_MOBIL__c`
- `SubsMobileVoice__c`
- `TSP_Dealer__c`
- `mobile_service_segment__c`

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 5
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula), JOIN26_copy0_copy0_copy0_copy0_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy1_copy0_copy0_copy1 (formula) |

#### Fields to ELIMINATE

- `FORBUND_START_DATE__c`
- `OrgNo__c`

### Contact (`LOAD_DATASET2_copy0_copy1_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 2
- **Fields unused:** 8

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | DROP_FIELDS0_copy2_copy0 (schema), FORMULA0_copy0_copy0 (formula) |
| `Id` | DROP_FIELDS0_copy2_copy0 (schema), JOIN0_copy2_copy0 (join), JOIN1_copy0_copy0 (join), FORMULA1_copy1_copy0 (computeRelative), JOIN33_copy0 (join) +6 more |

#### Fields to ELIMINATE

- `AccountId__c`
- `IsDeleted`
- `Key_contact__c`
- `MBSuperadmin__c`
- `MB_Admin__c`
- `Name`
- `Primary__c`
- `StatusKURT__c`

### Contact (`LOAD_DATASET2_copy0_copy1_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 2
- **Fields unused:** 8

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | DROP_FIELDS0_copy2_copy0_copy0_copy0 (schema), FORMULA0_copy0_copy0_copy0_copy0 (formula), FORMULA0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Id` | DROP_FIELDS0_copy2_copy0_copy0_copy0 (schema), JOIN0_copy2_copy0_copy0_copy0 (join), JOIN36_copy1 (join), JOIN1_copy0_copy0_copy0_copy0 (join), FORMULA1_copy1_copy0_copy0_copy0 (computeRelative) +7 more |

#### Fields to ELIMINATE

- `AccountId__c`
- `IsDeleted`
- `Key_contact__c`
- `MBSuperadmin__c`
- `MB_Admin__c`
- `Name`
- `Primary__c`
- `StatusKURT__c`
