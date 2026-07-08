# C360_431_-_Logic_Fiber_Newsale_Feil_nummer_Campaign__05vJ7000000wkVLIAY — Field Usage Report

**Recipe:** C360_431_-_Logic_Fiber_Newsale_Feil_nummer_Campaign__05vJ7000000wkVLIAY
**Total nodes:** 97

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET4 | Account | connectedDataset | 18 | 16 | 2 | 11% |
| **TOTAL** | | | **18** | **16** | **2** | **11%** |

## Detail per Source Object

### Account (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 18
- **Fields used:** 16
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_TM_RESERVATION__c` | FORMULA21_copy0 (formula) |
| `CompanyFamily__c` | FORMULA14_copy0 (formula) |
| `CustomerType__c` | FORMULA15_copy0 (formula), FORMULA39_copy0 (formula), FORMULA40_copy0 (formula) |
| `External_Credit_Rating__c` | FORMULA19_copy0 (formula) |
| `Has_Subscriptions_Actual__c` | FORMULA23_copy0 (formula) |
| `Id` | JOIN0 (join), JOIN1 (join), JOIN2 (join), JOIN3 (join), JOIN4 (join) +15 more |
| `KurtID__c` | DROP_FIELDS26_copy0 (schema), DROP_FIELDS29 (schema), FILTER5 (filter), DROP_FIELDS7_copy0_copy0 (schema), FORMULA20_copy0_copy0 (formula) +1 more |
| `NACE_Subclass_Code__c` | FORMULA15_copy0 (formula) |
| `NACE_Subclass_Description__c` | FORMULA25_copy0 (formula) |
| `Name` | FORMULA20_copy0 (formula), FORMULA24_copy0 (formula), DROP_FIELDS7_copy0_copy0 (schema), FORMULA26_copy0_copy0 (formula) |
| `NumberOfEmployees` | FORMULA15_copy0 (formula), FORMULA40_copy0 (formula) |
| `Phonenumber_type__c` | FORMULA22_copy0 (formula) |
| `Reservation_Date_IA_Outbound__c` | FORMULA29_copy0 (formula), DROP_FIELDS26_copy0 (schema), FORMULA44 (formula) |
| `StatusKURT__c` | FORMULA17_copy0 (formula) |
| `SubsMobileVoice__c` | FORMULA32_copy0 (formula) |
| `VisitingCounty__c` | FORMULA18_copy0 (formula) |

#### Fields to ELIMINATE

- `DPSS_Segment__c`
- `IsDeleted`
