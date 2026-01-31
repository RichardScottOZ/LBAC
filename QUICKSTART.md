# LBAC - Quick Start Guide

## Getting Started in 5 Minutes

### 1. Installation
```bash
# Clone or download the repository
# No dependencies needed - just Python 3.6+

# Make the game executable (Unix/Linux/Mac)
chmod +x lbac_game.py
```

### 2. Run the Game
```bash
python3 lbac_game.py
```

### 3. Choose Your Civilization

**For Beginners:**
- **New Kingdom Egypt** - Balanced, wealthy, good for learning
- **Hittite Empire** - Strong military, good for aggressive play

**For Advanced Players:**
- **Mycenaean Greece** - Warrior culture, naval focus
- **Ugarit** - Trading city-state, diplomatic focus
- **Cyprus** - Resource-rich, maritime power
- **Assyria** - Rising power, military-focused

### 4. Your First Turn

**Recommended First Actions:**
1. Check your status (press 5)
2. Send a gift to a Friendly neighbor (action 1)
3. Establish a trade route (action 2)
4. End turn (action 6)

### 5. Key Strategies

#### Must Do Every Few Turns:
- **Monitor Food** - Starvation kills population
- **Produce Bronze** - Combine tin + copper (in Trade menu)
- **Build Military** - Prevents raids
- **Maintain 1-2 Allies** - They provide aid

#### Resource Priority:
1. **Food** - Keeps population alive
2. **Bronze** - Required for military
3. **Gold** - Enables actions
4. **Tin/Copper** - Make bronze

#### Victory Paths:
1. **Military** - Eliminate all rivals (after turn 50)
2. **Prestige** - Reach 100 prestige points
3. **Survival** - Outlast the collapse

### 6. Common Mistakes

❌ **Don't:**
- Ignore food production
- Make everyone your enemy
- Spend all your gold
- Neglect military defense
- Forget to produce bronze

✅ **Do:**
- Keep 50+ food reserves
- Maintain 2-3 alliances
- Balance spending and income
- Build diverse military
- Trade when profitable

### 7. Handling Events

**Drought**: Keep food reserves
**Earthquake**: Rebuild quickly
**Sea Peoples**: Strong navy helps
**Plague**: Population will recover
**Good Events**: Capitalize quickly

### 8. Mid-Game Tips

**Turns 10-20:**
- Solidify alliances
- Build economy
- Strengthen military

**Turns 20-40:**
- Target weak rivals
- Push for prestige
- Expand influence

**Turns 40+:**
- Victory push
- Eliminate threats
- Maximize score

### 9. Controls Summary

```
Main Menu:
1 - Diplomacy (gifts, alliances, threats)
2 - Trade (routes, exchange, produce bronze)
3 - Military (recruit, raid, war)
4 - Internal (agriculture, tech, prestige)
5 - View Status
6 - End Turn
7 - Quit
```

### 10. Quick Reference

**Military Strength:**
- Infantry = 1x
- Archers = 2x
- Navy = 3x
- Chariots = 5x

**Unit Costs:**
- Infantry: 10 bronze, 5 gold
- Archers: 8 bronze, 8 gold
- Navy: 20 bronze, 20 gold
- Chariots: 25 bronze, 15 gold

**Relationships:**
- Allied: 75-100
- Friendly: 25-74
- Neutral: -24 to 24
- Unfriendly: -25 to -74
- Hostile: -75 to -100

**Per Turn Production:**
- Food: 30 + (Tech/10)
- Gold: 15 + (Prestige/10)
- Tin: 10
- Copper: 10

**Per Turn Consumption:**
- Population: Food (Pop/20)
- Military: Food (Units/10)

---

## Demo Mode

Want to see the game in action first?
```bash
python3 demo.py
```

## Run Tests

Verify everything works:
```bash
python3 test_game.py
```

## Need Help?

- Read the full [README.md](README.md)
- Check [GAMEPLAY_EXAMPLE.md](GAMEPLAY_EXAMPLE.md)
- Study historical context in README

---

**Now go forth and survive the Bronze Age Collapse!**

*"Will your civilization endure the storm, or be lost to history?"*
