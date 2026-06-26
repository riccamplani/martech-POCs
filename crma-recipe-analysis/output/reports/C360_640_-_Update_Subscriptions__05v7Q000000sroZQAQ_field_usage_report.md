# C360_640_-_Update_Subscriptions__05v7Q000000sroZQAQ — Field Usage Report

**Recipe:** C360_640_-_Update_Subscriptions__05v7Q000000sroZQAQ
**Total nodes:** 10

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET2 | C360 520 Subscriptions | analyticsDataset | 4 | 2 | 2 | 50% |
| LOAD_DATASET1 | Subscription__c | connectedDataset | 4 | 3 | 1 | 25% |
| **TOTAL** | | | **8** | **5** | **3** | **38%** |

## Detail per Source Object

### C360 520 Subscriptions (`LOAD_DATASET2`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 4
- **Fields used:** 2
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | FORMULA1 (formula), FORMULA2 (formula) |
| `FILTER7.Main_number__c` | JOIN0 (join) |

#### Fields to ELIMINATE

- `FILTER7.Name`
- `Subscription_Owner`

### Subscription__c (`LOAD_DATASET1`)

- **Connection:** SFDC_LOCAL_SEGMENTATION
- **Fields loaded:** 4
- **Fields used:** 3
- **Fields unused:** 1

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_sensitive__c` | FORMULA1 (formula), FORMULA2 (formula) |
| `Id` | DROP_FIELDS0 (schema) |
| `Main_number__c` | JOIN0 (join) |

#### Fields to ELIMINATE

- `Sub_Owner__c`
