# C360_630_-_Update_Sales_Tips_-_Personalization_fields__05v7Q000000sro5QAA — Field Usage Report

**Recipe:** C360_630_-_Update_Sales_Tips_-_Personalization_fields__05v7Q000000sro5QAA
**Total nodes:** 54

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET5 | C360 510 New Sales Tips | analyticsDataset | 27 | 22 | 5 | 19% |
| LOAD_DATASET4 | CustomerCampaignItem__c | connectedDataset | 28 | 24 | 4 | 14% |
| **TOTAL** | | | **55** | **46** | **9** | **16%** |

## Detail per Source Object

### C360 510 New Sales Tips (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 27
- **Fields used:** 22
- **Fields unused:** 5

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `KSBID_2` | JOIN2 (join) |
| `Personalization_10__c` | FORMULA10_copy0_copy1 (formula) |
| `Personalization_11__c` | FORMULA11_copy1 (formula) |
| `Personalization_12__c` | FORMULA12_copy1 (formula) |
| `Personalization_13__c` | FORMULA13_copy1 (formula) |
| `Personalization_14__c` | FORMULA14_copy1 (formula) |
| `Personalization_15__c` | FORMULA15_copy1 (formula) |
| `Personalization_16__c` | FORMULA16_copy1 (formula) |
| `Personalization_17__c` | FORMULA17_copy1 (formula) |
| `Personalization_18__c` | FORMULA18_copy1 (formula) |
| `Personalization_19__c` | FORMULA19_copy1 (formula) |
| `Personalization_1__c` | FORMULA1_copy0_copy0_copy0_copy1 (formula) |
| `Personalization_20__c` | FORMULA20_copy1 (formula) |
| `Personalization_2__c` | FORMULA2_copy0_copy0_copy1 (formula) |
| `Personalization_3__c` | FORMULA3_copy0_copy0_copy1 (formula) |
| `Personalization_4__c` | FORMULA4_copy0_copy0_copy1 (formula) |
| `Personalization_5__c` | FORMULA5_copy0_copy0_copy1 (formula) |
| `Personalization_6__c` | FORMULA6_copy0_copy0_copy1 (formula) |
| `Personalization_7__c` | FORMULA7_copy0_copy0_copy1 (formula) |
| `Personalization_8__c` | FORMULA8_copy0_copy0_copy1 (formula) |
| `Personalization_9__c` | FORMULA9_copy0_copy1 (formula) |
| `Sales_tip_description_template` | FORMULA23 (formula), DROP_FIELDS5 (schema) |

#### Fields to ELIMINATE

- `AccountCampaignID`
- `Kurt_Id`
- `SFB_AccountId`
- `SFB_CampainId`
- `Sales_tip_title`

### CustomerCampaignItem__c (`LOAD_DATASET4`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 28
- **Fields used:** 24
- **Fields unused:** 4

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | DROP_FIELDS4 (schema) |
| `KSBID__c` | DROP_FIELDS4 (schema), JOIN2 (join) |
| `Personalization_10__c` | FORMULA10_copy0 (formula) |
| `Personalization_11__c` | FORMULA11 (formula) |
| `Personalization_12__c` | FORMULA12 (formula) |
| `Personalization_13__c` | FORMULA13 (formula) |
| `Personalization_14__c` | FORMULA14 (formula) |
| `Personalization_15__c` | FORMULA15 (formula) |
| `Personalization_16__c` | FORMULA16 (formula) |
| `Personalization_17__c` | FORMULA17 (formula) |
| `Personalization_18__c` | FORMULA18 (formula) |
| `Personalization_19__c` | FORMULA19 (formula) |
| `Personalization_1__c` | FORMULA1_copy0_copy0_copy0 (formula) |
| `Personalization_20__c` | FORMULA20 (formula) |
| `Personalization_2__c` | FORMULA2_copy0_copy0 (formula) |
| `Personalization_3__c` | FORMULA3_copy0_copy0 (formula) |
| `Personalization_4__c` | FORMULA4_copy0_copy0 (formula) |
| `Personalization_5__c` | FORMULA5_copy0_copy0 (formula) |
| `Personalization_6__c` | FORMULA6_copy0_copy0 (formula) |
| `Personalization_7__c` | FORMULA7_copy0_copy0 (formula) |
| `Personalization_8__c` | FORMULA8_copy0_copy0 (formula) |
| `Personalization_9__c` | FORMULA9_copy0 (formula) |
| `Response_Code__c` | DROP_FIELDS4 (schema) |
| `Salestip_Template__c` | DROP_FIELDS4 (schema), FORMULA23 (formula) |

#### Fields to ELIMINATE

- `CreatedDate`
- `Reason_Sub_code__c`
- `Response_Date__c`
- `Status__c`
