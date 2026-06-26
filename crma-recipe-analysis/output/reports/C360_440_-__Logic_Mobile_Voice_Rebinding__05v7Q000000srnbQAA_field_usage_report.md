# C360_440_-__Logic_Mobile_Voice_Rebinding__05v7Q000000srnbQAA — Field Usage Report

**Recipe:** C360_440_-__Logic_Mobile_Voice_Rebinding__05v7Q000000srnbQAA
**Total nodes:** 292

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 21 | 7 | 14 | 67% |
| LOAD_DATASET14 | Account | connectedDataset | 7 | 7 | 0 | 0% |
| **TOTAL** | | | **28** | **14** | **14** | **50%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 21
- **Fields used:** 7
- **Fields unused:** 14

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Forbund_membership__c` | FILTER57 (filter) |
| `Id` | JOIN0 (join), JOIN2 (join), DROP_FIELDS0 (schema), APPEND0 (appendV2), JOIN1 (join) +92 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `Migration_flag__c` | FORMULA19 (formula) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0_copy0 (filter) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0_copy0 (filter) |

#### Fields to ELIMINATE

- `MBN_PROD_KO_ACT_DATE__c`
- `MBN_PROD_SVARSGRUPER_ACT_DATE__c`
- `Mobile_Voice_Penetration__c`
- `NBR_MBN_AVANSERT_SENTRALBORD__c`
- `NBR_MBN_SENTRALBORD__c`
- `NBR_MBN__c`
- `NBR_OPPDATERT__c`
- `NBR_SAFEZONE_MOBILE__c`
- `OrgNo__c`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `Segment__c`
- `SubsMobileVoice__c`
- `TSP_Dealer__c`

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 7
- **Fields used:** 7
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Diff_new_callplan_rev__c` | FORMULA23 (formula) |
| `Id` | FORMULA9_copy0_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy0_copy1 (formula), FORMULA9_copy0_copy0_copy0_copy0_copy0 (formula) +23 more |
| `KurtID__c` | FORMULA8_copy0_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy0_copy1 (formula), FORMULA8_copy0_copy0_copy0_copy0_copy0 (formula) +7 more |
| `Migration_flag__c` | FORMULA0 (formula), FORMULA0_copy0 (formula), FORMULA0_copy0_copy0 (formula), FORMULA0_copy0_copy0_copy0 (formula), FORMULA0_copy0_copy1 (formula) +3 more |
| `Mobile_Voice_Penetration__c` | FORMULA30 (formula), FORMULA28 (formula) |
| `NBR_SAFEZONE_MOBILE__c` | FORMULA0 (formula), FORMULA24 (formula), FORMULA27 (formula) |
| `NumberofEmployees_clean__c` | FORMULA29 (formula) |
