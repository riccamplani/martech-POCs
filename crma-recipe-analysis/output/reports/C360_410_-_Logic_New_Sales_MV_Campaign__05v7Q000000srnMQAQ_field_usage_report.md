# C360_410_-_Logic_New_Sales_MV_Campaign__05v7Q000000srnMQAQ — Field Usage Report

**Recipe:** C360_410_-_Logic_New_Sales_MV_Campaign__05v7Q000000srnMQAQ
**Total nodes:** 612

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET12 | Account | connectedDataset | 15 | 15 | 0 | 0% |
| LOAD_DATASET14 | Account | connectedDataset | 12 | 6 | 6 | 50% |
| **TOTAL** | | | **27** | **21** | **6** | **22%** |

## Detail per Source Object

### Account (`LOAD_DATASET12`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 15
- **Fields used:** 15
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_QUALITYMARK_PHONE__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +11 more |
| `FORBUND_START_DATE__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +9 more |
| `Forbund_membership__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +16 more |
| `Has_Subscriptions_Actual__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +24 more |
| `Has_Subscriptions__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +5 more |
| `Id` | FORMULA0 (formula), JOIN6 (join), JOIN7 (join), JOIN8 (join), JOIN9 (join) +197 more |
| `Mobile_Voice_Penetration__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +5 more |
| `NACE_Subclass_Code__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), FILTER69 (filter), FILTER68 (filter) +5 more |
| `NumberOfEmployees` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), FILTER49 (filter), FILTER47 (filter) +30 more |
| `Reservation_Date_MV_Inbound__c` | FILTER6_copy0 (filter), FILTER6 (filter), APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2) +12 more |
| `Reservation_Date_MV_Outbound__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), FILTER7_copy0 (filter), FILTER7 (filter) +11 more |
| `Segment__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +5 more |
| `TM_Forbund_Flag__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), DROP_FIELDS15 (schema), DROP_FIELDS14 (schema) +5 more |
| `TSP_Dealer__c` | FILTER4 (filter), FILTER5 (filter), FILTER4_copy0 (filter), FILTER5_copy0 (filter), APPEND6 (appendV2) +9 more |
| `mobile_service_segment__c` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND7 (appendV2), FILTER49 (filter), DROP_FIELDS15 (schema) +6 more |

### Account (`LOAD_DATASET14`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 6
- **Fields unused:** 6

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `FORBUND_START_DATE__c` | FORMULA19 (formula), FORMULA42 (formula) |
| `Forbund_membership__c` | FORMULA19 (formula), FORMULA26_copy0 (formula), FORMULA26_copy0_copy0_copy0 (formula), FORMULA26_copy0_copy0_copy0_copy0 (formula), FORMULA26_copy1_copy0 (formula) +3 more |
| `Has_Subscriptions__c` | FORMULA19 (formula), FORMULA42 (formula) |
| `Id` | FORMULA9 (formula), FORMULA9_copy0 (formula), FORMULA9_copy0_copy0 (formula), FORMULA9_copy0_copy0_copy0 (formula), FORMULA9_copy2 (formula) +70 more |
| `KurtID__c` | FORMULA8 (formula), FORMULA8_copy0 (formula), FORMULA8_copy0_copy0 (formula), FORMULA8_copy0_copy0_copy0 (formula), FORMULA8_copy2 (formula) +33 more |
| `NumberOfEmployees` | FORMULA19 (formula), FORMULA42 (formula) |

#### Fields to ELIMINATE

- `MBN_PROD_HOVEDNUMMER_ACT_DATE__c`
- `NBR_FIBER_USER__c`
- `NBR_FIXED_BBB_FIBER__c`
- `NBR_TBB_MOBIL_USER__c`
- `NBR_TBB_MOBIL__c`
- `SubsM2M__c`
