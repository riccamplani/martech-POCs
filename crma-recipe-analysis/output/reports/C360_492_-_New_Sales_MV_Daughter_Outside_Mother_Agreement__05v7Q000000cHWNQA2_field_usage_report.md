# C360_492_-_New_Sales_MV_Daughter_Outside_Mother_Agreement__05v7Q000000cHWNQA2 — Field Usage Report

**Recipe:** C360_492_-_New_Sales_MV_Daughter_Outside_Mother_Agreement__05v7Q000000cHWNQA2
**Total nodes:** 34

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 9 | 8 | 1 | 11% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| **TOTAL** | | | **11** | **10** | **1** | **9%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 9
- **Fields used:** 8
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CompanyFamily__c` | FILTER5 (filter), DROP_FIELDS0 (schema), JOIN0 (join), AGGREGATE1 (aggregate), DROP_FIELDS12_copy0_copy0_copy0_copy0 (schema) |
| `Concern__c` | FILTER6 (filter), DROP_FIELDS12_copy0_copy0_copy0_copy0 (schema) |
| `Id` | FILTER4_copy0 (filter), JOIN1 (join), DROP_FIELDS12_copy0_copy0_copy0_copy0 (schema), FILTER37 (filter), JOIN16 (join) |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `NumberOfEmployees` | FILTER3_copy0 (filter), DROP_FIELDS0 (schema), AGGREGATE1 (aggregate) |
| `StatusKURT__c` | FILTER1_copy0 (filter) |
| `SubsMobileVoice__c` | DROP_FIELDS0 (schema), AGGREGATE1 (aggregate) |
| `mobile_service_segment__c` | FILTER3_copy0 (filter) |

#### Fields to ELIMINATE

- `Mobile_Segment__c`

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0 (formula), FORMULA10_copy0 (formula), JOIN16 (join) |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |
