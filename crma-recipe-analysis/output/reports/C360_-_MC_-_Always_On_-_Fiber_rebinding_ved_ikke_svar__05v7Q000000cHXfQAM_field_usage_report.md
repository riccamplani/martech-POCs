# C360_-_MC_-_Always_On_-_Fiber_rebinding_ved_ikke_svar__05v7Q000000cHXfQAM — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Fiber_rebinding_ved_ikke_svar__05v7Q000000cHXfQAM
**Total nodes:** 54

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 6 | 6 | 0 | 0% |
| LOAD_DATASET10 | Account_Location__c | connectedDataset | 27 | 6 | 21 | 78% |
| **TOTAL** | | | **33** | **12** | **21** | **64%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 6
- **Fields used:** 6
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER4 (filter) |
| `DPSS_Segment__c` | FILTER2 (filter) |
| `Id` | JOIN1 (join), JOIN2 (join), JOIN3 (join), JOIN5 (join), DROP_FIELDS1 (schema) +8 more |
| `KurtID__c` | DROP_FIELDS1 (schema), DROP_FIELDS12 (schema), DROP_FIELDS17 (schema) |
| `StatusKURT__c` | FILTER2 (filter) |
| `TSP_Dealer__c` | FILTER3 (filter) |

### Account_Location__c (`LOAD_DATASET10`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 27
- **Fields used:** 6
- **Fields unused:** 21

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Active_subs__c` | DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) |
| `FAR_ID__c` | TO_DIMENSION0 (typeCast) |
| `Id` | JOIN10 (join), DROP_FIELDS17 (schema), DROP_FIELDS17 (schema), DROP_FIELDS17 (schema) |
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
- `IsDeleted`
- `LFA_IS_ONNET__c`
- `LastModifiedById`
- `LastModifiedDate`
- `Name`
- `OAF_ID__c`
- `OwnerId`
- `SystemModstamp`
