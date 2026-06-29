# C360_220_-_Logic_Suppressions__05v7Q000000srmsQAA — Field Usage Report

**Recipe:** C360_220_-_Logic_Suppressions__05v7Q000000srmsQAA
**Total nodes:** 251

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 28 | 28 | 0 | 0% |
| LOAD_DATASET16_copy0 | Contact | connectedDataset | 4 | 4 | 0 | 0% |
| **TOTAL** | | | **32** | **32** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 28
- **Fields used:** 28
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_QUALITYMARK_PHONE__c` | FILTER23 (filter) |
| `COM_CUSTOMER_TM_RESERVATION__c` | FILTER1 (filter) |
| `CompanyFamily__c` | FILTER10 (filter) |
| `CustomerType__c` | FILTER18 (filter), FILTER20_copy0 (filter), FILTER25 (filter) |
| `DPSS_DMU__c` | DROP_FIELDS37 (schema), FORMULA8 (formula) |
| `Economic_Attractivity__c` | FILTER24 (filter) |
| `External_Credit_Rating__c` | FILTER0 (filter) |
| `Has_Subscriptions_Actual__c` | FILTER20 (filter), FILTER23 (filter), FILTER20_copy0 (filter), FILTER25 (filter) |
| `Has_Subscriptions__c` |  |
| `Id` | DROP_FIELDS37 (schema), DROP_FIELDS7 (schema), DROP_FIELDS10 (schema), DROP_FIELDS4 (schema), DROP_FIELDS5 (schema) +76 more |
| `IsDeleted` | FILTER1_copy0 (filter) |
| `Is_DMU__c` | DROP_FIELDS37 (schema), FORMULA8 (formula), FILTER30 (filter) |
| `NACE_Subclass_Code__c` | FILTER18 (filter), JOIN4 (join) |
| `NACE_Subclass_Description__c` | FILTER20 (filter) |
| `NBR_FIBER_USER__c` |  |
| `NBR_FIXED_BBB_FIBER__c` |  |
| `NBR_TBB_MOBIL_USER__c` |  |
| `NBR_TBB_MOBIL__c` |  |
| `Name` | FILTER2 (filter), FILTER20 (filter) |
| `NumberOfEmployees` | FILTER18 (filter), FILTER25 (filter) |
| `Phonenumber_type__c` | FILTER3 (filter) |
| `Portfolio__c` | FILTER7 (filter) |
| `Reservation_Date_IA_Inbound__c` | FILTER15 (filter) |
| `Reservation_Date_IA_Outbound__c` | FILTER16 (filter) |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` |  |
| `StatusKURT__c` | FILTER1_copy0_copy0 (filter) |
| `VisitingCounty__c` | FILTER22 (filter) |

### Contact (`LOAD_DATASET16_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA21_copy0 (computeRelative), FORMULA22_copy0 (formula) |
| `Birthdate` | FILTER38_copy0 (filter) |
| `Id` | FORMULA21_copy0 (computeRelative) |
| `Primary__c` | FILTER37_copy0 (filter) |
