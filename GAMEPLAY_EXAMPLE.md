# LBAC Game - Gameplay Example

## Example Playthrough

This document shows an example game session to help you understand the mechanics.

### Starting the Game

```
$ python3 lbac_game.py

======================================================================
LATE BRONZE AGE COLLAPSE
A Game of Diplomacy, Trade, and Survival
======================================================================

The year is 1200 BC. Great civilizations face unprecedented crisis.
Choose your civilization:

1. Mycenaean Greece
   The warrior culture of mainland Greece, ruling from fortified palaces.
   Population: 1200, Military Strength: 375

2. Hittite Empire
   The powerful kingdom of Anatolia, masters of iron-working.
   Population: 1500, Military Strength: 500

3. New Kingdom Egypt
   The ancient civilization of the Nile, wealthy but facing threats.
   Population: 2000, Military Strength: 525

4. Ugarit
   A prosperous trading city-state on the Syrian coast.
   Population: 800, Military Strength: 224

5. Cyprus
   Island kingdom rich in copper deposits.
   Population: 900, Military Strength: 228

6. Assyria
   Rising power in northern Mesopotamia.
   Population: 1300, Military Strength: 403

Select civilization (1-6): 3

You have chosen to lead New Kingdom Egypt!
Your goal: Survive the coming collapse and emerge stronger.
```

### Turn 1 - Initial Status

```
======================================================================
Turn 1 - New Kingdom Egypt
======================================================================

RESOURCES:
  Population: 2000
  Food: 200
  Bronze: 70
  Gold: 100
  Tin: 35 | Copper: 50

MILITARY:
  Infantry: 180
  Chariots: 20
  Archers: 100
  Navy: 15
  Total Strength: 525

PRESTIGE: 50
TECHNOLOGY: 50

DIPLOMATIC RELATIONS:
  Mycenaean Greece: Neutral (+5)
  Hittite Empire: Neutral (-12)
  Ugarit: Friendly (+18)
  Cyprus: Neutral (-3)
  Assyria: Unfriendly (-30)
```

### Example Actions

#### Turn 1: Diplomacy - Strengthen Alliance with Ugarit

```
ACTIONS:
1. Diplomacy
2. Trade
3. Military
4. Internal Affairs
5. View Detailed Status
6. End Turn
7. Quit Game

Choose action: 1

--- DIPLOMACY ---

Choose civilization to interact with:
1. Mycenaean Greece - Neutral
2. Hittite Empire - Neutral
3. Ugarit - Friendly
4. Cyprus - Neutral
5. Assyria - Unfriendly
6. Back

Select: 3

--- Diplomacy with Ugarit ---
Current Relationship: Friendly (+18)

1. Send Gift (costs 20 gold)
2. Propose Alliance (requires Friendly or better)
3. Threaten (may worsen relations)
4. Request Aid
5. Back

Choose action: 2

Ugarit accepts your alliance!
```

#### Turn 2: Trade - Establish Trade Route

```
--- TRADE ---
1. Establish Trade Route
2. Trade Resources
3. Produce Bronze (combine Tin + Copper)
4. Back

Choose action: 1

Establish trade route with:
1. Mycenaean Greece
2. Hittite Empire
3. Ugarit
4. Cyprus
5. Assyria

Select: 4

Trade route established! Gained 25 gold.
```

#### Turn 3: Internal Affairs - Invest in Agriculture

```
--- INTERNAL AFFAIRS ---
1. Invest in Agriculture (50 gold -> increase food production)
2. Invest in Technology (60 gold -> increase tech level)
3. Hold Festival (30 gold -> increase prestige)
4. Back

Choose action: 1

Invested in agriculture! Food stores increased.
```

#### Turn 4: Military - Build Defenses

```
--- MILITARY ---
1. Recruit Units
2. Launch Raid
3. Declare War
4. Back

Choose action: 1

Recruit Units:
1. Infantry (10 bronze, 5 gold) - Current: 180
2. Chariots (25 bronze, 15 gold) - Current: 20
3. Archers (8 bronze, 8 gold) - Current: 100
4. Navy (20 bronze, 20 gold) - Current: 15

Select unit type: 4
How many? 3

Recruited 3 navy!
```

#### Turn 5: Random Event - Drought

```
Ending turn...

Produced: 35 food, 20 gold, 10 tin, 10 copper
Automatically produced 10 bronze from tin and copper

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MAJOR EVENT!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

DROUGHT strikes your lands! Lost 45 food.

Press Enter to continue...
```

#### Turn 10: Random Event - Sea Peoples

```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MAJOR EVENT!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

SEA PEOPLES raid your coasts!
Your navy repels the attack!

Press Enter to continue...
```

#### Turn 15: Military - Launch Raid

```
--- MILITARY ---
Choose action: 2

Raid which civilization:
1. Mycenaean Greece
2. Hittite Empire
3. Ugarit
4. Cyprus
5. Assyria

Select: 5

Raiding Assyria...
Your strength: 680
Their defense: 201

Victory! Plundered 35 gold and 22 food!
Your losses: 12 infantry
Their losses: 18 infantry
```

### Mid-Game Strategy

After 20 turns, you might focus on:

1. **Building Prestige** to reach 100 for a prestige victory
2. **Maintaining Alliances** with Ugarit and Cyprus
3. **Weakening Rivals** through strategic raids
4. **Balancing Resources** to avoid starvation
5. **Preparing for Events** by maintaining reserves

### Victory Conditions

The game ends when:
- You are the last civilization standing (after turn 50)
- Your prestige reaches 100
- You are defeated (population reaches 0)

### Tips from This Example

1. **Egypt's Strengths**: Large population, good navy, wealthy
2. **Early Alliances**: Build relationships early when it's cheaper
3. **Trade Routes**: Profitable investment (10 gold cost, 15-30 return)
4. **Naval Power**: Protects against Sea Peoples raids
5. **Resource Balance**: Egypt can afford to invest in both military and internal affairs
6. **Strategic Raiding**: Weak neighbors like Assyria can be profitable targets

### Common Mistakes to Avoid

1. **Ignoring Food**: Starvation can devastate your population
2. **No Military**: Makes you vulnerable to raids
3. **Poor Diplomacy**: Having all enemies means constant warfare
4. **Overspending**: Running out of gold prevents important actions
5. **Neglecting Bronze**: Need tin + copper to produce bronze for military

### Advanced Tactics

1. **Alliance Network**: Ally with 2-3 civilizations for mutual protection
2. **Resource Trading**: Buy tin/copper when cheap, sell bronze when you have excess
3. **Prestige Rush**: Hold festivals and win battles to reach 100 prestige quickly
4. **Elimination Strategy**: Weaken one civilization at a time through raids
5. **Event Preparation**: Keep 50+ food reserves for droughts, strong navy for Sea Peoples

---

This example shows just one path through the game. Each playthrough will be different based on:
- Your chosen civilization
- Random events that occur
- Diplomatic choices you make
- Military strategies you employ
- AI civilization behavior

Good luck surviving the Bronze Age Collapse!
