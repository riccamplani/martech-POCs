# C360_494_-_New_Sales_MV_Churn_Customer_last_12-30_months__05vJ7000000wlalIAA — Field Usage Report

**Recipe:** C360_494_-_New_Sales_MV_Churn_Customer_last_12-30_months__05vJ7000000wlalIAA
**Total nodes:** 34

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET11 | Account | connectedDataset | 10 | 10 | 0 | 0% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| **TOTAL** | | | **12** | **12** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET11`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 10
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Has_Subscriptions_Actual__c` |  |
| `Id` | JOIN1 (join), DROP_FIELDS12_copy0_copy1_copy0 (schema), JOIN16 (join) |
| `IsDeleted` |  |
| `KurtID__c` |  |
| `Latest_Port_out_date__c` | FILTER3 (filter) |
| `Reservation_Date_MV_Inbound__c` | FILTER6_copy2_copy0 (filter) |
| `Reservation_Date_MV_Outbound__c` | FILTER8_copy0 (filter) |
| `StatusKURT__c` |  |
| `SubsMobileVoice__c` |  |
| `mobile_service_segment__c` | FILTER2 (filter) |

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
