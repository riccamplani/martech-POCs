# C360_-_MC_-_Always_On_-_Velkomstprogram_nye_medlemmer_Forbund__05vJ7000000wlHeIAI — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Velkomstprogram_nye_medlemmer_Forbund__05vJ7000000wlHeIAI
**Total nodes:** 37

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 18 | 18 | 0 | 0% |
| **TOTAL** | | | **18** | **18** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 18
- **Fields used:** 18
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | APPEND3 (appendV2), FILTER5 (filter), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `FORBUND_START_DATE__c` | FILTER15_copy0 (filter), APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `Forbund_membership__c` | FILTER15_copy0 (filter), FILTER84 (filter), APPEND3 (appendV2), DROP_FIELDS4 (schema), FILTER4_copy0_copy0_copy0 (filter) +3 more |
| `Has_Min_Bedrift__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `Id` | APPEND3 (appendV2), JOIN6 (join), DROP_FIELDS4 (schema), APPEND2 (appendV2), JOIN5 (join) +1 more |
| `IsDeleted` | FILTER1_copy0 (filter), APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `KurtID__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2), DROP_FIELDS2_copy0_copy0 (schema) |
| `Last_Min_Bedrift_Web_Login__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `MV_FIRST_SALE_DT__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `NBR_SAFEZONE_MOBILE__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `NBR_SOURCE_ACCOUNT_ID_MOBIL__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `PersonHasOptedOutOfEmail` | APPEND3 (appendV2), FILTER5 (filter), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `SOURCE_ACCOUNT_ID_MOBIL__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0 (filter), APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `SubsMobileVoice__c` | APPEND3 (appendV2), FILTER85 (filter), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
| `TM_Forbund_Flag__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), FILTER4_copy0_copy0_copy0 (filter), FILTER4_copy0_copy0_copy0_copy0 (filter), APPEND2 (appendV2) |
| `TSP_Dealer__c` | APPEND3 (appendV2), DROP_FIELDS4 (schema), FILTER4_copy1 (filter), APPEND2 (appendV2) |
| `mobile_service_segment__c` | FILTER3_copy0 (filter), FILTER3_copy0_copy0 (filter), APPEND3 (appendV2), DROP_FIELDS4 (schema), APPEND2 (appendV2) |
