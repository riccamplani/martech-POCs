# C360_496_-_Pilot_SafeZone_og_Oppdatert_bundle__05vJ7000000wm1mIAA — Field Usage Report

**Recipe:** C360_496_-_Pilot_SafeZone_og_Oppdatert_bundle__05vJ7000000wm1mIAA
**Total nodes:** 729

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET14_copy0 | Account | connectedDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET0_copy0_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET1_copy0 | Account | connectedDataset | 11 | 11 | 0 | 0% |
| LOAD_DATASET0_copy0_copy0_copy0 | Account | connectedDataset | 5 | 5 | 0 | 0% |
| LOAD_DATASET0_copy0_copy0_copy1 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1_copy0_copy0 | Account | connectedDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1_copy0_copy0_copy0 | Account | connectedDataset | 6 | 6 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1 | Account | connectedDataset | 26 | 26 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET0_copy0_copy2 | Account | connectedDataset | 21 | 21 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0 | Account | connectedDataset | 12 | 12 | 0 | 0% |
| LOAD_DATASET0_copy0_copy0_copy1_copy0_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1_copy0_copy0_copy1 | Account | connectedDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET0_copy1_copy0 | Account | connectedDataset | 26 | 26 | 0 | 0% |
| LOAD_DATASET0_copy0_copy3 | Account | connectedDataset | 26 | 26 | 0 | 0% |
| LOAD_DATASET14_copy0_copy1 | Account | connectedDataset | 12 | 12 | 0 | 0% |
| LOAD_DATASET0_copy1_copy1 | Account | connectedDataset | 26 | 26 | 0 | 0% |
| LOAD_DATASET0_copy0_copy4 | Account | connectedDataset | 28 | 28 | 0 | 0% |
| LOAD_DATASET14_copy0_copy2 | Account | connectedDataset | 12 | 12 | 0 | 0% |
| LOAD_DATASET0_copy1_copy2 | Account | connectedDataset | 26 | 26 | 0 | 0% |
| LOAD_DATASET5_copy0 | Account | connectedDataset | 5 | 5 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0 | Account | connectedDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET0_copy0_copy5 | Account | connectedDataset | 23 | 23 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| LOAD_DATASET5_copy1 | Account | connectedDataset | 6 | 6 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0_copy0_copy1 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| LOAD_DATASET2_copy0_copy1 | Contact | connectedDataset | 10 | 10 | 0 | 0% |
| **TOTAL** | | | **320** | **320** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23_copy0_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula) +15 more |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula) +5 more |
| `Migration_flag__c` | FORMULA19_copy0_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0_copy0_copy0 (formula), DROP_FIELDS11_copy0_copy0_copy0_copy0_copy0_copy0 (schema), DROP_FIELDS11_copy0_copy0 (schema), DROP_FIELDS11_copy0_copy0_copy0 (schema) +7 more |

### Account (`LOAD_DATASET0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN21 (join), JOIN23 (join), DROP_FIELDS23 (schema), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy1_copy0_copy0_copy2_copy0_copy0_copy0_copy0 (schema), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy1_copy0_copy0_copy2_copy0_copy0_copy0 (schema) +12 more |
| `Reservation_Date_MV_Outbound__c` | FILTER34_copy0_copy0 (filter), FILTER34_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET1_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 11
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | DROP_FIELDS0_copy0 (schema), FILTER8_copy0_copy0 (filter) |
| `CustomerType__c` | DROP_FIELDS0_copy0 (schema), FILTER7_copy0_copy0 (filter) |
| `Forbund_membership__c` | DROP_FIELDS0_copy0 (schema), FILTER13_copy0 (filter) |
| `Id` | JOIN0_copy1 (join), DROP_FIELDS0_copy0 (schema), JOIN1_copy1 (join), DROP_FIELDS12_copy1_copy0_copy0_copy0 (schema), JOIN2_copy0 (join) |
| `NumberOfEmployees` | DROP_FIELDS0_copy0 (schema), FILTER15_copy0 (filter) |
| `Phonenumber_type__c` | DROP_FIELDS0_copy0 (schema), FILTER8_copy0_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | DROP_FIELDS0_copy0 (schema), FILTER34_copy0_copy0_copy0_copy0 (filter) |
| `TAG_TALKMORE_BEDRIFT__c` | DROP_FIELDS0_copy0 (schema), FILTER5_copy0_copy1 (filter) |
| `TAG_TALKMORE_PRIVATE__c` | DROP_FIELDS0_copy0 (schema), FILTER5_copy0_copy1 (filter) |
| `TSP_Dealer__c` | DROP_FIELDS0_copy0 (schema), FILTER14_copy0 (filter) |
| `mobile_service_segment__c` | DROP_FIELDS0_copy0 (schema), FILTER12_copy0 (filter) |

### Account (`LOAD_DATASET0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 5
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Has_Subscriptions__c` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy1_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy1_copy0_copy0 (formula), JOIN2_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy1_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy1_copy0_copy0 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) |

### Account (`LOAD_DATASET0_copy0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0_copy0_copy0_copy1_copy0_copy1 (formula), FORMULA10_copy0_copy0_copy0_copy1_copy0_copy1 (formula), JOIN1_copy0_copy0_copy0 (join), JOIN2_copy2_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy1_copy0_copy1 (formula), FORMULA11_copy0_copy0_copy0_copy1_copy0_copy1 (formula) |

### Account (`LOAD_DATASET0_copy0_copy1_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FILTER64_copy0_copy0_copy0 (filter), APPEND0_copy1_copy0_copy0 (appendV2), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy1_copy0_copy0_copy2_copy0_copy0_copy1_copy0_copy0 (schema), JOIN1_copy0_copy0_copy0 (join), JOIN2_copy2_copy0_copy0 (join) |

### Account (`LOAD_DATASET0_copy0_copy1_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 6
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN3_copy1 (join), DROP_FIELDS14_copy0 (schema), JOIN4_copy0 (join), JOIN5_copy0 (join), DROP_FIELDS15_copy0 (schema) +5 more |
| `IsDeleted` | FILTER72_copy0 (filter) |
| `NBR_OPPDATERT__c` | DROP_FIELDS14_copy0 (schema), FILTER79_copy0 (filter) |
| `StatusKURT__c` | FILTER72_copy0 (filter) |
| `TSP_Dealer__c` | DROP_FIELDS14_copy0 (schema), FILTER75_copy0 (filter) |
| `mobile_service_segment__c` | DROP_FIELDS14_copy0 (schema), FILTER74_copy0 (filter) |

### Account (`LOAD_DATASET0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 26
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Company_Family_Name__c` | FILTER110 (filter) |
| `Forbund_membership__c` | FILTER108 (filter) |
| `Id` | JOIN0_copy0_copy0 (join), JOIN29_copy0 (join), JOIN27_copy0 (join), JOIN28_copy0 (join), JOIN11_copy0_copy0 (join) +12 more |
| `Industry__c` |  |
| `IsDeleted` | FILTER1_copy0_copy0_copy0 (filter) |
| `KurtID__c` |  |
| `MBN_PROD_KO_ACT_DATE__c` |  |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` |  |
| `MPORT_FLG__c` |  |
| `Migration_flag__c` |  |
| `Mobile_Voice_Penetration__c` | FILTER3_copy0_copy0_copy0_copy0_copy0_copy0 (filter) |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` |  |
| `NBR_MBN_SENTRALBORD__c` |  |
| `NBR_MBN__c` |  |
| `NBR_OPPDATERT__c` | FILTER67_copy0 (filter) |
| `Name` |  |
| `NumberOfEmployees` |  |
| `OrgNo__c` |  |
| `Reservation_Date_MV_Outbound__c` | FILTER34_copy0_copy0_copy0_copy1 (filter), FILTER34_copy0_copy0_copy0_copy0_copy0 (filter) |
| `SUM_POTENTIAL__c` |  |
| `Segment__c` |  |
| `Service_segment__c` |  |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0 (filter) |
| `TM_Forbund_Flag__c` |  |
| `TSP_Dealer__c` | FILTER63_copy0_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET14_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0_copy0_copy0_copy1 (formula), FORMULA10_copy0_copy0_copy0_copy1 (formula), JOIN26_copy0 (join), FILTER103 (filter) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy1 (formula), FORMULA11_copy0_copy0_copy0_copy1 (formula) |

### Account (`LOAD_DATASET0_copy0_copy2`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | DROP_FIELDS0_copy1 (schema), FILTER8_copy0_copy0_copy0 (filter), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `CustomerType__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Forbund_membership__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), FILTER93 (filter), FILTER94 (filter) +1 more |
| `Has_Subscriptions_Actual__c` | DROP_FIELDS0_copy1 (schema), FILTER14_copy0_copy0 (filter), FILTER15_copy0_copy0 (filter), APPEND0_copy1 (appendV2), APPEND8 (appendV2) +1 more |
| `Has_Subscriptions__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Id` | JOIN0_copy0 (join), DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) +5 more |
| `IsDeleted` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `KurtID__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), JOIN34 (join), APPEND8 (appendV2), APPEND63 (appendV2) |
| `NACE_Subclass_Description__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `NBR_VOICE_PAYER__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Name` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `NumberOfEmployees` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), FILTER21_copy0_copy0 (filter), FILTER21_copy0_copy0_copy0 (filter), APPEND8 (appendV2) +1 more |
| `Phonenumber_type__c` | DROP_FIELDS0_copy1 (schema), FILTER8_copy0_copy0_copy0 (filter), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Portfolio__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), FILTER9_copy0_copy0 (filter), APPEND8 (appendV2), APPEND63 (appendV2) |
| `Segment__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `StatusKURT__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `SubsMobileVoice__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `TAG_TALKMORE_BEDRIFT__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), APPEND8 (appendV2), APPEND63 (appendV2) |
| `mobile_service_segment__c` | DROP_FIELDS0_copy1 (schema), APPEND0_copy1 (appendV2), FILTER17_copy0_copy0 (filter), FILTER17_copy0_copy0_copy0 (filter), APPEND8 (appendV2) +1 more |

### Account (`LOAD_DATASET14_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 12
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` |  |
| `Forbund_membership__c` | FORMULA19_copy0_copy1 (formula) |
| `Has_Subscriptions__c` |  |
| `Id` | FORMULA9_copy0_copy1 (formula), FORMULA10_copy0_copy1 (formula), JOIN16_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy1 (formula), FORMULA11_copy0_copy1 (formula) |
| `MBN_PROD_HOVEDNUMMER_ACT_DATE__c` |  |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `NumberOfEmployees` |  |
| `SubsM2M__c` |  |

### Account (`LOAD_DATASET0_copy0_copy0_copy1_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0_copy0_copy0_copy1_copy0_copy1_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy1_copy0_copy1_copy0_copy0 (formula), JOIN1_copy0_copy0_copy0_copy0_copy0 (join), JOIN2_copy2_copy0_copy0_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy1_copy0_copy1_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy1_copy0_copy1_copy0_copy0 (formula) |

### Account (`LOAD_DATASET0_copy0_copy1_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | DROP_FIELDS14_copy0_copy0_copy0 (schema), FILTER87_copy0 (filter) |
| `Id` | JOIN3_copy1_copy0_copy0 (join), DROP_FIELDS14_copy0_copy0_copy0 (schema), JOIN4_copy0_copy0_copy0 (join), JOIN5_copy0_copy0_copy0 (join), DROP_FIELDS15_copy0_copy0_copy0 (schema) +5 more |
| `IsDeleted` | FILTER72_copy0_copy0_copy0 (filter) |
| `NBR_OPPDATERT__c` | DROP_FIELDS14_copy0_copy0_copy0 (schema), FILTER79_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER72_copy0_copy0_copy0 (filter) |
| `TSP_Dealer__c` | DROP_FIELDS14_copy0_copy0_copy0 (schema), FILTER75_copy0_copy0_copy0 (filter) |
| `mobile_service_segment__c` | DROP_FIELDS14_copy0_copy0_copy0 (schema), FILTER74_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET0_copy0_copy1_copy0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FILTER64_copy0_copy0_copy0_copy1 (filter), APPEND0_copy2 (appendV2), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy1_copy0_copy0_copy2_copy0_copy0_copy1_copy0_copy0_copy0_copy0 (schema), JOIN1_copy0_copy0_copy0_copy0_copy0 (join), JOIN2_copy2_copy0_copy0_copy0_copy0 (join) |

### Account (`LOAD_DATASET0_copy1_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 26
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_QUALITYMARK_PHONE__c` |  |
| `COM_CUSTOMER_TM_RESERVATION__c` |  |
| `CompanyFamily__c` |  |
| `CustomerType__c` |  |
| `Economic_Attractivity__c` |  |
| `External_Credit_Rating__c` |  |
| `Has_Subscriptions_Actual__c` |  |
| `Has_Subscriptions__c` |  |
| `Id` | DROP_FIELDS30 (schema), APPEND71 (appendV2), FORMULA45 (computeRelative), FORMULA41 (formula), JOIN31 (join) +7 more |
| `IsDeleted` |  |
| `NACE_Subclass_Code__c` |  |
| `NACE_Subclass_Description__c` |  |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `Name` |  |
| `NumberOfEmployees` |  |
| `Phonenumber_type__c` | FILTER3_copy0_copy0 (filter) |
| `Portfolio__c` |  |
| `Reservation_Date_IA_Inbound__c` |  |
| `Reservation_Date_IA_Outbound__c` |  |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` |  |
| `StatusKURT__c` |  |
| `VisitingCounty__c` |  |

### Account (`LOAD_DATASET0_copy0_copy3`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 26
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `COM_CUSTOMER_PHONENBR_STATUS__c` | FILTER8_copy0_copy1 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Company_Family_Name__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER17_copy0_copy1 (filter), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `CustomerType__c` | FILTER7_copy0_copy1 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Forbund_membership__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Has_Subscriptions_Actual__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Has_Subscriptions__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Id` | JOIN1_copy0_copy0 (join), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER41_copy0 (filter), DROP_FIELDS2_copy0_copy0 (schema) +10 more |
| `IsDeleted` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `KurtID__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `Mobile_Segment__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER37_copy0 (filter), FILTER38_copy0 (filter), APPEND58_copy0 (appendV2) +1 more |
| `NACE_Subclass_Description__c` | FILTER6_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `NBR_VOICE_PAYER__c` | FILTER4_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Name` | FILTER6_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `NumberOfEmployees` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER21_copy0_copy1 (filter), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `OrgNo__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `Phonenumber_type__c` | FILTER8_copy0_copy1 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Portfolio__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER9_copy0_copy1 (filter), APPEND58_copy0 (appendV2) |
| `Segment__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `StatusKURT__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `SubsMobileVoice__c` | FILTER4_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `TAG_TALKMORE_BEDRIFT__c` | FILTER5_copy1_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | FILTER5_copy1_copy0 (filter), APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2) |
| `TSP_Dealer__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), FILTER39_copy0 (filter), APPEND58_copy0 (appendV2) |
| `mobile_service_segment__c` | APPEND2_copy1_copy0 (appendV2), APPEND1_copy0_copy0 (appendV2), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |

### Account (`LOAD_DATASET14_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 12
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` |  |
| `Forbund_membership__c` |  |
| `Has_Subscriptions__c` |  |
| `Id` | FORMULA9_copy0_copy2 (formula), FORMULA10_copy0_copy2 (formula), JOIN16_copy1 (join), JOIN32 (join), APPEND62 (appendV2) |
| `KurtID__c` | FORMULA8_copy0_copy2 (formula), FORMULA11_copy0_copy2 (formula) |
| `MBN_PROD_HOVEDNUMMER_ACT_DATE__c` |  |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `NumberOfEmployees` |  |
| `SubsM2M__c` |  |

### Account (`LOAD_DATASET0_copy1_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 26
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_QUALITYMARK_PHONE__c` |  |
| `COM_CUSTOMER_TM_RESERVATION__c` |  |
| `CompanyFamily__c` |  |
| `CustomerType__c` | APPEND58_copy0 (appendV2) |
| `Economic_Attractivity__c` |  |
| `External_Credit_Rating__c` |  |
| `Has_Subscriptions_Actual__c` | APPEND58_copy0 (appendV2) |
| `Has_Subscriptions__c` | APPEND58_copy0 (appendV2) |
| `Id` | DROP_FIELDS4_copy0_copy0 (schema), DROP_FIELDS5_copy0_copy0 (schema), DROP_FIELDS11_copy1_copy0 (schema), APPEND0_copy0_copy0 (appendV2), APPEND5_copy0_copy0 (appendV2) +15 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy1 (filter), APPEND58_copy0 (appendV2) |
| `NACE_Subclass_Code__c` |  |
| `NACE_Subclass_Description__c` | APPEND58_copy0 (appendV2) |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `Name` | APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `NumberOfEmployees` | FILTER21_copy0_copy1 (filter), APPEND58_copy0 (appendV2), DROP_FIELDS16_copy0 (schema) |
| `Phonenumber_type__c` | FILTER3_copy0_copy1 (filter), APPEND58_copy0 (appendV2) |
| `Portfolio__c` | APPEND58_copy0 (appendV2) |
| `Reservation_Date_IA_Inbound__c` |  |
| `Reservation_Date_IA_Outbound__c` |  |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` | FILTER9_copy0_copy1 (filter), APPEND58_copy0 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0_copy0 (filter), APPEND58_copy0 (appendV2) |
| `VisitingCounty__c` |  |

### Account (`LOAD_DATASET0_copy0_copy4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 28
- **Fields used:** 28
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `COM_CUSTOMER_PHONENBR_STATUS__c` | FILTER8_copy0_copy2 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), FILTER8_copy0_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `Company_Family_Name__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `CustomerType__c` | FILTER7_copy0_copy2 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Economic_Attractivity__c` | FILTER43_copy0 (filter) |
| `External_Credit_Rating__c` | FILTER0_copy0_copy0 (filter) |
| `Forbund_membership__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Has_Subscriptions_Actual__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), FILTER14_copy0_copy1 (filter), FILTER15_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `Has_Subscriptions__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Id` | JOIN1_copy0_copy1 (join), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), FILTER41_copy1 (filter), DROP_FIELDS2_copy0_copy1 (schema) +10 more |
| `IsDeleted` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `KurtID__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Mobile_Segment__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `NACE_Subclass_Description__c` | FILTER6_copy0_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `NBR_VOICE_PAYER__c` | FILTER4_copy0_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Name` | FILTER6_copy0_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `NumberOfEmployees` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2), FILTER21_copy0_copy2 (filter) |
| `OrgNo__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Phonenumber_type__c` | FILTER8_copy0_copy2 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), FILTER8_copy0_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `Portfolio__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `Reservation_Date_MV_Outbound__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2), FILTER9_copy0_copy2 (filter) |
| `Segment__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `StatusKURT__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `SubsMobileVoice__c` | FILTER4_copy0_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `TAG_TALKMORE_BEDRIFT__c` | FILTER5_copy1_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `TAG_TALKMORE_PRIVATE__c` | FILTER5_copy1_copy1 (filter), APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `TSP_Dealer__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2) |
| `mobile_service_segment__c` | APPEND2_copy1_copy1 (appendV2), APPEND1_copy0_copy1 (appendV2), APPEND61_copy0 (appendV2), FILTER42_copy0 (filter) |

### Account (`LOAD_DATASET14_copy0_copy2`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 12
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` |  |
| `Forbund_membership__c` |  |
| `Has_Subscriptions__c` |  |
| `Id` | FORMULA9_copy0_copy3 (formula), FORMULA10_copy0_copy3 (formula), JOIN16_copy2 (join) |
| `KurtID__c` | FORMULA8_copy0_copy3 (formula), FORMULA11_copy0_copy3 (formula) |
| `MBN_PROD_HOVEDNUMMER_ACT_DATE__c` |  |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `NumberOfEmployees` |  |
| `SubsM2M__c` |  |

### Account (`LOAD_DATASET0_copy1_copy2`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 26
- **Fields used:** 26
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_QUALITYMARK_PHONE__c` |  |
| `COM_CUSTOMER_TM_RESERVATION__c` |  |
| `CompanyFamily__c` |  |
| `CustomerType__c` | APPEND61_copy0 (appendV2) |
| `Economic_Attractivity__c` | FILTER43_copy0 (filter) |
| `External_Credit_Rating__c` | FILTER0_copy0_copy0 (filter) |
| `Has_Subscriptions_Actual__c` | FILTER14_copy0_copy1 (filter), FILTER15_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `Has_Subscriptions__c` | APPEND61_copy0 (appendV2) |
| `Id` | DROP_FIELDS4_copy0_copy1 (schema), DROP_FIELDS5_copy0_copy1 (schema), DROP_FIELDS11_copy1_copy1 (schema), DROP_FIELDS6_copy0_copy0 (schema), APPEND0_copy0_copy1 (appendV2) +17 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy2 (filter), APPEND61_copy0 (appendV2) |
| `NACE_Subclass_Code__c` |  |
| `NACE_Subclass_Description__c` | APPEND61_copy0 (appendV2) |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `Name` | APPEND61_copy0 (appendV2) |
| `NumberOfEmployees` | APPEND61_copy0 (appendV2), FILTER21_copy0_copy2 (filter) |
| `Phonenumber_type__c` | FILTER3_copy0_copy2 (filter), FILTER8_copy0_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `Portfolio__c` | FILTER7_copy1_copy0 (filter), APPEND61_copy0 (appendV2) |
| `Reservation_Date_IA_Inbound__c` |  |
| `Reservation_Date_IA_Outbound__c` |  |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` | APPEND61_copy0 (appendV2), FILTER9_copy0_copy2 (filter) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0_copy1 (filter), APPEND61_copy0 (appendV2) |
| `VisitingCounty__c` |  |

### Account (`LOAD_DATASET5_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 5
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA42_copy0 (formula), JOIN31_copy0 (join), DROP_FIELDS12_copy0_copy0_copy1_copy0_copy0_copy1_copy0_copy0_copy2_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (schema), JOIN26_copy0_copy0 (join) |
| `IsDeleted` | FILTER1_copy0_copy0_copy0_copy2 (filter) |
| `Name` |  |
| `OrgNo__c` | JOIN30_copy0 (join) |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0_copy2 (filter) |

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN29_copy1 (join), FORMULA9_copy0_copy0_copy0_copy0_copy1 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy1 (formula), JOIN26_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy1 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy1 (formula) |
| `OrgNo__c` | JOIN28_copy1 (join) |
| `SubsMobileVoice__c` | FORMULA19_copy0_copy0_copy0_copy0_copy1 (formula) |

### Account (`LOAD_DATASET0_copy0_copy5`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 23
- **Fields used:** 23
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` |  |
| `COM_CUSTOMER_EDM_RESERVATION__c` |  |
| `CompanyFamily__c` |  |
| `Company_Family_Name__c` |  |
| `Concern__c` |  |
| `Forbund_membership__c` |  |
| `Has_Min_Bedrift__c` |  |
| `Id` | JOIN1_copy0 (join), FORMULA1_copy1 (computeRelative), JOIN33 (join), FILTER100 (filter), JOIN35 (join) +2 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy3 (filter) |
| `KurtID__c` |  |
| `Last_Min_Bedrift_Web_Login__c` |  |
| `MV_FIRST_SALE_DT__c` |  |
| `NBR_OPPDATERT__c` |  |
| `NBR_SAFEZONE_MOBILE__c` |  |
| `NBR_SOURCE_ACCOUNT_ID_MOBIL__c` |  |
| `Name` |  |
| `PersonHasOptedOutOfEmail` |  |
| `Phonenumber_type__c` | FILTER15_copy0_copy2 (filter) |
| `SOURCE_ACCOUNT_ID_MOBIL__c` |  |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy3 (filter) |
| `SubsMobileVoice__c` |  |
| `TSP_Dealer__c` |  |
| `mobile_service_segment__c` |  |

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` |  |
| `Forbund_membership__c` |  |
| `Has_Subscriptions_Actual__c` |  |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy0_copy1 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy1 (formula), JOIN26_copy0_copy0_copy0 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy1 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy1 (formula) |
| `NumberOfEmployees` |  |
| `OrgNo__c` |  |

### Account (`LOAD_DATASET5_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 6
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA42_copy1 (formula), JOIN31_copy1 (join), JOIN32_copy0 (join), JOIN36 (join), FORMULA5_copy0_copy1 (computeRelative) +6 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy0_copy3 (filter) |
| `KurtID__c` | JOIN30_copy1 (join) |
| `Name` |  |
| `OrgNo__c` |  |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0_copy3 (filter) |

### Account (`LOAD_DATASET14_copy0_copy0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` | FORMULA19_copy0_copy0_copy0_copy0_copy2 (formula) |
| `Forbund_membership__c` | FORMULA19_copy0_copy0_copy0_copy0_copy2 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA19_copy0_copy0_copy0_copy0_copy2 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0_copy2 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy2 (formula), JOIN26_copy0_copy1 (join) |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy2 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy2 (formula) |
| `NumberOfEmployees` | FORMULA19_copy0_copy0_copy0_copy0_copy2 (formula) |
| `OrgNo__c` |  |

### Contact (`LOAD_DATASET2_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 10
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | DROP_FIELDS0_copy2 (schema), FORMULA0_copy0 (formula) |
| `AccountId__c` |  |
| `Id` | DROP_FIELDS0_copy2 (schema), JOIN0_copy2 (join), JOIN1_copy0 (join), FORMULA1_copy1 (computeRelative), JOIN33 (join) +4 more |
| `IsDeleted` |  |
| `Key_contact__c` |  |
| `MBSuperadmin__c` |  |
| `MB_Admin__c` |  |
| `Name` |  |
| `Primary__c` |  |
| `StatusKURT__c` |  |
