# C360_461_-_Logic_New_Sales_SafeZone_Oppdatert__05v7Q000000cHw8QAE — Field Usage Report

**Recipe:** C360_461_-_Logic_New_Sales_SafeZone_Oppdatert__05v7Q000000cHw8QAE
**Total nodes:** 34

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 9 | 9 | 0 | 0% |
| **TOTAL** | | | **9** | **9** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 9
- **Fields used:** 9
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | APPEND0 (appendV2), FILTER23 (filter), JOIN2 (join), FORMULA21_copy0_copy0 (formula), FORMULA22_copy0_copy0 (formula) +1 more |
| `IsDeleted` | FILTER0 (filter), APPEND0 (appendV2) |
| `KurtID__c` | APPEND0 (appendV2), FORMULA20_copy0_copy0 (formula), FORMULA23_copy0_copy0 (formula), DROP_FIELDS8_copy0_copy0 (schema) |
| `Mobile_Segment__c` | FILTER0 (filter), APPEND0 (appendV2) |
| `NBR_OPPDATERT__c` | FILTER4 (filter), APPEND0 (appendV2) |
| `NBR_SAFEZONE_MOBILE__c` | FILTER2 (filter), FILTER3 (filter), APPEND0 (appendV2) |
| `StatusKURT__c` | FILTER0 (filter), APPEND0 (appendV2) |
| `SubsMobileVoice__c` | FILTER1 (filter), APPEND0 (appendV2) |
| `mobile_service_segment__c` | APPEND0 (appendV2) |
