# C360_490_-_Logic_Førstegangssamtale_Small_Campaign__05v7Q000000cHI1QAM — Field Usage Report

**Recipe:** C360_490_-_Logic_Førstegangssamtale_Small_Campaign__05v7Q000000cHI1QAM
**Total nodes:** 71

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 22 | 22 | 0 | 0% |
| **TOTAL** | | | **22** | **22** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 22
- **Fields used:** 22
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_PHONENBR_STATUS__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `COM_CUSTOMER_TM_RESERVATION__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), FILTER1 (filter) |
| `CustomerType__c` | FILTER37 (filter) |
| `Id` | JOIN9 (join), JOIN0 (join), JOIN7 (join), APPEND5 (appendV2), APPEND5 (appendV2) +10 more |
| `KurtID__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), APPEND2 (appendV2) +4 more |
| `MBN_PROD_KO_ACT_DATE__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER17 (filter) +4 more |
| `MBN_PROD_SVARSGRUPER_ACT_DATE__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER17 (filter) +4 more |
| `MV_FIRST_SALE_DT__c` | FILTER2 (filter), FILTER3 (filter), APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) +4 more |
| `NBR_MBN_AVANSERT_SENTRALBORD__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER17 (filter) +4 more |
| `NBR_MBN_SENTRALBORD__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER17 (filter) +4 more |
| `NBR_MBN__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER15 (filter) +4 more |
| `NBR_SAFEZONE_MOBILE__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), DROP_FIELDS5 (schema), FILTER18 (filter) +4 more |
| `NEW_MV__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `NEW_TN__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `Name` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), FORMULA12 (formula) |
| `NumberOfEmployees` | FORMULA28 (formula) |
| `Phone` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `Phonenumber_type__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), FILTER1 (filter) |
| `Segment__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `StatusKURT__c` | FILTER0 (filter), APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2) |
| `SubsMobileVoice__c` | FORMULA28 (formula) |
| `TSP_Dealer__c` | APPEND5 (appendV2), APPEND5 (appendV2), APPEND1 (appendV2), FILTER5 (filter) |
