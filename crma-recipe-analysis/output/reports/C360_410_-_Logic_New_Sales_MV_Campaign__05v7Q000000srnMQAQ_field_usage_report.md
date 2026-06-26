# C360_410_-_Logic_New_Sales_MV_Campaign__05v7Q000000srnMQAQ — Field Usage Report

**Recipe:** C360_410_-_Logic_New_Sales_MV_Campaign__05v7Q000000srnMQAQ
**Total nodes:** 612

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET12 | Account | connectedDataset | 15 | 1 | 14 | 93% |
| LOAD_DATASET14 | Account | connectedDataset | 12 | 6 | 6 | 50% |
| **TOTAL** | | | **27** | **7** | **20** | **74%** |

## Detail per Source Object

### Account (`LOAD_DATASET12`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 15
- **Fields used:** 1
- **Fields unused:** 14

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA0 (formula), JOIN6 (join), JOIN7 (join), JOIN8 (join), JOIN9 (join) +193 more |

#### Fields to ELIMINATE

- `COM_CUSTOMER_QUALITYMARK_PHONE__c`
- `FORBUND_START_DATE__c`
- `Forbund_membership__c`
- `Has_Subscriptions_Actual__c`
- `Has_Subscriptions__c`
- `Mobile_Voice_Penetration__c`
- `NACE_Subclass_Code__c`
- `NumberOfEmployees`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `Segment__c`
- `TM_Forbund_Flag__c`
- `TSP_Dealer__c`
- `mobile_service_segment__c`

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
