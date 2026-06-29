# C360_310_-_Logic_Service_Model_SE__05v7Q000000srmxQAA — Field Usage Report

**Recipe:** C360_310_-_Logic_Service_Model_SE__05v7Q000000srmxQAA
**Total nodes:** 85

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0_copy0 | Account | connectedDataset | 12 | 12 | 0 | 0% |
| LOAD_DATASET0_copy0_copy0 | Account | connectedDataset | 15 | 15 | 0 | 0% |
| LOAD_DATASET0_copy0_copy1 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| **TOTAL** | | | **29** | **29** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 12
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` | FILTER56_copy0 (filter), APPEND16 (appendV2), APPEND17 (appendV2) |
| `Id` | JOIN0 (join), JOIN3 (join), APPEND16 (appendV2), DROP_FIELDS0_copy1 (schema), DROP_FIELDS0_copy0_copy0 (schema) +12 more |
| `IsDeleted` | FILTER1_copy0_copy0 (filter), APPEND16 (appendV2), APPEND17 (appendV2) |
| `Mobile_Voice_Penetration__c` | FILTER57_copy0 (filter), APPEND16 (appendV2), APPEND17 (appendV2) |
| `NACE_Subclass_Code__c` | APPEND16 (appendV2), APPEND17 (appendV2) |
| `NumberOfEmployees` | FILTER52_copy0_copy0_copy0_copy0 (filter), FILTER52_copy0_copy0_copy0_copy0_copy0 (filter), FILTER52_copy0_copy0_copy0_copy0_copy0_copy0 (filter), FILTER52_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (filter), FILTER52_copy0_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (filter) +3 more |
| `Portfolio__c` | APPEND16 (appendV2), APPEND17 (appendV2) |
| `Segment__c` | APPEND16 (appendV2), APPEND17 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0_copy0 (filter), APPEND16 (appendV2), APPEND17 (appendV2) |
| `SubsMobileVoice__c` | FILTER57_copy0 (filter), FILTER44_copy0_copy0 (filter), FILTER44_copy0_copy0_copy0 (filter), FILTER44_copy0_copy0_copy0_copy0 (filter), APPEND16 (appendV2) +1 more |
| `VisitingCounty__c` | APPEND16 (appendV2), APPEND17 (appendV2) |
| `mobile_service_segment__c` | APPEND16 (appendV2), APPEND17 (appendV2) |

### Account (`LOAD_DATASET0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 15
- **Fields used:** 15
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Owner_Full_Name__c` | FILTER56 (filter) |
| `Company_Family_Name__c` | FILTER4_copy0_copy0_copy1 (filter) |
| `Forbund_membership__c` | FILTER49 (filter), FILTER50 (filter) |
| `Id` | JOIN1 (join), JOIN4 (join), FILTER59 (filter), DROP_FIELDS3 (schema), DROP_FIELDS0_copy0_copy0_copy0_copy0_copy0 (schema) +6 more |
| `IsDeleted` | FILTER1_copy0_copy0_copy0 (filter) |
| `Mobile_Voice_Penetration__c` | FILTER57 (filter) |
| `NACE_Subclass_Code__c` |  |
| `NumberOfEmployees` | FILTER52_copy0_copy1 (filter), FILTER52_copy0_copy0_copy0 (filter), FILTER52_copy0_copy1_copy0 (filter), FILTER52_copy0_copy1_copy0_copy0 (filter) |
| `Portfolio__c` |  |
| `Segment__c` |  |
| `StatusKURT__c` | FILTER1_copy0_copy0_copy0 (filter) |
| `SubsMobileVoice__c` | FILTER57 (filter) |
| `TM_Forbund_Flag__c` |  |
| `VisitingCounty__c` |  |
| `mobile_service_segment__c` |  |

### Account (`LOAD_DATASET0_copy0_copy1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA1 (formula), JOIN0 (join), JOIN1 (join), JOIN3 (join), JOIN4 (join) +24 more |
| `KurtID__c` | JOIN2 (join) |
