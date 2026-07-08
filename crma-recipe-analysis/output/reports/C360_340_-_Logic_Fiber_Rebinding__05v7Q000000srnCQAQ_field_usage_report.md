# C360_340_-_Logic_Fiber_Rebinding__05v7Q000000srnCQAQ — Field Usage Report

**Recipe:** C360_340_-_Logic_Fiber_Rebinding__05v7Q000000srnCQAQ
**Total nodes:** 149

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET1 | Account | connectedDataset | 72 | 6 | 66 | 92% |
| **TOTAL** | | | **72** | **6** | **66** | **92%** |

## Detail per Source Object

### Account (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 72
- **Fields used:** 6
- **Fields unused:** 66

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `DPSS_Segment__c` | FILTER0 (filter), FILTER8 (filter), FILTER30_copy0 (filter), FILTER9 (filter) |
| `Id` | DROP_FIELDS17_copy1 (schema), DROP_FIELDS5 (schema), DROP_FIELDS15 (schema), DROP_FIELDS17_copy0 (schema), JOIN14 (join) +33 more |
| `KurtID__c` | DROP_FIELDS17_copy1 (schema), DROP_FIELDS15 (schema), DROP_FIELDS17_copy0 (schema), DROP_FIELDS17 (schema), DROP_FIELDS18 (schema) +3 more |
| `NBR_FIXED_BBB_FIBER__c` | FILTER4 (filter) |
| `Name` | DROP_FIELDS34 (schema) |
| `TSP_Dealer__c` | FILTER30 (filter), FILTER30_copy0 (filter) |

#### Fields to ELIMINATE

- `COM_CUSTOMER_TM_RESERVATION__c`
- `CompanyFamily__c`
- `Concern__c`
- `Country__c`
- `CreatedDate`
- `CustomerType__c`
- `DPSS_Portfolio__c`
- `DealerChain__c`
- `DealerID__c`
- `DealerSegment__c`
- `DivisionSPOC__c`
- `E_mail__c`
- `Industry__c`
- `IsDeleted`
- `IsPersonAccount`
- `LevelOfCertification__c`
- `LevelOfComplexity__c`
- `MDRevFixedL12__c`
- `MDRevIDCL12__c`
- `MDRevMobileL12__c`
- `MDRevTotTelenorL12__c`
- `MDSubsFixedBroadband__c`
- `MDSubsMobileBroadband__c`
- `MDSubsMobileVoice__c`
- `MDSubsNordicConnectIPVPNAccess__c`
- `MDSubsPOTSBLines__c`
- `MDSubsPOTS__c`
- `MRevFixedL12__c`
- `MRevIDCL12__c`
- `MRevMobileL12__c`
- `MRevTotTelenorL12__c`
- `MSubsFixedBroadband__c`
- `MSubsMobileBroadband__c`
- `MSubsMobileVoice__c`
- `MSubsNordicConnectIPVPNAccess__c`
- `MSubsPOTSBLines__c`
- `MSubsPOTS__c`
- `MarketArea__c`
- `Min_Bedrift__c`
- `Mobile_Voice_Penetration__c`
- `NACE_Subclass_Code__c`
- `NBR_FIBER_USER__c`
- `NBR_SAFEZONE_IA__c`
- `NBR_TBB_MOBIL_USER__c`
- `NBR_TBB_MOBIL__c`
- `NumberOfEmployees`
- `OrgNo__c`
- `ParentId`
- `Phone`
- `Phonenumber_type__c`
- `Portfolio__c`
- `PostalCity__c`
- `PostalStreet__c`
- `PostalZipcode__c`
- `RecordTypeId`
- `Region__c`
- `Reservation_Date_IA_Inbound__c`
- `Reservation_Date_IA_Outbound__c`
- `Reservation_Date_MV_Inbound__c`
- `Reservation_Date_MV_Outbound__c`
- `RevIDCL12__c`
- `RevTotTelenorL12__c`
- `Segment__c`
- `Service_segment__c`
- `SubsMobileVoice__c`
- `TopLevelAccountID__c`
