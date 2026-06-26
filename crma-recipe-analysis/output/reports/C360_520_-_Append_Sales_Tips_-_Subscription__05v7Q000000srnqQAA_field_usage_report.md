# C360_520_-_Append_Sales_Tips_-_Subscription__05v7Q000000srnqQAA — Field Usage Report

**Recipe:** C360_520_-_Append_Sales_Tips_-_Subscription__05v7Q000000srnqQAA
**Total nodes:** 16

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET5 | C360 420 Fiber Rebinding Subscription | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET9 | C360 421 Migrasjon TBB til Fiber Subscription | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET2 | C360 440 Rebinding Mobile Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET4 | C360 460 Vekst to Verdi Campaign Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET6 | C360 470 Rebinding Mobile Red Group Pilot Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET7 | C360 480 Rebinding Forbund Mobile Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET8 | C360 491 - Mobile Voice Rebinding Agrol Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| LOAD_DATASET10 | C360 496 - Pilot SafeZone og Oppdatert bundle - Subscriptions | analyticsDataset | 4 | 4 | 0 | 0% |
| **TOTAL** | | | **32** | **32** | **0** | **0%** |

## Detail per Source Object

### C360 420 Fiber Rebinding Subscription (`LOAD_DATASET5`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Main_number__c` | APPEND0 (appendV2), APPEND6 (appendV2) |
| `Name` | APPEND0 (appendV2), APPEND6 (appendV2) |
| `Subscription_Owner` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |

### C360 421 Migrasjon TBB til Fiber Subscription (`LOAD_DATASET9`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND5 (appendV2), APPEND6 (appendV2) |
| `Join2.Main_number__c` | APPEND5 (appendV2) |
| `Join2.Name` | APPEND5 (appendV2) |
| `Join2.Sub_Owner__c` | APPEND5 (appendV2) |

### C360 440 Rebinding Mobile Subscriptions (`LOAD_DATASET2`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `FILTER7.Main_number__c` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `FILTER7.Name` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |
| `Subscription_Owner` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +2 more |

### C360 460 Vekst to Verdi Campaign Subscriptions (`LOAD_DATASET4`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |
| `MobileVoic.Main_number__c` | APPEND1 (appendV2) |
| `MobileVoic.Name` | APPEND1 (appendV2) |
| `Subscription_Owner` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +1 more |

### C360 470 Rebinding Mobile Red Group Pilot Subscriptions (`LOAD_DATASET6`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Main_number__c` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Name` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `Subscription_Owner` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |

### C360 480 Rebinding Forbund Mobile Subscriptions (`LOAD_DATASET7`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Main_number__c` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Name` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Sub_Owner__c` | APPEND3 (appendV2), APPEND4 (appendV2) |

### C360 491 - Mobile Voice Rebinding Agrol Subscriptions (`LOAD_DATASET8`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Main_number__c` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Name` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) |
| `FILTER7.Sub_Owner__c` | APPEND4 (appendV2) |

### C360 496 - Pilot SafeZone og Oppdatert bundle - Subscriptions (`LOAD_DATASET10`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 4
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | APPEND6 (appendV2) |
| `Main_number__c` | APPEND6 (appendV2) |
| `Name` | APPEND6 (appendV2) |
| `Subscription_Owner` | APPEND6 (appendV2) |
