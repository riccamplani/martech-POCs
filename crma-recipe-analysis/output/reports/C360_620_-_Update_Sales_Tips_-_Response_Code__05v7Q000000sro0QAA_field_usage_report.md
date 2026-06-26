# C360_620_-_Update_Sales_Tips_-_Response_Code__05v7Q000000sro0QAA — Field Usage Report

**Recipe:** C360_620_-_Update_Sales_Tips_-_Response_Code__05v7Q000000sro0QAA
**Total nodes:** 15

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET5 | C360 510 New Sales Tips | analyticsDataset | 30 | 7 | 23 | 77% |
| LOAD_DATASET4 | Campaign | connectedDataset | 5 | 3 | 2 | 40% |
| LOAD_DATASET1 | CustomerCampaignItem__c | connectedDataset | 14 | 6 | 8 | 57% |
| **TOTAL** | | | **49** | **16** | **33** | **67%** |

## Detail per Source Object

### C360 510 New Sales Tips (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 30
- **Fields used:** 7
- **Fields unused:** 23

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignChannels` | DROP_FIELDS1 (schema) |
| `KSBID_2` | JOIN1 (join), FILTER1 (filter), DROP_FIELDS1 (schema) |
| `Kurt_Id` | DROP_FIELDS1 (schema) |
| `SFB_AccountId` | DROP_FIELDS1 (schema) |
| `SFB_CampainId` | DROP_FIELDS1 (schema) |
| `Sales_tip_title` | DROP_FIELDS1 (schema) |
| `TelesalesAgency` | DROP_FIELDS1 (schema) |

#### Fields to ELIMINATE

- `AccountCampaignID`
- `Personalization_10__c`
- `Personalization_11__c`
- `Personalization_12__c`
- `Personalization_13__c`
- `Personalization_14__c`
- `Personalization_15__c`
- `Personalization_16__c`
- `Personalization_17__c`
- `Personalization_18__c`
- `Personalization_19__c`
- `Personalization_1__c`
- `Personalization_20__c`
- `Personalization_2__c`
- `Personalization_3__c`
- `Personalization_4__c`
- `Personalization_5__c`
- `Personalization_6__c`
- `Personalization_7__c`
- `Personalization_8__c`
- `Personalization_9__c`
- `Rank_Accounts`
- `Sales_tip_description_template`

### Campaign (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 5
- **Fields used:** 3
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Channels__c` | FILTER4 (filter) |
| `Id` | JOIN2 (join) |
| `Status` | FILTER4 (filter) |

#### Fields to ELIMINATE

- `CampaignID__c`
- `Name`

### CustomerCampaignItem__c (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 14
- **Fields used:** 6
- **Fields unused:** 8

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Callinglist_status__c` | FILTER2 (filter) |
| `Campaign__c` | JOIN2 (join) |
| `CreatedDate` | FILTER2 (filter) |
| `Id` | JOIN2 (join) |
| `KSBID__c` | JOIN1 (join) |
| `Status__c` | FILTER2 (filter) |

#### Fields to ELIMINATE

- `Callback_Valid_To_Date__c`
- `Callinglist__c`
- `CampaignID__c`
- `Dialer_Account_Id__c`
- `Reason_Sub_code__c`
- `Response_Code__c`
- `Response_Date__c`
- `tm_agency__c`
