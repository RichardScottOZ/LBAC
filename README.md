# LBAC - Late Bronze Age Collapse

A Diplomacy, Trading and Conflict Resource Management Game

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎮 Quick Links

- **[Quick Start Guide](QUICKSTART.md)** - Get playing in 5 minutes
- **[Gameplay Example](GAMEPLAY_EXAMPLE.md)** - See a full playthrough
- **[Run Demo](demo.py)** - Watch the game in action

## Overview

Experience the tumultuous period of the Late Bronze Age Collapse (circa 1200 BC) in this strategic game inspired by King of Dragon Pass. Lead one of the great civilizations of the ancient world through unprecedented crisis, navigating diplomacy, trade, and conflict to ensure your people's survival.

**🎯 Quick Start:** `python3 lbac_game.py`

## Historical Background

The Late Bronze Age Collapse was one of history's most dramatic periods of societal upheaval. Around 1200 BC, the interconnected civilizations of the Eastern Mediterranean and Near East faced a "perfect storm" of catastrophes:

- **Environmental Disasters**: Prolonged droughts, earthquakes, and famines
- **Economic Breakdown**: Disruption of vital trade routes for tin and copper (essential for bronze production)
- **Military Threats**: The mysterious "Sea Peoples" and mass migrations
- **Social Upheaval**: Internal rebellions and the collapse of centralized authority

Major civilizations affected:
- **Mycenaean Greece**: Palatial centers destroyed, leading to the Greek Dark Ages
- **Hittite Empire**: Complete collapse, capital Hattusa abandoned
- **New Kingdom Egypt**: Survived but severely weakened
- **Canaanite City-States**: Many destroyed (including Ugarit, Hazor)
- **Cyprus**: Lost its complex urban centers
- **Assyria**: Emerged as a rising power

## Game Features

### Civilizations
Choose from six historical civilizations, each with unique strengths:

1. **Mycenaean Greece** - Warrior culture with strong navy
2. **Hittite Empire** - Masters of chariot warfare, powerful military
3. **New Kingdom Egypt** - Wealthy, large population, balanced forces
4. **Ugarit** - Trading city-state, maritime focus
5. **Cyprus** - Rich in copper resources, naval strength
6. **Assyria** - Rising military power from Mesopotamia

### Core Mechanics

#### Resources
- **Population**: Your civilization's people
- **Food**: Essential for feeding population and military
- **Bronze**: Primary military resource (made from tin + copper)
- **Gold**: Currency for trade and diplomacy
- **Tin & Copper**: Raw materials for bronze production

#### Diplomacy
- Build alliances with friendly civilizations
- Send gifts to improve relations
- Request aid in times of need
- Navigate complex relationships (Allied, Friendly, Neutral, Unfriendly, Hostile, At War)

#### Trade
- Establish trade routes for gold
- Exchange resources with other civilizations
- Produce bronze from tin and copper
- Balance resource production and consumption

#### Military
- Recruit four unit types:
  - **Infantry**: Reliable ground forces
  - **Chariots**: Elite shock troops (5x combat strength)
  - **Archers**: Ranged support (2x combat strength)
  - **Navy**: Coastal defense and raids (3x combat strength)
- Launch raids to plunder resources
- Declare wars to eliminate rivals
- Defend against threats including Sea Peoples

#### Events
Experience historical events and crises:
- Droughts and famines
- Devastating earthquakes
- Sea Peoples raids
- Plagues
- Diplomatic incidents
- Trade opportunities

#### Internal Affairs
- Invest in agriculture to increase food production
- Advance technology for better resource yields
- Hold festivals to boost prestige

### Victory Conditions

1. **Survival Victory**: Be the last civilization standing (after turn 50)
2. **Prestige Victory**: Reach 100 prestige points
3. **Time Limit**: Survive 50+ turns with the highest score

## Installation & Requirements

### Requirements
- Python 3.6 or higher
- No external dependencies required!

### Running the Game

```bash
# Make the game executable (Unix/Linux/Mac)
chmod +x lbac_game.py

# Run the game
python3 lbac_game.py

# Or directly (if executable)
./lbac_game.py
```

## How to Play

### Starting the Game
1. Run `python3 lbac_game.py`
2. Choose your civilization from the six available options
3. Read your civilization's description and starting stats

### Each Turn
The game displays:
- Your current resources (Population, Food, Bronze, Gold, Tin, Copper)
- Military forces (Infantry, Chariots, Archers, Navy)
- Prestige and Technology levels
- Diplomatic relations with other civilizations

### Available Actions

**1. Diplomacy**
- Choose a civilization to interact with
- Send gifts to improve relations (costs 20 gold)
- Propose alliances (requires Friendly relationship)
- Threaten rivals (worsens relations)
- Request aid from allies

**2. Trade**
- Establish trade routes (costs 10 gold, earns 15-30 gold)
- Exchange resources:
  - Trade Food for Gold
  - Trade Bronze for Gold
  - Trade Gold for Tin or Copper
- Produce Bronze (automatically combines Tin + Copper)

**3. Military**
- Recruit units:
  - Infantry: 10 bronze, 5 gold
  - Chariots: 25 bronze, 15 gold
  - Archers: 8 bronze, 8 gold
  - Navy: 20 bronze, 20 gold
- Launch raids on other civilizations
- Declare war

**4. Internal Affairs**
- Invest in Agriculture (50 gold → food production boost)
- Invest in Technology (60 gold → tech level increase)
- Hold Festival (30 gold → prestige boost)

**5. View Detailed Status**
- See the status of all surviving civilizations
- Compare military strengths
- Assess the global situation

**6. End Turn**
- Processes resource production
- Consumes resources (population and military maintenance)
- AI civilizations take their turns
- Random events may occur
- Checks victory/defeat conditions

### Tips for Success

1. **Balance Resources**: Ensure steady food production to prevent starvation
2. **Maintain Military**: Strong defenses deter raids and protect your people
3. **Forge Alliances**: Friendly neighbors can provide aid and trade opportunities
4. **Manage Bronze Production**: Keep tin and copper supplies steady
5. **Build Prestige**: Higher prestige increases gold income
6. **Adapt to Events**: Random events can drastically change your situation
7. **Plan for the Long Term**: Some victories require surviving 50+ turns

### Combat Mechanics
- **Raids**: Your military strength vs half of defender's strength
- **Victory**: Plunder gold and food, damage enemy forces
- **Defeat**: Lose more troops, damage diplomatic relations
- **Naval Defense**: Strong navy protects against Sea Peoples

### Resource Production (per turn)
- **Food**: 30 + (Technology/10)
- **Gold**: 15 + (Prestige/10)
- **Tin**: 10
- **Copper**: 10
- **Bronze**: Automatically produced from available Tin + Copper

### Resource Consumption (per turn)
- **Population**: Consumes Food (Population/20)
- **Military**: Consumes Food (Total Units/10)
- **Starvation**: If food < 0, lose up to 25% of population

## Game Design Philosophy

Inspired by **King of Dragon Pass**, this game emphasizes:

1. **Meaningful Choices**: Every decision affects your civilization's fate
2. **Emergent Narrative**: The story unfolds through your actions and random events
3. **Strategic Depth**: Balance short-term survival with long-term goals
4. **Historical Authenticity**: Events and mechanics reflect actual Bronze Age challenges
5. **Replayability**: Different civilizations and random events create unique experiences

## Historical Accuracy

While this is a game, it incorporates historical elements:

- **Civilizations**: Based on actual Late Bronze Age powers
- **Resources**: Bronze production required tin and copper trade networks
- **Events**: Droughts, earthquakes, and Sea Peoples were real threats
- **Trade**: Long-distance trade was essential to Bronze Age economies
- **Collapse**: Multiple factors contributed to the actual historical collapse

## Future Enhancements

Potential additions for future versions:
- More civilizations and city-states
- Deeper narrative events with branching choices
- Technology tree advancement
- Religious/cultural mechanics
- Marriage alliances
- More detailed combat system
- Save/load game functionality
- Multiple difficulty levels
- Achievements system

## Credits

**Game Design**: Inspired by King of Dragon Pass and the historical Late Bronze Age Collapse

**Historical Period**: Late Bronze Age (circa 1200 BC)

**Primary Sources**:
- Archaeological evidence from Mycenae, Hattusa, Ugarit, and other sites
- Egyptian records of the Sea Peoples
- Modern scholarship on the Bronze Age Collapse

## License

This is an educational project exploring historical game design.

## Contributing

Suggestions for historical accuracy improvements or gameplay enhancements are welcome!

---

*"The age of heroes is ending. Will your civilization survive the darkness to come?"*
