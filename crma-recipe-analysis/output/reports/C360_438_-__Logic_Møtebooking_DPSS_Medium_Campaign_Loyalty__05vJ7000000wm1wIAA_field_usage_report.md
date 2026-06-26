# C360_438_-__Logic_Møtebooking_DPSS_Medium_Campaign_Loyalty__05vJ7000000wm1wIAA — Field Usage Report

**Recipe:** C360_438_-__Logic_Møtebooking_DPSS_Medium_Campaign_Loyalty__05vJ7000000wm1wIAA
**Total nodes:** 42

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET13 | Campaign | connectedDataset | 4 | 2 | 2 | 50% |
| LOAD_DATASET17_copy0 | Case nysalg Fiber TBB open | analyticsDataset | 1 | 1 | 0 | 0% |
| LOAD_DATASET16_copy0_copy0 | CustomerCampaignItem__c | connectedDataset | 13 | 10 | 3 | 23% |
| LOAD_DATASET11_copy0 | Fiber and TBB Potential addresses to sell to | analyticsDataset | 3 | 3 | 0 | 0% |
| LOAD_DATASET14 | Fiber newsalesadress more adresses for a customer | analyticsDataset | 12 | 1 | 11 | 92% |
| LOAD_DATASET15 | Fiber newsalesadresses 1 for a customer | analyticsDataset | 9 | 2 | 7 | 78% |
| **TOTAL** | | | **42** | **19** | **23** | **55%** |

## Detail per Source Object

### Campaign (`LOAD_DATASET13`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 2
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignID__c` | FILTER40 (filter) |
| `Id` | JOIN7 (join) |

#### Fields to ELIMINATE

- `Name`
- `reporting_tag__c`

### Case nysalg Fiber TBB open (`LOAD_DATASET17_copy0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 1
- **Fields used:** 1
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Key_suppression_open_Case_fiber_tbb_newsale` | JOIN14 (join) |

### CustomerCampaignItem__c (`LOAD_DATASET16_copy0_copy0`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 13
- **Fields used:** 10
- **Fields unused:** 3

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account__c` | JOIN14 (join), FORMULA46_copy0_copy0 (formula) |
| `CampaignName__c` | FORMULA48_copy0_copy0 (formula) |
| `Campaign_Channels__c` | DROP_FIELDS18_copy0_copy0 (schema), FORMULA55 (formula) |
| `Campaign__c` | JOIN7 (join), FORMULA45_copy0_copy0 (formula) |
| `KSBID__c` | FORMULA44_copy0_copy0 (formula) |
| `KurtID__c` | FORMULA47_copy0_copy0 (formula) |
| `Personalization_1__c` | DROP_FIELDS18_copy0_copy0 (schema), DROP_FIELDS26 (schema), DROP_FIELDS20 (schema) |
| `Salestip_Template__c` | FORMULA49_copy0_copy0 (formula) |
| `Status__c` | FILTER41_copy0_copy0 (filter) |
| `tm_agency__c` | DROP_FIELDS18_copy0_copy0 (schema), FORMULA56 (formula) |

#### Fields to ELIMINATE

- `CampaignID__c`
- `Reason_Sub_code__c`
- `Response_Code__c`

### Fiber and TBB Potential addresses to sell to (`LOAD_DATASET11_copy0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 3
- **Fields used:** 3
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Antall_Lokasjoner_mersalg_TBB` | FORMULA40_copy0_copy0 (formula) |
| `Antall_lokasjoner_mersalg_fiber` | FORMULA40_copy0_copy0 (formula) |
| `Location_Owner__c` | DROP_FIELDS15_copy0_copy0 (schema), JOIN5 (join), DROP_FIELDS17 (schema), JOIN8 (join) |

### Fiber newsalesadress more adresses for a customer (`LOAD_DATASET14`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 12
- **Fields used:** 1
- **Fields unused:** 11

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Location_Owner__c` | JOIN4 (join), JOIN5 (join), DROP_FIELDS17 (schema), JOIN8 (join) |

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

### Fiber newsalesadresses 1 for a customer (`LOAD_DATASET15`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 9
- **Fields used:** 2
- **Fields unused:** 7

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `IA_full_new_sale_text_adresses` | FORMULA28_copy0_copy0 (formula) |
| `Location_Owner__c` | JOIN4 (join), JOIN5 (join), DROP_FIELDS17 (schema), JOIN8 (join) |

#### Fields to ELIMINATE

- `Capacity_code__c`
- `Coverage_4GP40__c`
- `Coverage_4G_Plus__c`
- `Coverage_4G__c`
- `Coverage_5G_P__c`
- `Fiber_cost__c`
- `Mulig_Installasjonsadresse`
