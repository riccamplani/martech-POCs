# C360 210 — Field Usage Report

**Recipe:** C360 210 - Logic Calculated Items
**Total nodes:** 398
**Total load nodes:** 12

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET7 | Account | connectedDataset | 58 | 16 | 42 | 72% |
| LOAD_DATASET11 | Account | connectedDataset | 3 | 2 | 1 | 33% |
| LOAD_DATASET5_copy0_copy0 | Account_Location__c | connectedDataset | 21 | 21 | 0 | 0% |
| LOAD_DATASET1_copy0_copy0 | BSS_Event__c | connectedDataset | 27 | 7 | 20 | 74% |
| LOAD_DATASET0_copy0 | Blacklist main | analyticsDataset | 6 | 6 | 0 | 0% |
| LOAD_DATASET10 | C360_eDM_Master | analyticsDataset | 6 | 5 | 1 | 17% |
| LOAD_DATASET3 | Case | connectedDataset | 10 | 10 | 0 | 0% |
| LOAD_DATASET6 | Contact | connectedDataset | 50 | 14 | 36 | 72% |
| LOAD_DATASET8 | Fiber nysalg Region postnummer | analyticsDataset | 5 | 1 | 4 | 80% |
| LOAD_DATASET2_copy0 | Opportunity | connectedDataset | 15 | 14 | 1 | 7% |
| LOAD_DATASET4 | Subscription__c | connectedDataset | 18 | 10 | 8 | 44% |
| LOAD_DATASET12 | Suppressions - Low Priority NACE-Codes - TM New Sales MV | analyticsDataset | 2 | 1 | 1 | 50% |
| **TOTAL** | | | **221** | **107** | **114** | **52%** |

## Detail per Source Object

### Account (`LOAD_DATASET7`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 58
- **Fields used:** 16
- **Fields unused:** 42

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Company_Family_Name__c` | FILTER8_copy0_copy0_copy0 (filter) |
| `CustomerType__c` | FILTER42 (filter) |
| `DPSS_Segment__c` | DROP_FIELDS25 (schema), FILTER40 (filter) |
| `Forbund_membership__c` | FILTER41 (filter) |
| `Id` | DROP_FIELDS25 (schema), APPEND1_copy1 (appendV2), FORMULA51 (formula), FORMULA55 (formula), DROP_FIELDS0_copy0_copy3 (schema) +14 more |
| `IsDeleted` | FILTER42 (filter) |
| `KurtID__c` | JOIN0_copy0 (join), JOIN21 (join), APPEND1_copy1 (appendV2), DROP_FIELDS0_copy0_copy3 (schema), JOIN20 (join) |
| `Latest_Port_out_date__c` | FILTER35 (filter) |
| `Name` | FILTER8_copy0_copy0_copy0 (filter) |
| `NumberOfEmployees` | FORMULA47 (formula) |
| `OrgNo__c` | FILTER8_copy0_copy0_copy0 (filter) |
| `Phone` | JOIN1_copy1 (join), JOIN2_copy1 (join), FILTER42 (filter), JOIN18 (join), APPEND1_copy1 (appendV2) +1 more |
| `StatusKURT__c` | FILTER42 (filter) |
| `SubsMobileVoice__c` | FILTER5_copy0_copy0 (filter), DROP_FIELDS0_copy0_copy3 (schema) |
| `VisitingZipcode__c` | JOIN19 (join) |
| `mobile_service_segment__c` | FORMULA47 (formula) |

#### Fields to ELIMINATE

- `CompanyFamily__c`
- `Concern__c`
- `Country__c`
- `CreatedDate`
- `DealerChain__c`
- `DealerID__c`
- `DivisionSPOC__c`
- `E_mail__c`
- `Industry__c`
- `IsPartner`
- `IsPersonAccount`
- `LevelOfCertification__c`
- `LevelOfComplexity__c`
- `MDRevFixedL12__c`
- `MDRevIDCL12__c`
- `MDRevMobileL12__c`
- `MDRevTotTelenorL12__c`
- `MDSubsFixedBroadband__c`
- `MDSubsMobileBroadband__c`
- `MDSubsMobileVoice__c`
- `MDSubsNordicConnectIPVPNAccess__c`
- `MDSubsPOTSBLines__c`
- `MDSubsPOTS__c`
- `MRevFixedL12__c`
- `MRevIDCL12__c`
- `MRevMobileL12__c`
- `MRevTotTelenorL12__c`
- `MSubsFixedBroadband__c`
- `MSubsMobileBroadband__c`
- `MSubsMobileVoice__c`
- `MSubsNordicConnectIPVPNAccess__c`
- `MSubsPOTSBLines__c`
- `MSubsPOTS__c`
- `MarketArea__c`
- `Min_Bedrift__c`
- `ParentId`
- `PersonHasOptedOutOfEmail`
- `Portfolio__c`
- `PostalCity__c`
- `RecordTypeId`
- `Segment__c`
- `TopLevelAccountID__c`

### Account (`LOAD_DATASET11`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 3
- **Fields used:** 2
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA72 (formula) |
| `NACE_Subclass_Code__c` | JOIN24 (join) |

#### Fields to ELIMINATE

- `NACE_Subclass_Description__c`

### Account_Location__c (`LOAD_DATASET5_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Active_subs__c` | FILTER13_copy0_copy0_copy0_copy0_copy0 (filter), APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `Address_Id__c` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `BUILDING_TYPE_LEVEL_2__c` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `BUILDING_TYPE_LEVEL_3__c` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `Building_type__c` | FILTER33_copy0_copy0 (filter), FILTER38 (filter), APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `COVERAGE_START_DATE_5G__c` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `Capacity_code__c` | FILTER13_copy0_copy0_copy0_copy0_copy0 (filter), FORMULA1_copy0_copy0_copy0_copy0 (formula), APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema) +3 more |
| `Coverage_4GP40__c` | APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `Coverage_4G_Plus__c` | APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `Coverage_4G__c` | FILTER13_copy0_copy0_copy0_copy0_copy0 (filter), FORMULA1_copy0_copy0_copy0_copy0 (formula), APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema) +3 more |
| `Coverage_5G_P__c` | APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `FAR_ID__c` | FORMULA14_copy0_copy0_copy0_copy0 (formula), APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) +1 more |
| `Fiber_cost__c` | FILTER13_copy0_copy0_copy0_copy0_copy0 (filter), FORMULA0_copy1_copy0_copy0_copy0 (formula), FORMULA17_copy0_copy0_copy0_copy0 (formula), FORMULA1_copy0_copy0_copy0_copy0 (formula), APPEND2_copy1 (appendV2) +5 more |
| `Id` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `IsDeleted` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `LFA_IS_ONNET__c` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `Location_Owner__c` | AGGREGATE9_copy0_copy0_copy0_copy0 (aggregate), DROP_FIELDS3_copy0_copy0_copy0_copy0 (schema), FORMULA25_copy0 (computeRelative), AGGREGATE23 (aggregate), FORMULA28_copy0 (computeRelative) +34 more |
| `Name` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `OwnerId` | APPEND2_copy1 (appendV2), DROP_FIELDS13_copy0 (schema), DROP_FIELDS14_copy0 (schema) |
| `Postal_address__c` | APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy0 (formula), DROP_FIELDS14_copy0 (schema) +1 more |
| `Street_address__c` | FILTER33_copy0_copy0 (filter), APPEND2_copy1 (appendV2), DROP_FIELDS15_copy0 (schema), DROP_FIELDS13_copy0 (schema), FORMULA16_copy0_copy0_copy0_copy0 (formula) +1 more |

### BSS_Event__c (`LOAD_DATASET1_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 27
- **Fields used:** 7
- **Fields unused:** 20

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Event_type__c` | FILTER2_copy0_copy0 (filter) |
| `Id` | FORMULA39_copy1 (formula), FORMULA40_copy1 (formula) |
| `Parameter_1_Value__c` | JOIN20 (join), AGGREGATE1_copy1 (aggregate), AGGREGATE3_copy3 (aggregate), FORMULA37_copy1 (formula), FORMULA35_copy1 (formula) |
| `Parameter_2_Value__c` | AGGREGATE1_copy1 (aggregate), AGGREGATE3_copy3 (aggregate) |
| `Parameter_3_Value__c` | FORMULA0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula) |
| `Parameter_4_Value__c` | FORMULA10_copy0_copy0_copy0 (formula) |
| `Parameter_8_Value__c` | FILTER5_copy0 (filter) |

#### Fields to ELIMINATE

- `Account__c`
- `CreatedById`
- `CreatedDate`
- `Event_Id__c`
- `LastModifiedById`
- `LastModifiedDate`
- `Name`
- `OwnerId`
- `Parameter_1_Name__c`
- `Parameter_2_Name__c`
- `Parameter_3_Name__c`
- `Parameter_4_Name__c`
- `Parameter_5_Name__c`
- `Parameter_5_Value__c`
- `Parameter_6_Name__c`
- `Parameter_6_Value__c`
- `Parameter_7_Name__c`
- `Parameter_7_Value__c`
- `Parameter_8_Name__c`
- `SystemModstamp`

### Blacklist main (`LOAD_DATASET0_copy0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 6
- **Fields used:** 6
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Blacklist_Date` | APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |
| `Blacklist_Fixed` | JOIN2_copy1 (join), APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |
| `Blacklist_Id` | APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |
| `Blacklist_Kurtid` | JOIN0_copy0 (join), APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |
| `Blacklist_Mobile` | JOIN1_copy1 (join), JOIN3_copy1 (join), APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |
| `Blacklist_Name` | APPEND0_copy1 (appendV2), APPEND1_copy1 (appendV2) |

### C360_eDM_Master (`LOAD_DATASET10`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 6
- **Fields used:** 5
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountID` | JOIN23 (join), DROP_FIELDS34 (schema), DROP_FIELDS35 (schema) |
| `CampaignCD` | FILTER44 (filter) |
| `ContactID` | DROP_FIELDS34 (schema), DROP_FIELDS35 (schema) |
| `Personalization_2__c` | TO_MEASURE3 (typeCast) |
| `Send_timestamp` | FILTER45 (filter) |

#### Fields to ELIMINATE

- `CampaignName`

### Case (`LOAD_DATASET3`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 10
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA4_copy0_copy0 (formula), FORMULA6 (formula), FORMULA6_copy0 (formula), FORMULA6_copy0_copy0 (formula), FORMULA6_copy1 (formula) +1 more |
| `ClosedDate` | FILTER14 (filter), FILTER15 (filter), FILTER15_copy0_copy0 (filter), APPEND2 (appendV2) |
| `CreatedDate` | APPEND2 (appendV2) |
| `Id` | APPEND2 (appendV2) |
| `LastModifiedDate` | FILTER15_copy1 (filter), APPEND2 (appendV2) |
| `Onboarding_Type__c` | FILTER14 (filter), APPEND2 (appendV2) |
| `Product_Category__c` | FILTER14 (filter), FILTER15 (filter), FILTER15_copy0 (filter), FILTER15_copy0_copy0 (filter), FILTER15_copy1 (filter) +1 more |
| `RecordTypeId` | FILTER14 (filter), APPEND2 (appendV2) |
| `Status` | FILTER11 (filter), FORMULA5 (formula), FILTER15 (filter), FILTER15_copy0 (filter), FILTER15_copy0_copy0 (filter) +2 more |
| `Type` | FILTER11 (filter), FILTER15 (filter), FILTER15_copy0 (filter), FILTER15_copy0_copy0 (filter), FILTER15_copy1 (filter) +1 more |

### Contact (`LOAD_DATASET6`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 50
- **Fields used:** 14
- **Fields unused:** 36

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | JOIN17 (join), DROP_FIELDS13 (schema), DROP_FIELDS17 (schema), DROP_FIELDS17_copy0 (schema), DROP_FIELDS13_copy1 (schema) +18 more |
| `Email` | DROP_FIELDS13 (schema), DROP_FIELDS17 (schema), DROP_FIELDS17_copy0 (schema), DROP_FIELDS13_copy1 (schema), DROP_FIELDS17_copy2 (schema) +1 more |
| `HasOptedOutOfEmail` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER32_copy0_copy0 (filter) |
| `Has_eMail__c` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER32_copy0_copy0 (filter), FILTER32_copy1 (filter), FILTER32_copy0_copy1 (filter) +1 more |
| `Id` | DROP_FIELDS13 (schema), DROP_FIELDS17 (schema), DROP_FIELDS17_copy0 (schema), DROP_FIELDS13_copy1 (schema), DROP_FIELDS17_copy2 (schema) +9 more |
| `IsDeleted` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER0_copy0 (filter), FILTER32_copy0_copy0 (filter), FILTER32_copy1 (filter) +2 more |
| `Key_contact__c` | FILTER32_copy0 (filter), FILTER32_copy0_copy1 (filter) |
| `MBSuperadmin__c` | FILTER32_copy0_copy0 (filter), FILTER32_copy0_copy0_copy0 (filter) |
| `MB_Admin__c` | FILTER32_copy0_copy0 (filter), FILTER32_copy0_copy0_copy0 (filter) |
| `Marketing_Cloud_Contact2__c` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER32_copy0_copy0 (filter), FILTER32_copy1 (filter), FILTER32_copy0_copy1 (filter) +1 more |
| `Marketing_Cloud_Email_Bounced__c` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER32_copy0_copy0 (filter), FILTER32_copy1 (filter), FILTER32_copy0_copy1 (filter) +1 more |
| `MobilePhone` | DROP_FIELDS13 (schema), DROP_FIELDS17 (schema), FORMULA0_copy0 (formula), DROP_FIELDS17_copy0 (schema), DROP_FIELDS13_copy1 (schema) +2 more |
| `Primary__c` | FILTER32 (filter), FILTER0_copy0 (filter), FILTER32_copy1 (filter) |
| `StatusKURT__c` | FILTER32 (filter), FILTER32_copy0 (filter), FILTER32_copy0_copy0 (filter), FILTER32_copy1 (filter), FILTER32_copy0_copy1 (filter) +1 more |

#### Fields to ELIMINATE

- `AccountId__c`
- `Account_KURT_Id__c`
- `Account_Market_Name__c`
- `Average_Rating__c`
- `Birthdate`
- `Business_Area__c`
- `Business_Customer_Contact__c`
- `Business_Customer_Primary_Contact__c`
- `Consent_status__c`
- `ContactID__c`
- `CreatedDate`
- `Data_Quality_Email_Mob__c`
- `Event__c`
- `EvergageFilters__c`
- `FirstName`
- `Has_Norwegian_Mobile__c`
- `IoT__c`
- `IsPersonAccount`
- `KTIFTI__c`
- `KurtID__c`
- `LastName`
- `Legal_Notification_Contact__c`
- `Legal_Owner__c`
- `Legal_Role_Phone__c`
- `Legal_Role__c`
- `Name`
- `Nettverksteknologi__c`
- `Non_Marketable_Contact__c`
- `Nyheter_fra_Telenor_Bedrift__c`
- `RecordTypeId`
- `Role_Level__c`
- `Role__c`
- `Sikkerhet__c`
- `Title`
- `Top_Level_Kurt_ID__c`
- `et4ae5__HasOptedOutOfMobile__c`

### Fiber nysalg Region postnummer (`LOAD_DATASET8`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 5
- **Fields used:** 1
- **Fields unused:** 4

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Postnummer` | AGGREGATE31 (aggregate), JOIN19 (join) |

#### Fields to ELIMINATE

- `Bruksomr_de`
- `Bydel`
- `Koordinatar`
- `Omr_de`

### Opportunity (`LOAD_DATASET2_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 15
- **Fields used:** 14
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA4_copy0_copy1 (formula), FORMULA49 (formula), AGGREGATE27 (aggregate), FORMULA50 (formula), FORMULA4 (formula) +5 more |
| `All_Product_Categories__c` | FORMULA2 (formula) |
| `CloseDate` | FILTER39 (filter), FILTER10_copy0 (filter), FILTER10_copy0_copy0 (filter) |
| `CreatedDate` | FILTER16 (filter), FILTER34 (filter) |
| `Created_By_Role__c` | FILTER16 (filter) |
| `Id` | JOIN16 (join) |
| `LastModifiedDate` | FILTER39 (filter), FILTER3_copy0 (filter), FILTER10_copy0 (filter), FILTER10_copy0_copy0_copy0_copy0 (filter), FILTER10_copy0_copy0 (filter) +1 more |
| `Lead_Scoring__c` | FILTER16 (filter), FILTER34 (filter) |
| `Opportunity_Source__c` | FILTER16 (filter) |
| `Owner_Role__c` | FILTER1_copy0 (filter) |
| `Product_Category__c` | FILTER0_copy1 (filter), FILTER39 (filter) |
| `RecordTypeId` | FILTER16 (filter) |
| `StageName` | FILTER2_copy0 (filter), FILTER39 (filter), FILTER10_copy0 (filter), FILTER10_copy0_copy0_copy0_copy0 (filter), FILTER10_copy0_copy0 (filter) +1 more |
| `WonLostReason__c` | FORMULA0 (formula) |

#### Fields to ELIMINATE

- `Type`

### Subscription__c (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 18
- **Fields used:** 10
- **Fields unused:** 8

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DRM_MARKET_PRODUCT_GROUP__c` | FILTER20 (filter), FORMULA8 (formula) |
| `IsDeleted` | FILTER20 (filter) |
| `MBN_ACTIVE_USER_ACT_DT__c` | FORMULA18 (formula) |
| `Market_area__c` | FILTER31 (filter) |
| `Product_Name__c` | FORMULA27 (formula), FORMULA56 (formula), FORMULA56_copy0 (formula), FORMULA9_copy1 (formula), FORMULA61 (formula) |
| `SUBSCRIPTION_BINDINGREMDAY__c` | FORMULA7 (formula), FORMULA7_copy0 (formula), FORMULA69 (formula) |
| `SafeZone_Product_Name__c` | FORMULA39_copy2 (formula), FORMULA40_copy2 (formula), FORMULA57 (formula) |
| `Stealth_campaign__c` | FORMULA71 (formula) |
| `Sub_Owner__c` | AGGREGATE15 (aggregate), JOIN23 (join), FORMULA68 (formula) |
| `Sub_User__c` | AGGREGATE19 (aggregate) |

#### Fields to ELIMINATE

- `FarId__c`
- `MV_PORTOUT_ORDER_DATE__c`
- `Main_number__c`
- `NUMBER_OF_HOURS_TO_PORT__c`
- `OPPDATERT__c`
- `PORT_DATE_KEY__c`
- `Product_Category__c`
- `Sub_Payer__c`

### Suppressions - Low Priority NACE-Codes - TM New Sales MV (`LOAD_DATASET12`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 1
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `NACE` | JOIN24 (join) |

#### Fields to ELIMINATE

- `ACTIVITY`
