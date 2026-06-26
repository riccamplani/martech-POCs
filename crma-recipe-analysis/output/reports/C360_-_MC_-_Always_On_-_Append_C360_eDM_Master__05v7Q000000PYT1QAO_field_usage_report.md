# C360_-_MC_-_Always_On_-_Append_C360_eDM_Master__05v7Q000000PYT1QAO — Field Usage Report

**Recipe:** C360_-_MC_-_Always_On_-_Append_C360_eDM_Master__05v7Q000000PYT1QAO
**Total nodes:** 16

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET7 | C360 - MC - Always On - Fiber nysalg - Har fiber gjennom utleier_3.part | analyticsDataset | 11 | 11 | 0 | 0% |
| LOAD_DATASET3 | C360 - MC - Always On - Nysalg Fiber ved ikke svar | analyticsDataset | 13 | 13 | 0 | 0% |
| LOAD_DATASET1 | C360 - MC - Always On - Onboarding new Mobil Tale kunde | analyticsDataset | 16 | 16 | 0 | 0% |
| LOAD_DATASET5 | C360 - MC - Always On - Onboarding new SZMobil kunde oppsalg oppdatert | analyticsDataset | 15 | 15 | 0 | 0% |
| LOAD_DATASET6 | C360 - MC - Always On - Onboarding new SafeZoneMobil kunde | analyticsDataset | 18 | 18 | 0 | 0% |
| LOAD_DATASET4 | C360 - MC - Always On - Rebinding Fiber ved ikke svar | analyticsDataset | 13 | 13 | 0 | 0% |
| LOAD_DATASET8 | C360 - MC - Always On - Velkomstprogram nye medlemmer Forbund | analyticsDataset | 12 | 12 | 0 | 0% |
| LOAD_DATASET0 | C360 eDM Master | analyticsDataset | 30 | 19 | 11 | 37% |
| **TOTAL** | | | **128** | **117** | **11** | **9%** |

## Detail per Source Object

### C360 - MC - Always On - Fiber nysalg - Har fiber gjennom utleier_3.part (`LOAD_DATASET7`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 11
- **Fields used:** 11
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account.SEogAgrol.Id` | APPEND5 (appendV2) |
| `Account.SEogAgrol.KurtID__c` | APPEND5 (appendV2) |
| `C360_96.CampaignName` | APPEND5 (appendV2) |
| `C360_96.Id` | APPEND5 (appendV2) |
| `Campaign_cd` | APPEND5 (appendV2) |
| `Personalization_1__c` | APPEND5 (appendV2), APPEND6 (appendV2) |
| `PrimaryCon.Email` | APPEND5 (appendV2) |
| `PrimaryCon.Id` | APPEND5 (appendV2) |
| `PrimaryCon.MobilePhone` | APPEND5 (appendV2) |
| `Send_timestamp` | APPEND5 (appendV2), APPEND6 (appendV2) |
| `Send_timestamp_string` | APPEND5 (appendV2), APPEND6 (appendV2) |

### C360 - MC - Always On - Nysalg Fiber ved ikke svar (`LOAD_DATASET3`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 13
- **Fields used:** 13
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Account.Id` | APPEND4 (appendV2) |
| `Account.KurtID__c` | APPEND4 (appendV2) |
| `C360_96.CampaignName` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `C360_96.Id` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `Campaign_cd` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `Personalization_1__c` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `Personalization_2__c` | APPEND4 (appendV2), APPEND6 (appendV2) |
| `Personalization_3__c` | APPEND4 (appendV2) |
| `PrimaryCon.Email` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `PrimaryCon.Id` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `PrimaryCon.MobilePhone` | APPEND4 (appendV2), APPEND5 (appendV2) |
| `Send_timestamp` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `Send_timestamp_string` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |

### C360 - MC - Always On - Onboarding new Mobil Tale kunde (`LOAD_DATASET1`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 16
- **Fields used:** 16
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Primarymed.Email` | APPEND0 (appendV2) |
| `Primarymed.Id` | APPEND0 (appendV2) |
| `Primarymed.MobilePhone` | APPEND0 (appendV2) |
| `Send_timestamp` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Send_timestamp_string` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Transform1.CampaignCD` | APPEND0 (appendV2) |
| `Transform1.Personalization_1__c` | APPEND0 (appendV2) |
| `Transform1.Personalization_20__c` | APPEND0 (appendV2) |
| `Transform1.Personalization_2__c` | APPEND0 (appendV2) |
| `Transform1.Personalization_3__c` | APPEND0 (appendV2) |
| `Transform1.Personalization_4__c` | APPEND0 (appendV2) |
| `Transform1.Personalization_5__c` | APPEND0 (appendV2) |
| `Transform1.Transform1.CampaignName` | APPEND0 (appendV2) |
| `Transform1.Transform1.Id` | APPEND0 (appendV2) |
| `Transform1.Transform7.Id` | APPEND0 (appendV2) |
| `Transform1.Transform7.KurtID__c` | APPEND0 (appendV2) |

### C360 - MC - Always On - Onboarding new SZMobil kunde oppsalg oppdatert (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 15
- **Fields used:** 15
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `C360_143.Id` | APPEND2 (appendV2) |
| `C360_143.Name` | APPEND2 (appendV2) |
| `Campaign_CD` | APPEND2 (appendV2), APPEND6 (appendV2) |
| `Id` | APPEND2 (appendV2), APPEND6 (appendV2) |
| `KurtID__c` | APPEND2 (appendV2), APPEND6 (appendV2) |
| `Personaliz.Personalization_5__c` | APPEND2 (appendV2) |
| `Personalization_1__c` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `Personalization_2__c` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND6 (appendV2) |
| `Personalization_3__c` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) |
| `Personalization_4__c` | APPEND2 (appendV2) |
| `PrimaryCon.Email` | APPEND2 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) |
| `PrimaryCon.Id` | APPEND2 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) |
| `PrimaryCon.MobilePhone` | APPEND2 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) |
| `Send_timestamp` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `Send_timestamp_string` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |

### C360 - MC - Always On - Onboarding new SafeZoneMobil kunde (`LOAD_DATASET6`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 18
- **Fields used:** 18
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountID` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `CampaignID` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `CampaignName` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `ContactID` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `Email` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `KurtID` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `MobilePhone` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `Send_timestamp` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `Send_timestamp_string` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `Transform9.CampaignCD` | APPEND1 (appendV2) |
| `Transform9.Personalization_7__c` | APPEND1 (appendV2) |
| `Transform9.Personalization_8` | APPEND1 (appendV2) |
| `Transform9.Transform8.Personalization_4__c` | APPEND1 (appendV2) |
| `Transform9.Transform8.aftersuppr.Transform7.Personalization_1__c` | APPEND1 (appendV2) |
| `Transform9.Transform8.aftersuppr.Transform7.Personalization_2__c` | APPEND1 (appendV2) |
| `Transform9.Transform8.aftersuppr.Transform7.Personalization_3__c` | APPEND1 (appendV2) |
| `Transform9.Transform8.aftersuppr.Transform7.Personalization_5__c` | APPEND1 (appendV2) |
| `Transform9.Transform8.aftersuppr.Transform7.Personalization_6__c` | APPEND1 (appendV2) |

### C360 - MC - Always On - Rebinding Fiber ved ikke svar (`LOAD_DATASET4`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 13
- **Fields used:** 13
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Beregnedef.Account.Id` | APPEND3 (appendV2) |
| `Beregnedef.Account.KurtID__c` | APPEND3 (appendV2) |
| `Beregnedef.C360_96.CampaignName` | APPEND3 (appendV2) |
| `Beregnedef.C360_96.Id` | APPEND3 (appendV2) |
| `Beregnedef.Campaign_cd` | APPEND3 (appendV2) |
| `Beregnedef.PrimaryCon.Email` | APPEND3 (appendV2) |
| `Beregnedef.PrimaryCon.Id` | APPEND3 (appendV2) |
| `Beregnedef.PrimaryCon.MobilePhone` | APPEND3 (appendV2) |
| `Beregnedef.Send_timestamp` | APPEND3 (appendV2) |
| `Beregnedef.Send_timestamp_string` | APPEND3 (appendV2) |
| `Join8.Personalization_2__c` | APPEND3 (appendV2) |
| `Join8.Personalization_3__c` | APPEND3 (appendV2) |
| `Personalization_1__c` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |

### C360 - MC - Always On - Velkomstprogram nye medlemmer Forbund (`LOAD_DATASET8`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 12
- **Fields used:** 12
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `C360_44.Id` | APPEND6 (appendV2) |
| `C360_44.Name` | APPEND6 (appendV2) |
| `Campaign_CD` | APPEND6 (appendV2) |
| `Id` | APPEND6 (appendV2) |
| `KurtID__c` | APPEND6 (appendV2) |
| `Personalization_1` | APPEND6 (appendV2) |
| `Personalization_2` | APPEND6 (appendV2) |
| `Send_timestamp` | APPEND6 (appendV2) |
| `Send_timestamp_string` | APPEND6 (appendV2) |
| `UniqueCont.Email` | APPEND6 (appendV2) |
| `UniqueCont.Id` | APPEND6 (appendV2) |
| `UniqueCont.MobilePhone` | APPEND6 (appendV2) |

### C360 eDM Master (`LOAD_DATASET0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 30
- **Fields used:** 19
- **Fields unused:** 11

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `AccountID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `CampaignCD` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `CampaignID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `CampaignName` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `ContactID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Email` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `KurtID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `MobilePhone` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Personalization_1__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Personalization_20__c` | APPEND0 (appendV2) |
| `Personalization_2__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +1 more |
| `Personalization_3__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) |
| `Personalization_4__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2) |
| `Personalization_5__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2) |
| `Personalization_6__c` | APPEND1 (appendV2) |
| `Personalization_7__c` | APPEND1 (appendV2) |
| `Personalization_8__c` | APPEND1 (appendV2) |
| `Send_timestamp` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Send_timestamp_string` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |

#### Fields to ELIMINATE

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
- `Personalization_9__c`
