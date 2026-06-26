# C360_494_-_New_Sales_MV_Churn_Customer_last_12-30_months__05vJ7000000wlalIAA — Field Usage Report

**Recipe:** C360_494_-_New_Sales_MV_Churn_Customer_last_12-30_months__05vJ7000000wlalIAA
**Total nodes:** 34

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET11 | Account | connectedDataset | 10 | 1 | 9 | 90% |
| LOAD_DATASET14_copy0 | Account | connectedDataset | 2 | 2 | 0 | 0% |
| **TOTAL** | | | **12** | **3** | **9** | **75%** |

## Detail per Source Object

### Account (`LOAD_DATASET11`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 1
- **Fields unused:** 9

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN1 (join) |

#### Fields to ELIMINATE

- `Has_Subscriptions_Actual__c`
- `IsDeleted`
- `KurtID__c`
- `Latest_Port_out_date__c`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `StatusKURT__c`
- `SubsMobileVoice__c`
- `mobile_service_segment__c`

### Account (`LOAD_DATASET14_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | FORMULA9_copy0 (formula), FORMULA10_copy0 (formula) |
| `KurtID__c` | FORMULA8_copy0 (formula), FORMULA11_copy0 (formula) |
