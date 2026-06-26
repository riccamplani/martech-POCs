# C360_-_MC_-_Always_On_-_Onboarding_ny_SafeZone_Mobil_kunde__05v7Q000000PYMPQA4 — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Onboarding_ny_SafeZone_Mobil_kunde__05v7Q000000PYMPQA4
**Total nodes:** 66

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET0 | Account | connectedDataset | 62 | 10 | 52 | 84% |
| **TOTAL** | | | **62** | **10** | **52** | **84%** |

## Detail per Source Object

### Account (`LOAD_DATASET0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 62
- **Fields used:** 10
- **Fields unused:** 52

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN1 (join), DROP_FIELDS9 (schema), FORMULA19 (formula), FORMULA21 (formula), FORMULA39 (formula) |
| `KurtID__c` | FORMULA17 (formula) |
| `NBR_FIXED_BBB_FIBER__c` | FORMULA6 (formula) |
| `NBR_SAFEZONE_IA__c` | FORMULA7 (formula) |
| `NBR_TBB_MOBIL__c` | FORMULA6 (formula) |
| `Name` | DROP_FIELDS9 (schema), FORMULA16 (formula) |
| `SAFEZONE_MOB_START_DT__c` | FILTER0 (filter) |
| `SOURCE_ACCOUNT_ID_MOBIL__c` | FORMULA8 (formula) |
| `StatusKURT__c` | FILTER1 (filter) |
| `mobile_service_segment__c` | FILTER1 (filter) |

#### Fields to ELIMINATE

- `COM_CUSTOMER_EDM_RESERVATION__c`
- `CompanyFamily__c`
- `Concern__c`
- `Country__c`
- `CreatedDate`
- `CustomerType__c`
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
- `NBR_SAFEZONE_MOBILE__c`
- `NBR_SOURCE_ACCOUNT_ID_MOBIL__c`
- `NumberOfEmployees`
- `OrgNo__c`
- `ParentId`
- `Phone`
- `Phonenumber_type__c`
- `Portfolio__c`
- `PostalCity__c`
- `PostalStreet__c`
- `RecordTypeId`
- `Segment__c`
- `TopLevelAccountID__c`
