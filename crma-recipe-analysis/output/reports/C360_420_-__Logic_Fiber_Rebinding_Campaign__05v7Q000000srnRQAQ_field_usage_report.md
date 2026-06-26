# C360_420_-__Logic_Fiber_Rebinding_Campaign__05v7Q000000srnRQAQ — Field Usage Report

**Recipe:** C360_420_-__Logic_Fiber_Rebinding_Campaign__05v7Q000000srnRQAQ
**Total nodes:** 82

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET11 | Campaign | connectedDataset | 11 | 4 | 7 | 64% |
| LOAD_DATASET17 | Fiber Rebinding Flere Lokasjoner | analyticsDataset | 13 | 13 | 0 | 0% |
| LOAD_DATASET19 | Fiber Rebinding customers DPSS Medium Silje | analyticsDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET20 | Fiber Rebinding customers Kundeservice DPSS Small og Medium | analyticsDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET21 | Fiber Rebinding customers TM DPSS Small | analyticsDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET22 | Fiber Rebinding customers TSP DPSS Small | analyticsDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET10 | Fiber Rebinding subscription Refine | analyticsDataset | 6 | 4 | 2 | 33% |
| LOAD_DATASET16 | Fiber Rebinding Øvrige Rebindinger | analyticsDataset | 13 | 13 | 0 | 0% |
| LOAD_DATASET23 | Fiber newsalesadress more adresses for a customer | analyticsDataset | 12 | 1 | 11 | 92% |
| LOAD_DATASET12 | Fiber newsalesadresses 1 for a customer | analyticsDataset | 2 | 2 | 0 | 0% |
| LOAD_DATASET18 | Fiber rebinding Mersalgspotensiale | analyticsDataset | 13 | 13 | 0 | 0% |
| **TOTAL** | | | **78** | **58** | **20** | **26%** |

## Detail per Source Object

### Campaign (`LOAD_DATASET11`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 11
- **Fields used:** 4
- **Fields unused:** 7

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `CampaignID__c` | JOIN5 (join) |
| `Id` | FORMULA21 (formula), FORMULA22 (formula) |
| `Name` | FORMULA26 (formula) |
| `reporting_tag__c` | FORMULA20 (formula) |

#### Fields to ELIMINATE

- `Campaign_Type_Description__c`
- `Channels__c`
- `EndDate`
- `Product_Type_Description__c`
- `StartDate`
- `Status`
- `Type`

### Fiber Rebinding Flere Lokasjoner (`LOAD_DATASET17`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 13
- **Fields used:** 13
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Antall_lokasjoner_IA_mulighet` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `CAMPAIGN_CD` | APPEND11 (appendV2), APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) |
| `CAMPAIGN_CD_TSP_KSI` | APPEND11 (appendV2), APPEND12 (appendV2), FORMULA30 (formula) |
| `Campaign_text_lokasjoner` | APPEND11 (appendV2) |
| `Campaign_text_oppsalg_fase12_mersalg` | APPEND11 (appendV2) |
| `Fiber_rebinding_fase` | APPEND11 (appendV2), APPEND12 (appendV2), FILTER36 (filter), FILTER37 (filter) |
| `Fibernewsa.IA_full_new_sale_text_adresses` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Have_more_locations` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Kampanjegruppe` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Personalization_2__c` | APPEND11 (appendV2), APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema), FORMULA32 (formula) +1 more |
| `Prisgruppe_fiber_rebinding` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Sum_wifi_mobilbackup_sz` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `have1fiber.Transform1.Id` | APPEND11 (appendV2), APPEND12 (appendV2), JOIN3 (join), JOIN4 (join), DROP_FIELDS14 (schema) +3 more |

### Fiber Rebinding customers DPSS Medium Silje (`LOAD_DATASET19`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN3 (join), APPEND10 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), FORMULA21 (formula) +1 more |
| `KurtID__c` | APPEND10 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), FORMULA20 (formula), FORMULA23 (formula) |

### Fiber Rebinding customers Kundeservice DPSS Small og Medium (`LOAD_DATASET20`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN0 (join), APPEND9 (appendV2), FORMULA21 (formula), FORMULA22 (formula) |
| `KurtID__c` | APPEND9 (appendV2), FORMULA20 (formula), FORMULA23 (formula) |

### Fiber Rebinding customers TM DPSS Small (`LOAD_DATASET21`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Transform2.Id` | JOIN4 (join), FORMULA5_copy0 (computeRelative), FORMULA6_copy0 (computeRelative), APPEND7 (appendV2), APPEND8 (appendV2) +1 more |
| `Transform2.KurtID__c` | APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2) |

### Fiber Rebinding customers TSP DPSS Small (`LOAD_DATASET22`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Id` | JOIN8 (join), APPEND10 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), FORMULA21 (formula) +1 more |
| `KurtID__c` | APPEND10 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), FORMULA20 (formula), FORMULA23 (formula) |

### Fiber Rebinding subscription Refine (`LOAD_DATASET10`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 6
- **Fields used:** 4
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | DROP_FIELDS9 (schema) |
| `Main_number__c` | DROP_FIELDS9 (schema), FILTER39 (filter) |
| `Name` | DROP_FIELDS9 (schema) |
| `Sub_Owner__c` | DROP_FIELDS9 (schema), FORMULA29 (formula) |

#### Fields to ELIMINATE

- `Bandwidth__c`
- `FIBER_MONTHLY_FEE__c`

### Fiber Rebinding Øvrige Rebindinger (`LOAD_DATASET16`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 13
- **Fields used:** 13
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Antall_lokasjoner_IA_mulighet` | APPEND12 (appendV2) |
| `CAMPAIGN_CD` | APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) |
| `CAMPAIGN_CD_TSP_KSI` | APPEND12 (appendV2), FORMULA30 (formula) |
| `Campaign_text_oppsalg_fase12_rest` | APPEND12 (appendV2), FORMULA31 (formula) |
| `Campaign_text_rebinding_andre` | APPEND12 (appendV2) |
| `Fiber_rebinding_fase` | APPEND12 (appendV2), FILTER36 (filter), FILTER37 (filter) |
| `Fibernewsa.IA_full_new_sale_text_adresses` | APPEND12 (appendV2) |
| `Have_more_locations` | APPEND12 (appendV2) |
| `Kampanjegruppe` | APPEND12 (appendV2) |
| `Personalization_2__c` | APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema), FORMULA32 (formula), DROP_FIELDS16 (schema) |
| `Prisgruppe_fiber_rebinding` | APPEND12 (appendV2) |
| `Sum_wifi_mobilbackup_sz` | APPEND12 (appendV2) |
| `have1fiber.Transform1.Id` | APPEND12 (appendV2), JOIN3 (join), JOIN4 (join), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) +2 more |

### Fiber newsalesadress more adresses for a customer (`LOAD_DATASET23`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 12
- **Fields used:** 1
- **Fields unused:** 11

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Location_Owner__c` | JOIN9 (join) |

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

### Fiber newsalesadresses 1 for a customer (`LOAD_DATASET12`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 2
- **Fields used:** 2
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `IA_full_new_sale_text_adresses` | FORMULA28 (formula) |
| `Location_Owner__c` | JOIN7 (join), JOIN9 (join) |

### Fiber rebinding Mersalgspotensiale (`LOAD_DATASET18`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 13
- **Fields used:** 13
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Antall_lokasjoner_IA_mulighet` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `CAMPAIGN_CD` | APPEND11 (appendV2), APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema) |
| `CAMPAIGN_CD_TSP_KSI` | APPEND11 (appendV2), APPEND12 (appendV2), FORMULA30 (formula) |
| `Campaign_text_oppsalg_fase12_rest` | APPEND11 (appendV2), APPEND12 (appendV2), FORMULA31 (formula) |
| `Campaign_text_rebinding_mersalg` | APPEND11 (appendV2), APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema), FORMULA27 (formula) |
| `Fiber_rebinding_fase` | APPEND11 (appendV2), APPEND12 (appendV2), FILTER36 (filter), FILTER37 (filter) |
| `Fibernewsa.IA_full_new_sale_text_adresses` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Have_more_locations` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Kampanjegruppe` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Personalization_2__c` | APPEND11 (appendV2), APPEND12 (appendV2), DROP_FIELDS14 (schema), DROP_FIELDS15 (schema), FORMULA32 (formula) +1 more |
| `Prisgruppe_fiber_rebinding` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `Sum_wifi_mobilbackup_sz` | APPEND11 (appendV2), APPEND12 (appendV2) |
| `have1fiber.Transform1.Id` | APPEND11 (appendV2), APPEND12 (appendV2), JOIN3 (join), JOIN4 (join), DROP_FIELDS14 (schema) +3 more |
