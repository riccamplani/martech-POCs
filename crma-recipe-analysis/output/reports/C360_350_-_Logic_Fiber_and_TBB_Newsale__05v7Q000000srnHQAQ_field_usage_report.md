# C360_350_-_Logic_Fiber_and_TBB_Newsale__05v7Q000000srnHQAQ — Field Usage Report

**Recipe:** C360_350_-_Logic_Fiber_and_TBB_Newsale__05v7Q000000srnHQAQ
**Total nodes:** 61

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 65 | 65 | 0 | 0% |
| **TOTAL** | | | **65** | **65** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 65
- **Fields used:** 65
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CompanyFamily__c` |  |
| `Company_Family_Name__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `Concern__c` |  |
| `Country__c` |  |
| `CreatedDate` |  |
| `CustomerType__c` |  |
| `DPSS_Portfolio__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `DPSS_Segment__c` | FILTER1 (filter), DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `DealerChain__c` |  |
| `DealerID__c` |  |
| `DivisionSPOC__c` |  |
| `E_mail__c` |  |
| `Has_Subscriptions_Actual__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `Has_Subscriptions__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `Id` | DROP_FIELDS11 (schema), FORMULA0 (formula), JOIN0 (join), JOIN10 (join), JOIN10 (join) +18 more |
| `Industry__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `KurtID__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `LevelOfCertification__c` |  |
| `LevelOfComplexity__c` |  |
| `MDRevFixedL12__c` |  |
| `MDRevIDCL12__c` |  |
| `MDRevMobileL12__c` |  |
| `MDRevTotTelenorL12__c` |  |
| `MDSubsFixedBroadband__c` |  |
| `MDSubsMobileBroadband__c` |  |
| `MDSubsMobileVoice__c` |  |
| `MDSubsNordicConnectIPVPNAccess__c` |  |
| `MDSubsPOTSBLines__c` |  |
| `MDSubsPOTS__c` |  |
| `MRevFixedL12__c` |  |
| `MRevIDCL12__c` |  |
| `MRevMobileL12__c` |  |
| `MRevTotTelenorL12__c` |  |
| `MSubsFixedBroadband__c` |  |
| `MSubsMobileBroadband__c` |  |
| `MSubsMobileVoice__c` |  |
| `MSubsNordicConnectIPVPNAccess__c` |  |
| `MSubsPOTSBLines__c` |  |
| `MSubsPOTS__c` |  |
| `MarketArea__c` |  |
| `Min_Bedrift__c` |  |
| `Mobile_Voice_Penetration__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `NACE_Subclass_Code__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `NBR_FIBER_PAYER__c` |  |
| `NBR_FIBER_USER__c` | FILTER0 (filter) |
| `NBR_FIXED_BBB_FIBER__c` | FILTER0 (filter) |
| `NBR_TBB_MOBIL_PAYER__c` |  |
| `NBR_TBB_MOBIL_USER__c` | FILTER0 (filter) |
| `NBR_TBB_MOBIL__c` | FILTER0 (filter) |
| `NBR_VOICE_PAYER__c` |  |
| `Name` |  |
| `NumberOfEmployees` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `OrgNo__c` |  |
| `Phone` |  |
| `Phonenumber_type__c` | DROP_FIELDS11 (schema), FILTER12 (filter), DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `Reservation_Date_IA_Inbound__c` |  |
| `Reservation_Date_IA_Outbound__c` |  |
| `Reservation_Date_MV_Inbound__c` |  |
| `Reservation_Date_MV_Outbound__c` |  |
| `RevTotTelenorL12__c` |  |
| `Segment__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `Service_segment__c` |  |
| `SubsMobileVoice__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `TSP_Dealer__c` | DROP_FIELDS1 (schema), DROP_FIELDS2 (schema) |
| `TopLevelAccountID__c` |  |
