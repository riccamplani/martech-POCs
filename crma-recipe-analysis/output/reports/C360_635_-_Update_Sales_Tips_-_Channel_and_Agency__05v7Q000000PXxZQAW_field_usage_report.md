# C360_635_-_Update_Sales_Tips_-_Channel_and_Agency__05v7Q000000PXxZQAW — Field Usage Report

**Recipe:** C360_635_-_Update_Sales_Tips_-_Channel_and_Agency__05v7Q000000PXxZQAW
**Total nodes:** 11

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET5 | C360 510 New Sales Tips | analyticsDataset | 8 | 3 | 5 | 62% |
| LOAD_DATASET4 | CustomerCampaignItem__c | connectedDataset | 10 | 6 | 4 | 40% |
| **TOTAL** | | | **18** | **9** | **9** | **50%** |

## Detail per Source Object

### C360 510 New Sales Tips (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 3
- **Fields unused:** 5

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignChannels` | FORMULA24 (formula), DROP_FIELDS5 (schema) |
| `KSBID_2` | JOIN2 (join) |
| `TelesalesAgency` | FORMULA25 (formula), FORMULA26 (formula) |

#### Fields to ELIMINATE

- `AccountCampaignID`
- `Kurt_Id`
- `SFB_AccountId`
- `SFB_CampainId`
- `Sales_tip_title`

### CustomerCampaignItem__c (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 10
- **Fields used:** 6
- **Fields unused:** 4

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Callinglist__c` | DROP_FIELDS4 (schema) |
| `Campaign_Channels__c` | DROP_FIELDS4 (schema), FORMULA24 (formula) |
| `Id` | DROP_FIELDS4 (schema) |
| `KSBID__c` | DROP_FIELDS4 (schema), JOIN2 (join) |
| `Response_Code__c` | DROP_FIELDS4 (schema) |
| `tm_agency__c` | DROP_FIELDS4 (schema), FORMULA25 (formula) |

#### Fields to ELIMINATE

- `CreatedDate`
- `Reason_Sub_code__c`
- `Response_Date__c`
- `Status__c`
