# C360_491_-_Mobile_Voice_Rebinding_Agrol__05v7Q000000cHIzQAM — Field Usage Report

**Recipe:** C360_491_-_Mobile_Voice_Rebinding_Agrol__05v7Q000000cHIzQAM
**Total nodes:** 91

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET14_copy0_copy0 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| **TOTAL** | | | **27** | **27** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Company_Family_Name__c` | FILTER4_copy0 (filter) |
| `Forbund_membership__c` |  |
| `Id` | JOIN2 (join), JOIN1 (join), FORMULA24_copy0 (computeRelative), FILTER60 (filter), FILTER19 (filter) +15 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `MBN_PROD_KO_ACT_DATE__c` | FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `Migration_flag__c` | FILTER59 (filter) |
| `Mobile_Voice_Penetration__c` |  |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `NBR_MBN_SENTRALBORD__c` | FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `NBR_MBN__c` | FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `NBR_SAFEZONE_MOBILE__c` | FILTER61 (filter), FILTER61_copy0 (filter) |
| `OrgNo__c` |  |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` | FILTER38 (filter), FILTER36 (filter), FILTER37 (filter) |
| `Segment__c` |  |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `SubsMobileVoice__c` | FILTER4 (filter), FILTER48_copy1_copy0 (filter), FILTER48_copy1_copy0_copy0 (filter) |
| `TSP_Dealer__c` | FILTER10_copy0_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0 (filter) |

### Account (`LOAD_DATASET14_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN11 (join), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA10_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +9 more |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (formula), FORMULA11_copy0_copy0_copy0_copy0_copy0_copy0 (formula) +1 more |
| `NBR_FIBER_USER__c` | FORMULA19_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy1 (formula) |
| `NBR_FIXED_BBB_FIBER__c` | FORMULA19_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy1 (formula) |
| `NBR_OPPDATERT__c` | FORMULA19_copy0_copy0_copy1 (formula) |
| `NBR_TBB_MOBIL_USER__c` | FORMULA19_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy1 (formula) |
| `NBR_TBB_MOBIL__c` | FORMULA19_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy0 (formula), FORMULA19_copy0_copy0_copy1 (formula) |
