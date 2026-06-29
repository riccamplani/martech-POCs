# C360_320_-_Logic_Deep_Sale__05v7Q000000srn2QAA — Field Usage Report

**Recipe:** C360_320_-_Logic_Deep_Sale__05v7Q000000srn2QAA
**Total nodes:** 19

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 8 | 8 | 0 | 0% |
| **TOTAL** | | | **8** | **8** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN0 (join), JOIN1 (join), DROP_FIELDS0 (schema), DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `Mobile_Voice_Penetration__c` | FILTER6 (filter), FILTER7 (filter), FILTER9 (filter) |
| `NumberOfEmployees` | FILTER3_copy0_copy0_copy0 (filter) |
| `Segment__c` |  |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `SubsMobileVoice__c` | FILTER4 (filter) |
| `mobile_service_segment__c` | FILTER3_copy0_copy0_copy0 (filter) |
