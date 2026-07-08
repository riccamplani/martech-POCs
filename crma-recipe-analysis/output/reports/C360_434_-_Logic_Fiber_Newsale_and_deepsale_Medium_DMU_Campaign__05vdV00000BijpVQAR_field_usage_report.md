# C360_434_-_Logic_Fiber_Newsale_and_deepsale_Medium_DMU_Campaign__05vdV00000BijpVQAR — Field Usage Report

**Recipe:** C360_434_-_Logic_Fiber_Newsale_and_deepsale_Medium_DMU_Campaign__05vdV00000BijpVQAR
**Total nodes:** 228

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 25 | 14 | 11 | 44% |
| LOAD_DATASET5_copy0_copy0_copy0 | Account_Location__c | connectedDataset | 21 | 21 | 0 | 0% |
| **TOTAL** | | | **46** | **35** | **11** | **24%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 25
- **Fields used:** 14
- **Fields unused:** 11

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DPSS_DMU__c` | FORMULA47 (formula), DROP_FIELDS18 (schema) |
| `DPSS_Segment__c` | FILTER9 (filter), DROP_FIELDS18 (schema) |
| `Has_Subscriptions_Actual__c` | FORMULA0_copy0 (formula), DROP_FIELDS18 (schema) |
| `Id` | DROP_FIELDS21 (schema), FORMULA47 (formula), JOIN19 (join), JOIN0 (join), JOIN3 (join) +22 more |
| `Industry__c` | FORMULA87 (formula), DROP_FIELDS18 (schema), FORMULA97 (formula), DROP_FIELDS8_copy0_copy0 (schema) |
| `Is_DMU__c` | FORMULA47 (formula), DROP_FIELDS18 (schema), FILTER39 (filter), FORMULA57 (formula), FORMULA60 (formula) |
| `KurtID__c` | DROP_FIELDS18 (schema), FORMULA23_copy0_copy0 (formula) |
| `NBR_FIBER_USER__c` | FORMULA71 (formula), AGGREGATE38 (aggregate), FORMULA69 (formula) |
| `NBR_FIXED_BBB_FIBER__c` | FORMULA70 (formula), AGGREGATE38 (aggregate), FORMULA69 (formula) |
| `NBR_TBB_MOBIL_USER__c` | FORMULA71 (formula), AGGREGATE38 (aggregate), FORMULA69 (formula) |
| `NBR_TBB_MOBIL__c` | FORMULA70 (formula), AGGREGATE38 (aggregate), FORMULA69 (formula) |
| `Name` | DROP_FIELDS21 (schema), DROP_FIELDS18 (schema), FORMULA78 (formula), FORMULA59 (formula) |
| `StatusKURT__c` | FILTER9 (filter) |
| `SubsMobileVoice__c` | AGGREGATE38 (aggregate) |

#### Fields to ELIMINATE

- `CompanyFamily__c`
- `DPSS_Owner_Full_Name__c`
- `IsDeleted`
- `NBR_FIBER_PAYER__c`
- `NBR_TBB_MOBIL_PAYER__c`
- `PostalCity__c`
- `PostalStreet__c`
- `PostalZipcode__c`
- `VisitingCity__c`
- `VisitingStreet__c`
- `VisitingZipcode__c`

### Account_Location__c (`LOAD_DATASET5_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Active_subs__c` | FILTER13_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `Address_Id__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `BUILDING_TYPE_LEVEL_2__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `BUILDING_TYPE_LEVEL_3__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `Building_type__c` | FILTER33_copy0_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `COVERAGE_START_DATE_5G__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `Capacity_code__c` | FILTER13_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) +3 more |
| `Coverage_4GP40__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `Coverage_4G_Plus__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `Coverage_4G__c` | FILTER13_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) +3 more |
| `Coverage_5G_P__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), FORMULA12_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `FAR_ID__c` | FORMULA14_copy0_copy0_copy0_copy0_copy0 (formula), DROP_FIELDS22 (schema), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema) +2 more |
| `Fiber_cost__c` | FILTER13_copy0_copy0_copy0_copy0_copy0_copy0 (filter), FORMULA17_copy0_copy0_copy0_copy0_copy0 (formula), FILTER38 (filter), DROP_FIELDS22 (schema), APPEND2_copy1_copy0 (appendV2) +7 more |
| `Id` | JOIN20 (join), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), JOIN3 (join) +19 more |
| `IsDeleted` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `LFA_IS_ONNET__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `Location_Owner__c` | FORMULA25_copy0_copy0 (computeRelative), FORMULA28_copy0_copy0 (computeRelative), DROP_FIELDS22 (schema), FORMULA30_copy0_copy0 (computeRelative), FORMULA30_copy0_copy0_copy0 (computeRelative) +31 more |
| `Name` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), DROP_FIELDS18 (schema), FORMULA59 (formula) +1 more |
| `OwnerId` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema) |
| `Postal_address__c` | APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), DROP_FIELDS14_copy0_copy0 (schema), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +2 more |
| `Street_address__c` | FILTER33_copy0_copy0_copy0 (filter), APPEND2_copy1_copy0 (appendV2), DROP_FIELDS15_copy0_copy0 (schema), DROP_FIELDS13_copy0_copy0 (schema), FORMULA16_copy0_copy0_copy0_copy0_copy0 (formula) +2 more |
