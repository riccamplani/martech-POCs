# MC_-_Automatised_Rebinding_-_Deep_sales_using_SafeZone__05vdV00000Fbux3QAB — Field Usage Report

**Recipe:** MC_-_Automatised_Rebinding_-_Deep_sales_using_SafeZone__05vdV00000Fbux3QAB
**Total nodes:** 113

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET17_copy0_copy0_copy0_copy0_copy0_copy0 | Account | connectedDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET22 | Contact | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET22_copy0 | Contact | connectedDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET2_copy0_copy1_copy0_copy0 | Contact | connectedDataset | 2 | 2 | 0 | 0% |
| **TOTAL** | | | **26** | **26** | **0** | **0%** |

## Detail per Source Object

### Account (`LOAD_DATASET17_copy0_copy0_copy0_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `COM_CUSTOMER_EDM_RESERVATION__c` | FILTER5_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `Forbund_membership__c` | APPEND26 (appendV2), FILTER69 (filter), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `Id` | JOIN23 (join), FILTER98 (filter), JOIN24 (join), JOIN29 (join), JOIN30 (join) +29 more |
| `IsDeleted` | FILTER1_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `KurtID__c` | FILTER99 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +5 more |
| `Migration_flag__c` | FILTER95 (filter), FILTER96 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2) +2 more |
| `Mobile_Segment__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `NBR_OPPDATERT__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `NBR_SAFEZONE_MOBILE__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `NBR_SOURCE_ACCOUNT_ID_MOBIL__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `Name` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) +3 more |
| `NumberOfEmployees` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `PersonHasOptedOutOfEmail` | FILTER5_copy0_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `SOURCE_ACCOUNT_ID_MOBIL__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `Segment__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `Service_segment__c` | APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2), APPEND30 (appendV2) |
| `StatusKURT__c` | FILTER1_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `SubsMobileVoice__c` | APPEND26 (appendV2), FILTER64_copy0 (filter), FILTER64 (filter), FILTER65 (filter), APPEND27 (appendV2) +3 more |
| `TSP_Dealer__c` | APPEND26 (appendV2), FILTER63 (filter), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |
| `mobile_service_segment__c` | FILTER61_copy0_copy0_copy0_copy0_copy0_copy0 (filter), APPEND26 (appendV2), APPEND27 (appendV2), APPEND28 (appendV2), APPEND29 (appendV2) +1 more |

### Contact (`LOAD_DATASET22`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA48 (computeRelative), FORMULA49 (formula), JOIN27 (join), FORMULA44_copy1 (formula), APPEND28 (appendV2) +2 more |
| `Id` | JOIN28 (join), FORMULA48 (computeRelative), JOIN29 (join), JOIN30 (join), JOIN31 (join) +28 more |

### Contact (`LOAD_DATASET22_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA48_copy0 (computeRelative), FORMULA49_copy0 (formula), JOIN27 (join), FORMULA44_copy1 (formula), APPEND28 (appendV2) +2 more |
| `Id` | JOIN28_copy0 (join), FORMULA48_copy0 (computeRelative), JOIN30 (join), JOIN31 (join), APPEND26 (appendV2) +27 more |

### Contact (`LOAD_DATASET2_copy0_copy1_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountId` | FORMULA48_copy0_copy0 (computeRelative), FORMULA0_copy0_copy0_copy0 (formula), JOIN27 (join), FORMULA44_copy1 (formula), APPEND28 (appendV2) +2 more |
| `Id` | JOIN0_copy2_copy0_copy0 (join), FORMULA48_copy0_copy0 (computeRelative), JOIN31 (join), APPEND26 (appendV2), APPEND26 (appendV2) +26 more |
