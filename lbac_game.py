#!/usr/bin/env python3
"""
Late Bronze Age Collapse (LBAC) - A Diplomacy, Trading and Conflict Resource Game
Inspired by King of Dragon Pass

Set in the Late Bronze Age Collapse era (circa 1200 BC), you lead one of the great
civilizations through a period of unprecedented crisis and opportunity.
"""

import random
import sys
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum


class RelationshipStatus(Enum):
    """Diplomatic relationship statuses"""
    ALLIED = "Allied"
    FRIENDLY = "Friendly"
    NEUTRAL = "Neutral"
    UNFRIENDLY = "Unfriendly"
    HOSTILE = "Hostile"
    WAR = "At War"


class EventType(Enum):
    """Types of random events"""
    DROUGHT = "drought"
    EARTHQUAKE = "earthquake"
    SEA_PEOPLES = "sea_peoples"
    PLAGUE = "plague"
    GOOD_HARVEST = "good_harvest"
    TRADE_OPPORTUNITY = "trade_opportunity"
    DIPLOMATIC_INCIDENT = "diplomatic_incident"


@dataclass
class Resources:
    """Civilization resources"""
    food: int = 100
    bronze: int = 50
    gold: int = 50
    tin: int = 30
    copper: int = 30
    population: int = 1000
    
    def can_afford(self, cost: 'Resources') -> bool:
        """Check if we have enough resources"""
        return (self.food >= cost.food and
                self.bronze >= cost.bronze and
                self.gold >= cost.gold and
                self.tin >= cost.tin and
                self.copper >= cost.copper)
    
    def subtract(self, cost: 'Resources'):
        """Subtract resources"""
        self.food -= cost.food
        self.bronze -= cost.bronze
        self.gold -= cost.gold
        self.tin -= cost.tin
        self.copper -= cost.copper
    
    def add(self, gain: 'Resources'):
        """Add resources"""
        self.food += gain.food
        self.bronze += gain.bronze
        self.gold += gain.gold
        self.tin += gain.tin
        self.copper += gain.copper


@dataclass
class MilitaryForce:
    """Military strength"""
    infantry: int = 100
    chariots: int = 10
    archers: int = 50
    navy: int = 5
    
    def get_total_strength(self) -> int:
        """Calculate total military strength"""
        return self.infantry + (self.chariots * 5) + (self.archers * 2) + (self.navy * 3)


@dataclass
class Civilization:
    """Represents a civilization in the game"""
    name: str
    description: str
    resources: Resources = field(default_factory=Resources)
    military: MilitaryForce = field(default_factory=MilitaryForce)
    relationships: Dict[str, int] = field(default_factory=dict)  # -100 to 100
    prestige: int = 50
    technology_level: int = 50
    is_player: bool = False
    is_alive: bool = True
    
    def get_relationship_status(self, faction_name: str) -> RelationshipStatus:
        """Get relationship status with another faction"""
        value = self.relationships.get(faction_name, 0)
        if value >= 75:
            return RelationshipStatus.ALLIED
        elif value >= 25:
            return RelationshipStatus.FRIENDLY
        elif value >= -25:
            return RelationshipStatus.NEUTRAL
        elif value >= -75:
            return RelationshipStatus.UNFRIENDLY
        elif value >= -100:
            return RelationshipStatus.HOSTILE
        else:
            return RelationshipStatus.WAR
    
    def modify_relationship(self, faction_name: str, change: int):
        """Modify relationship with another faction"""
        current = self.relationships.get(faction_name, 0)
        self.relationships[faction_name] = max(-100, min(100, current + change))
    
    def produce_bronze(self):
        """Produce bronze from tin and copper"""
        producable = min(self.resources.tin, self.resources.copper)
        self.resources.tin -= producable
        self.resources.copper -= producable
        self.resources.bronze += producable
        return producable
    
    def consume_resources(self):
        """Consume resources each turn"""
        # Population consumes food
        food_needed = self.resources.population // 20
        self.resources.food -= food_needed
        
        # Military consumes resources
        military_cost = (self.military.infantry + self.military.chariots * 2 + 
                        self.military.archers + self.military.navy * 2) // 10
        self.resources.food -= military_cost
        
        # Check for starvation
        if self.resources.food < 0:
            starvation = abs(self.resources.food)
            population_loss = min(starvation * 10, self.resources.population // 4)
            self.resources.population -= population_loss
            self.resources.food = 0
            return f"Starvation! Lost {population_loss} population."
        return None


class Game:
    """Main game class"""
    
    def __init__(self):
        self.turn = 1
        self.civilizations: Dict[str, Civilization] = {}
        self.player_civ: Optional[Civilization] = None
        self.game_over = False
        self.initialize_civilizations()
    
    def initialize_civilizations(self):
        """Initialize all civilizations"""
        civs_data = [
            {
                "name": "Mycenaean Greece",
                "description": "The warrior culture of mainland Greece, ruling from fortified palaces.",
                "resources": Resources(food=120, bronze=60, gold=70, tin=40, copper=40, population=1200),
                "military": MilitaryForce(infantry=150, chariots=15, archers=60, navy=10)
            },
            {
                "name": "Hittite Empire",
                "description": "The powerful kingdom of Anatolia, masters of iron-working.",
                "resources": Resources(food=150, bronze=80, gold=60, tin=50, copper=50, population=1500),
                "military": MilitaryForce(infantry=200, chariots=25, archers=80, navy=5)
            },
            {
                "name": "New Kingdom Egypt",
                "description": "The ancient civilization of the Nile, wealthy but facing threats.",
                "resources": Resources(food=200, bronze=70, gold=100, tin=35, copper=50, population=2000),
                "military": MilitaryForce(infantry=180, chariots=20, archers=100, navy=15)
            },
            {
                "name": "Ugarit",
                "description": "A prosperous trading city-state on the Syrian coast.",
                "resources": Resources(food=80, bronze=50, gold=80, tin=30, copper=30, population=800),
                "military": MilitaryForce(infantry=80, chariots=8, archers=40, navy=12)
            },
            {
                "name": "Cyprus",
                "description": "Island kingdom rich in copper deposits.",
                "resources": Resources(food=90, bronze=60, gold=60, tin=20, copper=80, population=900),
                "military": MilitaryForce(infantry=90, chariots=5, archers=45, navy=15)
            },
            {
                "name": "Assyria",
                "description": "Rising power in northern Mesopotamia.",
                "resources": Resources(food=130, bronze=70, gold=55, tin=45, copper=45, population=1300),
                "military": MilitaryForce(infantry=160, chariots=18, archers=90, navy=3)
            }
        ]
        
        for civ_data in civs_data:
            civ = Civilization(
                name=civ_data["name"],
                description=civ_data["description"],
                resources=civ_data["resources"],
                military=civ_data["military"]
            )
            self.civilizations[civ.name] = civ
        
        # Initialize relationships (slight bias towards neutral/friendly)
        for civ in self.civilizations.values():
            for other_civ_name in self.civilizations.keys():
                if other_civ_name != civ.name:
                    civ.relationships[other_civ_name] = random.randint(-20, 20)
    
    def choose_civilization(self):
        """Let player choose their civilization"""
        print("\n" + "="*70)
        print("LATE BRONZE AGE COLLAPSE")
        print("A Game of Diplomacy, Trade, and Survival")
        print("="*70)
        print("\nThe year is 1200 BC. Great civilizations face unprecedented crisis.")
        print("Choose your civilization:\n")
        
        civ_list = list(self.civilizations.values())
        for i, civ in enumerate(civ_list, 1):
            print(f"{i}. {civ.name}")
            print(f"   {civ.description}")
            print(f"   Population: {civ.resources.population}, Military Strength: {civ.military.get_total_strength()}")
            print()
        
        while True:
            try:
                choice = input("Select civilization (1-{}): ".format(len(civ_list)))
                choice_num = int(choice)
                if 1 <= choice_num <= len(civ_list):
                    self.player_civ = civ_list[choice_num - 1]
                    self.player_civ.is_player = True
                    print(f"\nYou have chosen to lead {self.player_civ.name}!")
                    print("Your goal: Survive the coming collapse and emerge stronger.\n")
                    input("Press Enter to begin...")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(civ_list)}")
            except (ValueError, EOFError):
                print(f"Please enter a number between 1 and {len(civ_list)}")
    
    def display_status(self):
        """Display current status"""
        print("\n" + "="*70)
        print(f"Turn {self.turn} - {self.player_civ.name}")
        print("="*70)
        
        print("\nRESOURCES:")
        print(f"  Population: {self.player_civ.resources.population}")
        print(f"  Food: {self.player_civ.resources.food}")
        print(f"  Bronze: {self.player_civ.resources.bronze}")
        print(f"  Gold: {self.player_civ.resources.gold}")
        print(f"  Tin: {self.player_civ.resources.tin} | Copper: {self.player_civ.resources.copper}")
        
        print("\nMILITARY:")
        print(f"  Infantry: {self.player_civ.military.infantry}")
        print(f"  Chariots: {self.player_civ.military.chariots}")
        print(f"  Archers: {self.player_civ.military.archers}")
        print(f"  Navy: {self.player_civ.military.navy}")
        print(f"  Total Strength: {self.player_civ.military.get_total_strength()}")
        
        print(f"\nPRESTIGE: {self.player_civ.prestige}")
        print(f"TECHNOLOGY: {self.player_civ.technology_level}")
    
    def display_relationships(self):
        """Display diplomatic relationships"""
        print("\nDIPLOMATIC RELATIONS:")
        for civ_name, civ in self.civilizations.items():
            if civ_name != self.player_civ.name and civ.is_alive:
                status = self.player_civ.get_relationship_status(civ_name)
                value = self.player_civ.relationships[civ_name]
                print(f"  {civ_name}: {status.value} ({value:+d})")
    
    def main_menu(self) -> str:
        """Display main action menu"""
        print("\n" + "-"*70)
        print("ACTIONS:")
        print("1. Diplomacy")
        print("2. Trade")
        print("3. Military")
        print("4. Internal Affairs")
        print("5. View Detailed Status")
        print("6. End Turn")
        print("7. Quit Game")
        
        choice = input("\nChoose action: ").strip()
        return choice
    
    def diplomacy_menu(self):
        """Handle diplomatic actions"""
        print("\n--- DIPLOMACY ---")
        alive_civs = [name for name, civ in self.civilizations.items() 
                     if civ.is_alive and name != self.player_civ.name]
        
        if not alive_civs:
            print("No other civilizations remain!")
            return
        
        print("\nChoose civilization to interact with:")
        for i, civ_name in enumerate(alive_civs, 1):
            status = self.player_civ.get_relationship_status(civ_name)
            print(f"{i}. {civ_name} - {status.value}")
        print(f"{len(alive_civs) + 1}. Back")
        
        try:
            choice = int(input("\nSelect: "))
            if 1 <= choice <= len(alive_civs):
                target_name = alive_civs[choice - 1]
                self.diplomatic_actions(target_name)
        except (ValueError, EOFError):
            pass
    
    def diplomatic_actions(self, target_name: str):
        """Perform diplomatic action with target civilization"""
        target = self.civilizations[target_name]
        status = self.player_civ.get_relationship_status(target_name)
        
        print(f"\n--- Diplomacy with {target_name} ---")
        print(f"Current Relationship: {status.value} ({self.player_civ.relationships[target_name]:+d})")
        print("\n1. Send Gift (costs 20 gold)")
        print("2. Propose Alliance (requires Friendly or better)")
        print("3. Threaten (may worsen relations)")
        print("4. Request Aid")
        print("5. Back")
        
        try:
            action = int(input("\nChoose action: "))
            
            if action == 1:
                if self.player_civ.resources.gold >= 20:
                    self.player_civ.resources.gold -= 20
                    improvement = random.randint(10, 25)
                    self.player_civ.modify_relationship(target_name, improvement)
                    target.modify_relationship(self.player_civ.name, improvement)
                    print(f"\nYou sent a valuable gift to {target_name}.")
                    print(f"Relationship improved by {improvement}!")
                else:
                    print("\nInsufficient gold!")
            
            elif action == 2:
                if self.player_civ.relationships[target_name] >= 25:
                    if random.random() < 0.7:
                        self.player_civ.modify_relationship(target_name, 25)
                        target.modify_relationship(self.player_civ.name, 25)
                        print(f"\n{target_name} accepts your alliance!")
                    else:
                        print(f"\n{target_name} declines your alliance proposal.")
                else:
                    print("\nRelationship not good enough for alliance!")
            
            elif action == 3:
                change = random.randint(-30, -10)
                self.player_civ.modify_relationship(target_name, change)
                target.modify_relationship(self.player_civ.name, change)
                print(f"\nYou threatened {target_name}. They are not pleased.")
            
            elif action == 4:
                if self.player_civ.relationships[target_name] >= 50:
                    aid = random.randint(10, 30)
                    self.player_civ.resources.food += aid
                    print(f"\n{target_name} sends {aid} food to assist you!")
                else:
                    print(f"\n{target_name} refuses to send aid.")
        
        except (ValueError, EOFError):
            pass
    
    def trade_menu(self):
        """Handle trading actions"""
        print("\n--- TRADE ---")
        print("1. Establish Trade Route")
        print("2. Trade Resources")
        print("3. Produce Bronze (combine Tin + Copper)")
        print("4. Back")
        
        try:
            choice = int(input("\nChoose action: "))
            
            if choice == 1:
                alive_civs = [name for name, civ in self.civilizations.items() 
                            if civ.is_alive and name != self.player_civ.name]
                if alive_civs:
                    print("\nEstablish trade route with:")
                    for i, civ_name in enumerate(alive_civs, 1):
                        print(f"{i}. {civ_name}")
                    
                    idx = int(input("Select: ")) - 1
                    if 0 <= idx < len(alive_civs):
                        target_name = alive_civs[idx]
                        if self.player_civ.resources.gold >= 10:
                            self.player_civ.resources.gold -= 10
                            self.player_civ.modify_relationship(target_name, 10)
                            bonus = random.randint(15, 30)
                            self.player_civ.resources.gold += bonus
                            print(f"\nTrade route established! Gained {bonus} gold.")
                        else:
                            print("\nInsufficient gold!")
            
            elif choice == 2:
                print("\nTrade your resources:")
                print("1. Trade 20 Food for 10 Gold")
                print("2. Trade 15 Bronze for 20 Gold")
                print("3. Trade 25 Gold for 15 Tin")
                print("4. Trade 25 Gold for 15 Copper")
                
                trade_choice = int(input("Select: "))
                
                if trade_choice == 1 and self.player_civ.resources.food >= 20:
                    self.player_civ.resources.food -= 20
                    self.player_civ.resources.gold += 10
                    print("\nTraded 20 Food for 10 Gold")
                elif trade_choice == 2 and self.player_civ.resources.bronze >= 15:
                    self.player_civ.resources.bronze -= 15
                    self.player_civ.resources.gold += 20
                    print("\nTraded 15 Bronze for 20 Gold")
                elif trade_choice == 3 and self.player_civ.resources.gold >= 25:
                    self.player_civ.resources.gold -= 25
                    self.player_civ.resources.tin += 15
                    print("\nTraded 25 Gold for 15 Tin")
                elif trade_choice == 4 and self.player_civ.resources.gold >= 25:
                    self.player_civ.resources.gold -= 25
                    self.player_civ.resources.copper += 15
                    print("\nTraded 25 Gold for 15 Copper")
                else:
                    print("\nInsufficient resources!")
            
            elif choice == 3:
                produced = self.player_civ.produce_bronze()
                print(f"\nProduced {produced} bronze from tin and copper!")
        
        except (ValueError, EOFError):
            pass
    
    def military_menu(self):
        """Handle military actions"""
        print("\n--- MILITARY ---")
        print("1. Recruit Units")
        print("2. Launch Raid")
        print("3. Declare War")
        print("4. Back")
        
        try:
            choice = int(input("\nChoose action: "))
            
            if choice == 1:
                print("\nRecruit Units:")
                print(f"1. Infantry (10 bronze, 5 gold) - Current: {self.player_civ.military.infantry}")
                print(f"2. Chariots (25 bronze, 15 gold) - Current: {self.player_civ.military.chariots}")
                print(f"3. Archers (8 bronze, 8 gold) - Current: {self.player_civ.military.archers}")
                print(f"4. Navy (20 bronze, 20 gold) - Current: {self.player_civ.military.navy}")
                
                unit_choice = int(input("Select unit type: "))
                amount = int(input("How many? "))
                
                if unit_choice == 1:
                    cost = Resources(bronze=10*amount, gold=5*amount)
                    if self.player_civ.resources.can_afford(cost):
                        self.player_civ.resources.subtract(cost)
                        self.player_civ.military.infantry += amount
                        print(f"\nRecruited {amount} infantry!")
                    else:
                        print("\nInsufficient resources!")
                
                elif unit_choice == 2:
                    cost = Resources(bronze=25*amount, gold=15*amount)
                    if self.player_civ.resources.can_afford(cost):
                        self.player_civ.resources.subtract(cost)
                        self.player_civ.military.chariots += amount
                        print(f"\nRecruited {amount} chariots!")
                    else:
                        print("\nInsufficient resources!")
            
            elif choice == 2:
                alive_civs = [name for name, civ in self.civilizations.items() 
                            if civ.is_alive and name != self.player_civ.name]
                if alive_civs:
                    print("\nRaid which civilization:")
                    for i, civ_name in enumerate(alive_civs, 1):
                        print(f"{i}. {civ_name}")
                    
                    idx = int(input("Select: ")) - 1
                    if 0 <= idx < len(alive_civs):
                        target_name = alive_civs[idx]
                        self.conduct_raid(target_name)
            
            elif choice == 3:
                alive_civs = [name for name, civ in self.civilizations.items() 
                            if civ.is_alive and name != self.player_civ.name]
                if alive_civs:
                    print("\nDeclare war on:")
                    for i, civ_name in enumerate(alive_civs, 1):
                        print(f"{i}. {civ_name}")
                    
                    idx = int(input("Select: ")) - 1
                    if 0 <= idx < len(alive_civs):
                        target_name = alive_civs[idx]
                        self.player_civ.relationships[target_name] = -100
                        self.civilizations[target_name].relationships[self.player_civ.name] = -100
                        print(f"\n{self.player_civ.name} declares war on {target_name}!")
        
        except (ValueError, EOFError):
            pass
    
    def conduct_raid(self, target_name: str):
        """Conduct a raid on another civilization"""
        target = self.civilizations[target_name]
        
        our_strength = self.player_civ.military.get_total_strength()
        their_defense = target.military.get_total_strength() // 2  # Defenders have advantage
        
        print(f"\nRaiding {target_name}...")
        print(f"Your strength: {our_strength}")
        print(f"Their defense: {their_defense}")
        
        if our_strength > their_defense:
            # Successful raid
            loot_gold = random.randint(20, 50)
            loot_food = random.randint(10, 30)
            self.player_civ.resources.gold += loot_gold
            self.player_civ.resources.food += loot_food
            
            # Losses
            our_losses = random.randint(5, 15)
            their_losses = random.randint(10, 25)
            
            self.player_civ.military.infantry -= our_losses
            target.military.infantry -= their_losses
            
            print(f"\nVictory! Plundered {loot_gold} gold and {loot_food} food!")
            print(f"Your losses: {our_losses} infantry")
            print(f"Their losses: {their_losses} infantry")
            
            # Relationship damage
            self.player_civ.modify_relationship(target_name, -30)
            target.modify_relationship(self.player_civ.name, -30)
            
            self.player_civ.prestige += 5
        else:
            # Failed raid
            our_losses = random.randint(15, 30)
            their_losses = random.randint(5, 10)
            
            self.player_civ.military.infantry -= our_losses
            target.military.infantry -= their_losses
            
            print(f"\nDefeat! The raid failed!")
            print(f"Your losses: {our_losses} infantry")
            print(f"Their losses: {their_losses} infantry")
            
            self.player_civ.modify_relationship(target_name, -20)
            target.modify_relationship(self.player_civ.name, -10)
            
            self.player_civ.prestige -= 5
    
    def internal_affairs_menu(self):
        """Handle internal affairs"""
        print("\n--- INTERNAL AFFAIRS ---")
        print("1. Invest in Agriculture (50 gold -> increase food production)")
        print("2. Invest in Technology (60 gold -> increase tech level)")
        print("3. Hold Festival (30 gold -> increase prestige)")
        print("4. Back")
        
        try:
            choice = int(input("\nChoose action: "))
            
            if choice == 1 and self.player_civ.resources.gold >= 50:
                self.player_civ.resources.gold -= 50
                self.player_civ.resources.food += 40
                print("\nInvested in agriculture! Food stores increased.")
            elif choice == 2 and self.player_civ.resources.gold >= 60:
                self.player_civ.resources.gold -= 60
                self.player_civ.technology_level += 5
                print("\nInvested in technology! Tech level increased.")
            elif choice == 3 and self.player_civ.resources.gold >= 30:
                self.player_civ.resources.gold -= 30
                self.player_civ.prestige += 10
                print("\nHeld a grand festival! Prestige increased.")
            else:
                print("\nInsufficient gold!")
        except (ValueError, EOFError):
            pass
    
    def random_event(self):
        """Generate a random event"""
        if random.random() < 0.3:  # 30% chance per turn
            event = random.choice(list(EventType))
            
            print("\n" + "!"*70)
            print("MAJOR EVENT!")
            print("!"*70)
            
            if event == EventType.DROUGHT:
                food_loss = random.randint(30, 60)
                self.player_civ.resources.food -= food_loss
                print(f"\nDROUGHT strikes your lands! Lost {food_loss} food.")
            
            elif event == EventType.EARTHQUAKE:
                gold_loss = random.randint(20, 40)
                pop_loss = random.randint(50, 150)
                self.player_civ.resources.gold -= gold_loss
                self.player_civ.resources.population -= pop_loss
                print(f"\nEARTHQUAKE devastates your cities!")
                print(f"Lost {gold_loss} gold and {pop_loss} population.")
            
            elif event == EventType.SEA_PEOPLES:
                print("\nSEA PEOPLES raid your coasts!")
                if self.player_civ.military.navy >= 10:
                    print("Your navy repels the attack!")
                    self.player_civ.prestige += 10
                else:
                    losses = random.randint(20, 40)
                    self.player_civ.military.infantry -= losses
                    self.player_civ.resources.gold -= 30
                    print(f"They plunder your lands! Lost {losses} infantry and 30 gold.")
            
            elif event == EventType.PLAGUE:
                pop_loss = random.randint(100, 300)
                self.player_civ.resources.population -= pop_loss
                print(f"\nPLAGUE sweeps through your population! Lost {pop_loss} people.")
            
            elif event == EventType.GOOD_HARVEST:
                food_gain = random.randint(40, 80)
                self.player_civ.resources.food += food_gain
                print(f"\nGOOD HARVEST! Gained {food_gain} food.")
            
            elif event == EventType.TRADE_OPPORTUNITY:
                gold_gain = random.randint(30, 60)
                self.player_civ.resources.gold += gold_gain
                print(f"\nTRADE OPPORTUNITY! Merchants bring {gold_gain} gold.")
            
            elif event == EventType.DIPLOMATIC_INCIDENT:
                civs = [name for name in self.civilizations.keys() 
                       if name != self.player_civ.name]
                if civs:
                    target = random.choice(civs)
                    change = random.randint(-20, 20)
                    self.player_civ.modify_relationship(target, change)
                    print(f"\nDIPLOMATIC INCIDENT with {target}!")
                    if change > 0:
                        print(f"Relations improved by {change}.")
                    else:
                        print(f"Relations worsened by {abs(change)}.")
            
            input("\nPress Enter to continue...")
    
    def ai_turn(self, civ: Civilization):
        """Simple AI turn for other civilizations"""
        # Produce bronze
        civ.produce_bronze()
        
        # Add some base production
        civ.resources.food += random.randint(20, 40)
        civ.resources.gold += random.randint(10, 20)
        civ.resources.tin += random.randint(5, 15)
        civ.resources.copper += random.randint(5, 15)
        
        # Consume resources
        civ.consume_resources()
        
        # Random actions
        if random.random() < 0.3:
            # Recruit units
            if civ.resources.bronze >= 10 and civ.resources.gold >= 5:
                civ.resources.bronze -= 10
                civ.resources.gold -= 5
                civ.military.infantry += 1
    
    def end_turn(self):
        """End current turn and process turn logic"""
        print("\nEnding turn...")
        
        # Player production
        base_food = 30 + (self.player_civ.technology_level // 10)
        base_gold = 15 + (self.player_civ.prestige // 10)
        base_tin = 10
        base_copper = 10
        
        self.player_civ.resources.food += base_food
        self.player_civ.resources.gold += base_gold
        self.player_civ.resources.tin += base_tin
        self.player_civ.resources.copper += base_copper
        
        print(f"\nProduced: {base_food} food, {base_gold} gold, {base_tin} tin, {base_copper} copper")
        
        # Produce bronze automatically if possible
        bronze_made = self.player_civ.produce_bronze()
        if bronze_made > 0:
            print(f"Automatically produced {bronze_made} bronze from tin and copper")
        
        # Consume resources
        message = self.player_civ.consume_resources()
        if message:
            print(f"\n{message}")
        
        # AI turns
        for name, civ in self.civilizations.items():
            if name != self.player_civ.name and civ.is_alive:
                self.ai_turn(civ)
        
        # Check for defeats
        for name, civ in self.civilizations.items():
            if civ.resources.population <= 0 and civ.is_alive:
                civ.is_alive = False
                print(f"\n{name} has collapsed!")
                if civ.is_player:
                    self.game_over = True
        
        # Random event
        self.random_event()
        
        # Check victory conditions
        if self.turn >= 50:
            self.check_victory()
        
        self.turn += 1
        input("\nPress Enter to continue...")
    
    def check_victory(self):
        """Check if player has won"""
        alive_count = sum(1 for civ in self.civilizations.values() if civ.is_alive)
        
        if alive_count == 1 and self.player_civ.is_alive:
            print("\n" + "="*70)
            print("VICTORY!")
            print("="*70)
            print(f"\nYou are the sole surviving civilization!")
            print(f"Final score: {self.player_civ.prestige + self.player_civ.resources.population // 10}")
            self.game_over = True
        elif self.player_civ.prestige >= 100:
            print("\n" + "="*70)
            print("PRESTIGE VICTORY!")
            print("="*70)
            print(f"\nYour civilization's prestige is unmatched!")
            self.game_over = True
    
    def view_detailed_status(self):
        """View detailed status of all civilizations"""
        print("\n" + "="*70)
        print("WORLD STATUS")
        print("="*70)
        
        for name, civ in self.civilizations.items():
            if civ.is_alive:
                marker = " (YOU)" if civ.is_player else ""
                print(f"\n{name}{marker}:")
                print(f"  Population: {civ.resources.population}")
                print(f"  Military Strength: {civ.military.get_total_strength()}")
                print(f"  Prestige: {civ.prestige}")
        
        input("\nPress Enter to continue...")
    
    def play(self):
        """Main game loop"""
        self.choose_civilization()
        
        while not self.game_over:
            self.display_status()
            self.display_relationships()
            
            choice = self.main_menu()
            
            if choice == "1":
                self.diplomacy_menu()
            elif choice == "2":
                self.trade_menu()
            elif choice == "3":
                self.military_menu()
            elif choice == "4":
                self.internal_affairs_menu()
            elif choice == "5":
                self.view_detailed_status()
            elif choice == "6":
                self.end_turn()
            elif choice == "7":
                print("\nThanks for playing!")
                break
        
        if self.game_over and not self.player_civ.is_alive:
            print("\n" + "="*70)
            print("GAME OVER")
            print("="*70)
            print("\nYour civilization has fallen to the Bronze Age Collapse.")
            print("History will remember your struggles...")


def main():
    """Entry point"""
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
