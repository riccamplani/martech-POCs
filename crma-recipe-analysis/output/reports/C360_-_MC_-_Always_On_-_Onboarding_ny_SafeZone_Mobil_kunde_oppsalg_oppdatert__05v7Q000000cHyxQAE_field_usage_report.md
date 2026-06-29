# C360_-_MC_-_Always_On_-_Onboarding_ny_SafeZone_Mobil_kunde_oppsalg_oppdatert__05v7Q000000cHyxQAE — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Onboarding_ny_SafeZone_Mobil_kunde_oppsalg_oppdatert__05v7Q000000cHyxQAE
**Total nodes:** 65

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 17 | 17 | 0 | 0% |
| **TOTAL** | | | **17** | **17** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 17
- **Fields used:** 17
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER21 (filter), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `Company_Family_Name__c` | DROP_FIELDS18_copy0_copy0 (schema), FORMULA58 (formula), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `Id` | JOIN10 (join), JOIN0 (join), JOIN8 (join), FORMULA55 (formula), JOIN9 (join) +20 more |
| `IsDeleted` | FILTER19 (filter), APPEND0 (appendV2) |
| `KurtID__c` | APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema), DROP_FIELDS24 (schema), FILTER76 (filter) |
| `Last_Min_Bedrift_Web_Login__c` | FILTER73_copy0 (filter) |
| `Mobile_Segment__c` | DROP_FIELDS18_copy0_copy0 (schema), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `NBR_OPPDATERT__c` | FILTER22 (filter), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `NBR_SAFEZONE_MOBILE__c` | FILTER75 (filter), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `Name` | DROP_FIELDS14_copy0 (schema), DROP_FIELDS24 (schema) |
| `NumberOfEmployees` | DROP_FIELDS18_copy0_copy0 (schema), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `SAFEZONE_MOB_START_DT__c` | FILTER0_copy0 (filter), APPEND0 (appendV2) |
| `SOURCE_ACCOUNT_ID_MOBIL__c` | TO_DIMENSION0 (typeCast), APPEND0 (appendV2) |
| `StatusKURT__c` | FILTER19 (filter), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `SubsMobileVoice__c` | DROP_FIELDS18_copy0_copy0 (schema), FORMULA44_copy0_copy0 (formula), APPEND0 (appendV2) |
| `TSP_Dealer__c` | FILTER17 (filter), APPEND0 (appendV2), DROP_FIELDS22 (schema), DROP_FIELDS14_copy0 (schema) |
| `mobile_service_segment__c` | FILTER19 (filter), DROP_FIELDS18_copy0_copy0 (schema), APPEND0 (appendV2) |
