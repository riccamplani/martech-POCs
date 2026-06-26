# C360_430_-_Logic_Fiber_and_TBB_Newsale_Campaign__05v7Q000000srnWQAQ — Field Usage Report

**Recipe:** C360_430_-_Logic_Fiber_and_TBB_Newsale_Campaign__05v7Q000000srnWQAQ
**Total nodes:** 247

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET7 | Campaign | connectedDataset | 11 | 4 | 7 | 64% |
| LOAD_DATASET13_copy0 | Campaign | connectedDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET16_copy0_copy0_copy0 | CustomerCampaignItem__c | connectedDataset | 12 | 6 | 6 | 50% |
| LOAD_DATASET0 | Fiber TBB Newsale qualified customer | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET11 | Fiber and TBB Potential addresses to sell to | analyticsDataset | 3 | 3 | 0 | 0% |
| LOAD_DATASET10 | Fiber newsalesadress more adresses for a customer | analyticsDataset | 12 | 1 | 11 | 92% |
| LOAD_DATASET8 | Fiber newsalesadresses 1 for a customer | analyticsDataset | 8 | 2 | 6 | 75% |
| LOAD_DATASET1 | Fiber_newsale_qualified_Inbound | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET2 | Fiber_newsale_qualified_Outbound | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET3 | Fiber_newsale_qualified_TM | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET18 | Fiber_newsale_wo_phone_qualified_TM | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET17 | Kunder i Region fiber nysalg | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET4 | TBB_newsale_qualified_Inbound | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET5 | TBB_newsale_qualified_Outbound | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET6 | TBB_newsale_qualified_TM | analyticsDataset | 1 | 1 | 0 | 0% |
| **TOTAL** | | | **78** | **48** | **30** | **38%** |

## Detail per Source Object

### Campaign (`LOAD_DATASET7`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 4
- **Fields unused:** 7

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignID__c` | JOIN14 (join) |
| `Id` | FORMULA21_copy0 (formula), FORMULA22_copy0 (formula) |
| `Name` | FORMULA26_copy0 (formula) |
| `reporting_tag__c` | FORMULA20_copy0 (formula) |

#### Fields to ELIMINATE

- `Campaign_Type_Description__c`
- `Channels__c`
- `EndDate`
- `Product_Type_Description__c`
- `StartDate`
- `Status`
- `Type`

### Campaign (`LOAD_DATASET13_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignID__c` | FILTER40_copy2 (filter), JOIN14 (join) |
| `Id` | JOIN7_copy0 (join), FORMULA21_copy0 (formula), FORMULA22_copy0 (formula) |
| `Name` | FORMULA26_copy0 (formula) |
| `reporting_tag__c` | FORMULA20_copy0 (formula) |

### CustomerCampaignItem__c (`LOAD_DATASET16_copy0_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 12
- **Fields used:** 6
- **Fields unused:** 6

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account__c` | DROP_FIELDS23 (schema), JOIN30 (join) |
| `CampaignID__c` | JOIN14 (join) |
| `Campaign__c` | JOIN7_copy0 (join) |
| `CreatedDate` | FILTER43 (filter) |
| `KurtID__c` | FORMULA20_copy0 (formula), FORMULA23_copy0 (formula) |
| `Personalization_1__c` | DROP_FIELDS24 (schema), APPEND19 (appendV2), APPEND65 (appendV2) |

#### Fields to ELIMINATE

- `CampaignName__c`
- `Campaign_Channels__c`
- `KSBID__c`
- `Salestip_Template__c`
- `Status__c`
- `tm_agency__c`

### Fiber TBB Newsale qualified customer (`LOAD_DATASET0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CangetFib1.HavenotIA.SEogAgrol.Company_Family_Name__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.DPSS_Portfolio__c` | DROP_FIELDS1 (schema), FILTER7 (filter) |
| `CangetFib1.HavenotIA.SEogAgrol.DPSS_Segment__c` | DROP_FIELDS1 (schema), FILTER7 (filter), FILTER36 (filter), APPEND54 (appendV2), APPEND18 (appendV2) +10 more |
| `CangetFib1.HavenotIA.SEogAgrol.Has_Subscriptions_Actual__c` | FILTER4 (filter), FILTER5 (filter), APPEND54 (appendV2), FILTER4_copy0 (filter), FILTER5_copy0 (filter) +15 more |
| `CangetFib1.HavenotIA.SEogAgrol.Has_Subscriptions__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `CangetFib1.HavenotIA.SEogAgrol.Id` | DROP_FIELDS1 (schema), JOIN0 (join), JOIN1 (join), JOIN2 (join), JOIN3 (join) +38 more |
| `CangetFib1.HavenotIA.SEogAgrol.Industry__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.KurtID__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.Mobile_Voice_Penetration__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.NACE_Subclass_Code__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.NumberOfEmployees` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.Segment__c` | DROP_FIELDS1 (schema), APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2) +8 more |
| `CangetFib1.HavenotIA.SEogAgrol.SubsMobileVoice__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `CangetFib1.HavenotIA.SEogAgrol.TSP_Dealer__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Capacity_code__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Coverage_4GP40__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Coverage_4G_Plus__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Coverage_4G__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Coverage_5G_P__c` | APPEND54 (appendV2), APPEND18 (appendV2), APPEND49 (appendV2), APPEND50 (appendV2), APPEND51 (appendV2) +7 more |
| `Fiber_cost__c` | FILTER0 (filter), FILTER1 (filter), FILTER2 (filter), FILTER3 (filter), APPEND54 (appendV2) +11 more |

### Fiber and TBB Potential addresses to sell to (`LOAD_DATASET11`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 3
- **Fields used:** 3
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Antall_Lokasjoner_mersalg_TBB` | FORMULA40 (formula) |
| `Antall_lokasjoner_mersalg_fiber` | FORMULA40 (formula) |
| `Location_Owner__c` | DROP_FIELDS15 (schema), JOIN18 (join), JOIN21 (join), JOIN26 (join), JOIN27 (join) +3 more |

### Fiber newsalesadress more adresses for a customer (`LOAD_DATASET10`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 12
- **Fields used:** 1
- **Fields unused:** 11

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Location_Owner__c` | JOIN17 (join), JOIN18 (join) |

#### Fields to ELIMINATE

- `Adresse1.Adresse1`
- `Adresse10.Adresse10`
- `Adresse2.Adresse2`
- `Adresse3.Adresse3`
- `Adresse4.Adresse4`
- `Adresse5.Adresse5`
- `Adresse6.Adresse6`
- `Adresse7.Adresse7`
- `Adresse8.Adresse8`
- `Adresse9.Adresse9`
- `Text_adress_1`

### Fiber newsalesadresses 1 for a customer (`LOAD_DATASET8`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 2
- **Fields unused:** 6

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `IA_full_new_sale_text_adresses` | DROP_FIELDS7_copy0 (schema), FORMULA28_copy0 (formula) |
| `Location_Owner__c` | JOIN15 (join), JOIN17 (join), JOIN18 (join) |

#### Fields to ELIMINATE

- `Capacity_code__c`
- `Coverage_4GP40__c`
- `Coverage_4G_Plus__c`
- `Coverage_4G__c`
- `Coverage_5G_P__c`
- `Fiber_cost__c`

### Fiber_newsale_qualified_Inbound (`LOAD_DATASET1`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_Fiber_Inbound` | JOIN0 (join), JOIN2 (join), JOIN19 (join), APPEND2 (appendV2), APPEND60 (appendV2) +3 more |

### Fiber_newsale_qualified_Outbound (`LOAD_DATASET2`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_Fiber_Outbound` | JOIN4 (join), JOIN6 (join), APPEND2 (appendV2), JOIN25 (join), APPEND4 (appendV2) +2 more |

### Fiber_newsale_qualified_TM (`LOAD_DATASET3`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_Fiber_TM` | JOIN8 (join), JOIN20 (join), JOIN32 (join), JOIN33 (join), JOIN21 (join) +10 more |

### Fiber_newsale_wo_phone_qualified_TM (`LOAD_DATASET18`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_Fiber_TM_wo_phone` | JOIN34 (join), DROP_FIELDS26_copy0 (schema) |

### Kunder i Region fiber nysalg (`LOAD_DATASET17`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account_Region` | JOIN31 (join), JOIN32 (join), APPEND64 (appendV2) |

### TBB_newsale_qualified_Inbound (`LOAD_DATASET4`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_TBB_Inbound` | JOIN1 (join), JOIN3 (join), JOIN23 (join), APPEND13 (appendV2), APPEND61 (appendV2) +1 more |

### TBB_newsale_qualified_Outbound (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_TBB_Outbound` | JOIN5 (join), JOIN7 (join), APPEND13 (appendV2), APPEND15 (appendV2) |

### TBB_newsale_qualified_TM (`LOAD_DATASET6`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_Qualified_TBB_TM` | JOIN11 (join), FORMULA5_copy0_copy0_copy0 (computeRelative), FORMULA6_copy0_copy0_copy0 (computeRelative), APPEND16 (appendV2), APPEND15 (appendV2) |
