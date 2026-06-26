# C360_510_-_Append_Sales_Tips_-_Account__05v7Q000000srnlQAA — Field Usage Report

**Recipe:** C360_510_-_Append_Sales_Tips_-_Account__05v7Q000000srnlQAA
**Total nodes:** 62

## Summary

| Load Node | Source Object | Type | Total Fields | Used | Unused | Reduction |
|-----------|--------------|------|-------------|------|--------|-----------|
| LOAD_DATASET7 | C360 410 New Sales Mobile | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET6 | C360 420 Fiber Rebinding Customer | analyticsDataset | 19 | 19 | 0 | 0% |
| LOAD_DATASET19 | C360 421 Migrasjon TBB til Fiber Customer | analyticsDataset | 19 | 19 | 0 | 0% |
| LOAD_DATASET8 | C360 430 Fiber and TBB Newsale Customer | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET22 | C360 431 - Fiber Newsale Feil nummer Customer | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET24 | C360 432 - Oppfølging opportunities fra KS - Fiber og TBB Customer | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET25 | C360 433 - Fiber deepsale Medium Customer | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET32 | C360 434 - Fiber Newsale and deepsale Medium DMU | analyticsDataset | 28 | 28 | 0 | 0% |
| LOAD_DATASET28 | C360 438 -  Møtebooking DPSS Medium Loyalty Customers | analyticsDataset | 20 | 20 | 0 | 0% |
| LOAD_DATASET9 | C360 440 Rebinding Mobile Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET10 | C360 450 New Sales Mobile Agrol | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET12 | C360 460 Vekst to Verdi Campaign Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET20 | C360 461 New Sales Safezone and Oppdatert Customer | analyticsDataset | 9 | 7 | 2 | 22% |
| LOAD_DATASET13 | C360 470 Rebinding Mobile Red Group Pilot Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET16 | C360 480 Rebinding Forbund Mobile Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET15 | C360 490 Førstegangssamtale Small Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET17 | C360 491 - Mobile Voice Rebinding Agrol Customers | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET18 | C360 492 - New Sales MV Daughter Outside Mother Agreement | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET21 | C360 493 - New Sales MV NHO Service og Handel | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET26 | C360 494 New Sales Mobile Dealer | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET27 | C360 495 - Holdback NHO Byggenæringen | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET29 | C360 496 - Pilot SafeZone og Oppdatert bundle - Customers | analyticsDataset | 9 | 9 | 0 | 0% |
| LOAD_DATASET33 | C360 497 - New Sales MV Campaign - Medium | analyticsDataset | 8 | 8 | 0 | 0% |
| LOAD_DATASET30 | C360_439_Møtebooking-pilot Hunter M_Customer | analyticsDataset | 11 | 11 | 0 | 0% |
| LOAD_DATASET0 | SalesTips_structure | analyticsDataset | 21 | 21 | 0 | 0% |
| **TOTAL** | | | **320** | **318** | **2** | **1%** |

## Detail per Source Object

### C360 410 New Sales Mobile (`LOAD_DATASET7`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +19 more |
| `TRANSFORM1.KSBID` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `TRANSFORM1.Kurt_Id` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `TRANSFORM1.SFB_AccountId` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `TRANSFORM1.SFB_CampainId` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `TRANSFORM1.Sales_tip_title` | APPEND1 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +6 more |
| `Telesales_agency` | APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2) +18 more |

### C360 420 Fiber Rebinding Customer (`LOAD_DATASET6`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 19
- **Fields used:** 19
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +20 more |
| `KSBID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +21 more |
| `Kurt_Id` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +19 more |
| `Personalization_10__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_11__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_1__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +5 more |
| `Personalization_2__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +4 more |
| `Personalization_3__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +4 more |
| `Personalization_4__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_5__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_6__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_7__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_8__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_9__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `SFB_AccountId` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +21 more |
| `SFB_CampainId` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +20 more |
| `Sales_tip_description_template` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +19 more |
| `Sales_tip_title` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +19 more |
| `Telesales_agency` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +19 more |

### C360 421 Migrasjon TBB til Fiber Customer (`LOAD_DATASET19`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 19
- **Fields used:** 19
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +9 more |
| `KSBID` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +10 more |
| `Kurt_Id` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +8 more |
| `Personalization_10__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_11__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_1__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +3 more |
| `Personalization_2__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_3__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_4__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_5__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_6__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_7__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_8__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_9__c` | APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `SFB_AccountId` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +10 more |
| `SFB_CampainId` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +9 more |
| `Sales_tip_description_template` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +8 more |
| `Sales_tip_title` | APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +8 more |
| `Telesales_agency` | APPEND11 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +8 more |

### C360 430 Fiber and TBB Newsale Customer (`LOAD_DATASET8`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +18 more |
| `Join14.Append19.Personalization_1__c` | APPEND2 (appendV2) |
| `KSBID` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +19 more |
| `Kurt_Id` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +17 more |
| `Personalization_10__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_11__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_12__c` | APPEND2 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_2__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_3__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_4__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_5__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_6__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_7__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_8__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `Personalization_9__c` | APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +2 more |
| `SFB_AccountId` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +19 more |
| `SFB_CampainId` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +18 more |
| `Sales_tip_description_template` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +17 more |
| `Sales_tip_title` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +17 more |
| `Telesales_agency` | APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2) +17 more |

### C360 431 - Fiber Newsale Feil nummer Customer (`LOAD_DATASET22`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +6 more |
| `KSBID` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +7 more |
| `Kurt_Id` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +5 more |
| `Personalization_10__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_11__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_12__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_1__c` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +2 more |
| `Personalization_2__c` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_3__c` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_4__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_5__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_6__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_7__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_8__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_9__c` | APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `SFB_AccountId` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +7 more |
| `SFB_CampainId` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +6 more |
| `Sales_tip_description_template` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +5 more |
| `Sales_tip_title` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +5 more |
| `Telesales_agency` | APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2) +6 more |

### C360 432 - Oppfølging opportunities fra KS - Fiber og TBB Customer (`LOAD_DATASET24`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +4 more |
| `KSBID` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +5 more |
| `Kurt_Id` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +3 more |
| `Personalization_10__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_11__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_12__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_1__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2) |
| `Personalization_2__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_3__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_4__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_5__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_6__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_7__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_8__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_9__c` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `SFB_AccountId` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +5 more |
| `SFB_CampainId` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +4 more |
| `Sales_tip_title` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +3 more |
| `Sales_tips_description_template` | APPEND16 (appendV2) |
| `Telesales_agency` | APPEND16 (appendV2), APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2) +4 more |

### C360 433 - Fiber deepsale Medium Customer (`LOAD_DATASET25`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +3 more |
| `KSBID` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +4 more |
| `Kurt_Id` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +2 more |
| `Personalization_10__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_11__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_12__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_1__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2) |
| `Personalization_2__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_3__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_4__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_5__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_6__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_7__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_8__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_9__c` | APPEND17 (appendV2), APPEND20 (appendV2), APPEND22 (appendV2) |
| `SFB_AccountId` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +4 more |
| `SFB_CampainId` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +3 more |
| `Sales_tip_description_template` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +2 more |
| `Sales_tip_title` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +2 more |
| `Telesales_agency` | APPEND17 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2) +3 more |

### C360 434 - Fiber Newsale and deepsale Medium DMU (`LOAD_DATASET32`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 28
- **Fields used:** 28
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign.Id` | APPEND22 (appendV2) |
| `KSBID` | APPEND22 (appendV2), APPEND23 (appendV2), FORMULA7 (formula), FORMULA8 (formula) |
| `Output.Campaign_Channels` | APPEND22 (appendV2) |
| `Output.Kurt_Id` | APPEND22 (appendV2) |
| `Output.Personalization_10__c` | APPEND22 (appendV2) |
| `Output.Personalization_11__c` | APPEND22 (appendV2) |
| `Output.Personalization_12__c` | APPEND22 (appendV2) |
| `Output.Personalization_13__c` | APPEND22 (appendV2) |
| `Output.Personalization_14__c` | APPEND22 (appendV2) |
| `Output.Personalization_15__c` | APPEND22 (appendV2) |
| `Output.Personalization_16__c` | APPEND22 (appendV2) |
| `Output.Personalization_17__c` | APPEND22 (appendV2) |
| `Output.Personalization_19__c` | APPEND22 (appendV2) |
| `Output.Personalization_20__c` | APPEND22 (appendV2) |
| `Output.Personalization_2__c` | APPEND22 (appendV2) |
| `Output.Personalization_3__c` | APPEND22 (appendV2) |
| `Output.Personalization_4__c` | APPEND22 (appendV2) |
| `Output.Personalization_5__c` | APPEND22 (appendV2) |
| `Output.Personalization_6__c` | APPEND22 (appendV2) |
| `Output.Personalization_7__c` | APPEND22 (appendV2) |
| `Output.Personalization_8__c` | APPEND22 (appendV2) |
| `Output.Personalization_9__c` | APPEND22 (appendV2) |
| `Output.SFB_AccountId` | APPEND22 (appendV2) |
| `Output.Telesales_agency` | APPEND22 (appendV2) |
| `Personalization_18__c` | APPEND22 (appendV2) |
| `Sales_tip_description_template` | APPEND22 (appendV2), APPEND23 (appendV2) |
| `Sales_tip_title` | APPEND22 (appendV2), APPEND23 (appendV2) |
| `Transform5.Personalization_1__c` | APPEND22 (appendV2) |

### C360 438 -  Møtebooking DPSS Medium Loyalty Customers (`LOAD_DATASET28`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 20
- **Fields used:** 20
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA3 (computeRelative) |
| `KSBID` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA7 (formula) +1 more |
| `Kurt_Id` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2) |
| `Output.Personalization_10__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_11__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_12__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_2__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_3__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_4__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_5__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_6__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_7__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_8__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Output.Personalization_9__c` | APPEND20 (appendV2), APPEND22 (appendV2) |
| `Personalization_1__c` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2) |
| `SFB_AccountId` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FILTER0 (filter) +1 more |
| `SFB_CampainId` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA2 (formula) |
| `Sales_tip_description_template` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2) |
| `Sales_tip_title` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2) |
| `Telesales_agency` | APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA5 (computeRelative) |

### C360 440 Rebinding Mobile Customers (`LOAD_DATASET9`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +17 more |
| `TRANSFORM1.KSBID` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `TRANSFORM1.Kurt_Id` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `TRANSFORM1.SFB_AccountId` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `TRANSFORM1.SFB_CampainId` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `TRANSFORM1.Sales_tip_title` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +5 more |
| `Telesales_agency` | APPEND3 (appendV2), APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2) +16 more |

### C360 450 New Sales Mobile Agrol (`LOAD_DATASET10`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2) +16 more |
| `TRANSFORM1.KSBID` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `TRANSFORM1.Kurt_Id` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `TRANSFORM1.SFB_AccountId` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `TRANSFORM1.SFB_CampainId` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `TRANSFORM1.Sales_tip_title` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2) +4 more |
| `Telesales_agency` | APPEND4 (appendV2), APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2) +15 more |

### C360 460 Vekst to Verdi Campaign Customers (`LOAD_DATASET12`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2) +15 more |
| `TRANSFORM1.KSBID` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `TRANSFORM1.Kurt_Id` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `TRANSFORM1.SFB_AccountId` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `TRANSFORM1.SFB_CampainId` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `TRANSFORM1.Sales_tip_title` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +3 more |
| `Telesales_agency` | APPEND5 (appendV2), APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2) +14 more |

### C360 461 New Sales Safezone and Oppdatert Customer (`LOAD_DATASET20`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 9
- **Fields used:** 7
- **Fields unused:** 2

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +8 more |
| `KSBID` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +9 more |
| `Kurt_Id` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +7 more |
| `SFB_AccountId` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +9 more |
| `SFB_CampainId` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +8 more |
| `Sales_tip_description_template` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +7 more |
| `Sales_tip_title` | APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2) +7 more |

#### Fields to ELIMINATE

- `Id`
- `KurtID__c`

### C360 470 Rebinding Mobile Red Group Pilot Customers (`LOAD_DATASET13`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +14 more |
| `TRANSFORM1.KSBID` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `TRANSFORM1.Kurt_Id` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `TRANSFORM1.SFB_AccountId` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `TRANSFORM1.SFB_CampainId` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `TRANSFORM1.Sales_tip_title` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2) +2 more |
| `Telesales_agency` | APPEND6 (appendV2), APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2) +13 more |

### C360 480 Rebinding Forbund Mobile Customers (`LOAD_DATASET16`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2) +13 more |
| `TRANSFORM1.KSBID` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `TRANSFORM1.Kurt_Id` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `TRANSFORM1.SFB_AccountId` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `TRANSFORM1.SFB_CampainId` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `TRANSFORM1.Sales_tip_description_template` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `TRANSFORM1.Sales_tip_title` | APPEND7 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2) +1 more |
| `Telesales_agency` | APPEND7 (appendV2), APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2) +12 more |

### C360 490 Førstegangssamtale Small Customers (`LOAD_DATASET15`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +12 more |
| `KSBID` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +13 more |
| `Kurt_Id` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +11 more |
| `SFB_AccountId` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +13 more |
| `SFB_CampainId` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +12 more |
| `Sales_tip_description_template` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +11 more |
| `Sales_tip_title` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2) +11 more |
| `Telesales_agency` | APPEND8 (appendV2), APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND13 (appendV2) +11 more |

### C360 491 - Mobile Voice Rebinding Agrol Customers (`LOAD_DATASET17`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2) +11 more |
| `TRANSFORM1.KSBID` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Kurt_Id` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_AccountId` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_CampainId` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_description_template` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_title` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `Telesales_agency` | APPEND9 (appendV2), APPEND10 (appendV2), APPEND11 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2) +10 more |

### C360 492 - New Sales MV Daughter Outside Mother Agreement (`LOAD_DATASET18`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND10 (appendV2), APPEND11 (appendV2), APPEND12 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2) +10 more |
| `TRANSFORM1.KSBID` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Kurt_Id` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_AccountId` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_CampainId` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_description_template` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_title` | APPEND10 (appendV2), APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `Telesales_agency` | APPEND10 (appendV2), APPEND11 (appendV2), APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +9 more |

### C360 493 - New Sales MV NHO Service og Handel (`LOAD_DATASET21`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +7 more |
| `TRANSFORM1.KSBID` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Kurt_Id` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_AccountId` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_CampainId` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_description_template` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_title` | APPEND13 (appendV2), APPEND18 (appendV2), APPEND19 (appendV2) |
| `Telesales_agency` | APPEND13 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2) +7 more |

### C360 494 New Sales Mobile Dealer (`LOAD_DATASET26`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2) +2 more |
| `TRANSFORM1.KSBID` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Kurt_Id` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_AccountId` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.SFB_CampainId` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_description_template` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_title` | APPEND18 (appendV2), APPEND19 (appendV2) |
| `Telesales_agency` | APPEND18 (appendV2), APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2) +2 more |

### C360 495 - Holdback NHO Byggenæringen (`LOAD_DATASET27`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2) +1 more |
| `TRANSFORM1.KSBID` | APPEND19 (appendV2) |
| `TRANSFORM1.Kurt_Id` | APPEND19 (appendV2) |
| `TRANSFORM1.SFB_AccountId` | APPEND19 (appendV2) |
| `TRANSFORM1.SFB_CampainId` | APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_description_template` | APPEND19 (appendV2) |
| `TRANSFORM1.Sales_tip_title` | APPEND19 (appendV2) |
| `Telesales_agency` | APPEND19 (appendV2), APPEND20 (appendV2), APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2) +1 more |

### C360 496 - Pilot SafeZone og Oppdatert bundle - Customers (`LOAD_DATASET29`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 9
- **Fields used:** 9
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA3 (computeRelative) |
| `ExportDefi.KSBID` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `ExportDefi.Kurt_Id` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `ExportDefi.Personalization_1` | APPEND21 (appendV2) |
| `ExportDefi.SFB_AccountId` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `ExportDefi.SFB_CampainId` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `ExportDefi.Sales_tip_description_template` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `ExportDefi.Sales_tip_title` | APPEND21 (appendV2), APPEND23 (appendV2) |
| `Telesales_agency` | APPEND21 (appendV2), APPEND22 (appendV2), APPEND23 (appendV2), FORMULA5 (computeRelative) |

### C360 497 - New Sales MV Campaign - Medium (`LOAD_DATASET33`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 8
- **Fields used:** 8
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `Campaign_Channels` | APPEND23 (appendV2), FORMULA3 (computeRelative) |
| `ExportDefi.KSBID` | APPEND23 (appendV2) |
| `ExportDefi.Kurt_Id` | APPEND23 (appendV2) |
| `ExportDefi.SFB_AccountId` | APPEND23 (appendV2) |
| `ExportDefi.SFB_CampainId` | APPEND23 (appendV2) |
| `ExportDefi.Sales_tip_description_template` | APPEND23 (appendV2) |
| `ExportDefi.Sales_tip_title` | APPEND23 (appendV2) |
| `Telesales_agency` | APPEND23 (appendV2), FORMULA5 (computeRelative) |

### C360_439_Møtebooking-pilot Hunter M_Customer (`LOAD_DATASET30`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 11
- **Fields used:** 11
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `kvalifiser.Campaign_Channels` | APPEND15 (appendV2) |
| `kvalifiser.KSBID` | APPEND15 (appendV2) |
| `kvalifiser.Kurt_Id` | APPEND15 (appendV2) |
| `kvalifiser.Personalization_1__c` | APPEND15 (appendV2) |
| `kvalifiser.Personalization_2__c` | APPEND15 (appendV2) |
| `kvalifiser.Personalization_3__c` | APPEND15 (appendV2) |
| `kvalifiser.SFB_AccountId` | APPEND15 (appendV2) |
| `kvalifiser.SFB_CampainId` | APPEND15 (appendV2) |
| `kvalifiser.Sales_tip_description_template` | APPEND15 (appendV2) |
| `kvalifiser.Sales_tip_title` | APPEND15 (appendV2) |
| `kvalifiser.Telesales_agency` | APPEND15 (appendV2) |

### SalesTips_structure (`LOAD_DATASET0`)

- **Connection:** analyticsDataset (in-org)
- **Fields loaded:** 21
- **Fields used:** 21
- **Fields unused:** 0

#### Fields to KEEP

| Field | Used In |
|-------|---------|
| `KSBID` | APPEND0 (appendV2), APPEND1 (appendV2), APPEND2 (appendV2), APPEND3 (appendV2), APPEND4 (appendV2) +21 more |
| `Personalization_10__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_11__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_12__c` | APPEND2 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2), APPEND17 (appendV2), APPEND20 (appendV2) +1 more |
| `Personalization_13__c` | APPEND22 (appendV2) |
| `Personalization_14__c` | APPEND22 (appendV2) |
| `Personalization_15__c` | APPEND22 (appendV2) |
| `Personalization_16__c` | APPEND22 (appendV2) |
| `Personalization_17__c` | APPEND22 (appendV2) |
| `Personalization_18__c` | APPEND22 (appendV2) |
| `Personalization_19__c` | APPEND22 (appendV2) |
| `Personalization_1__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +5 more |
| `Personalization_20__c` | APPEND22 (appendV2) |
| `Personalization_2__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +4 more |
| `Personalization_3__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND15 (appendV2) +4 more |
| `Personalization_4__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_5__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_6__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_7__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_8__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
| `Personalization_9__c` | APPEND0 (appendV2), APPEND2 (appendV2), APPEND11 (appendV2), APPEND14 (appendV2), APPEND16 (appendV2) +3 more |
