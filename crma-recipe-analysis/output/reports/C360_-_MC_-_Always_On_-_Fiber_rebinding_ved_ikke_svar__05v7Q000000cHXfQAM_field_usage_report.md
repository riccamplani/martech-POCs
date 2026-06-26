# C360_-_MC_-_Always_On_-_Fiber_rebinding_ved_ikke_svar__05v7Q000000cHXfQAM — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Fiber_rebinding_ved_ikke_svar__05v7Q000000cHXfQAM
**Total nodes:** 54

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 6 | 5 | 1 | 17% |
| LOAD_DATASET10 | Account_Location__c | connectedDataset | 27 | 5 | 22 | 81% |
| **TOTAL** | | | **33** | **10** | **23** | **70%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 5
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER4 (filter) |
| `DPSS_Segment__c` | FILTER2 (filter) |
| `Id` | JOIN1 (join) |
| `StatusKURT__c` | FILTER2 (filter) |
| `TSP_Dealer__c` | FILTER3 (filter) |

#### Fields to ELIMINATE

- `KurtID__c`

### Account_Location__c (`LOAD_DATASET10`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 27
- **Fields used:** 5
- **Fields unused:** 22

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Active_subs__c` | DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) |
| `FAR_ID__c` | TO_DIMENSION0 (typeCast) |
| `Location_Owner__c` | DROP_FIELDS14 (schema), DROP_FIELDS15 (schema), JOIN9 (join), JOIN10 (join) |
| `Postal_address__c` | DROP_FIELDS14 (schema), FORMULA34 (formula), DROP_FIELDS15 (schema) |
| `Street_address__c` | DROP_FIELDS14 (schema), FORMULA34 (formula), DROP_FIELDS15 (schema) |

#### Fields to ELIMINATE

- `Address_Id__c`
- `BUILDING_TYPE_LEVEL_2__c`
- `BUILDING_TYPE_LEVEL_3__c`
- `Building_type__c`
- `COVERAGE_START_DATE_5G__c`
- `Capacity_code__c`
- `Coverage_4GP40__c`
- `Coverage_4G_Plus__c`
- `Coverage_4G__c`
- `Coverage_5G_P__c`
- `CreatedById`
- `CreatedDate`
- `Fiber_cost__c`
- `Id`
- `IsDeleted`
- `LFA_IS_ONNET__c`
- `LastModifiedById`
- `LastModifiedDate`
- `Name`
- `OAF_ID__c`
- `OwnerId`
- `SystemModstamp`
