# C360_610_-_Insert_Sales_Tips__05v7Q000000srnvQAA — Field Usage Report

**Recipe:** C360_610_-_Insert_Sales_Tips__05v7Q000000srnvQAA
**Total nodes:** 10

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET5 | C360 510 New Sales Tips | analyticsDataset | 28 | 2 | 26 | 93% |
| LOAD_DATASET4 | CustomerCampaignItem__c | connectedDataset | 2 | 1 | 1 | 50% |
| **TOTAL** | | | **30** | **3** | **27** | **90%** |

## Detail per Source Object

### C360 510 New Sales Tips (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 28
- **Fields used:** 2
- **Fields unused:** 26

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `KSBID_2` | JOIN0 (join) |
| `SFB_CampainId` | FORMULA2 (formula) |

#### Fields to ELIMINATE

- `CampaignChannels`
- `Kurt_Id`
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
- `SFB_AccountId`
- `Sales_tip_description_template`
- `Sales_tip_title`
- `TelesalesAgency`

### CustomerCampaignItem__c (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 2
- **Fields used:** 1
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `KSBID__c` | JOIN0 (join) |

#### Fields to ELIMINATE

- `Status__c`
