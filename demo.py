#!/usr/bin/env python3
"""
Demo script that showcases LBAC game features
This runs a scripted playthrough to demonstrate gameplay
"""

from lbac_game import Game, Resources, Civilization
import time


def demo_game():
    """Run a demonstration of the game"""
    print("\n" + "="*70)
    print("LBAC GAME DEMONSTRATION")
    print("="*70)
    print("\nThis demo showcases the game's features with a scripted playthrough.")
    print("In the actual game, all choices are interactive!\n")
    input("Press Enter to begin the demo...")
    
    # Create game
    game = Game()
    
    # Choose Egypt
    game.player_civ = game.civilizations["New Kingdom Egypt"]
    game.player_civ.is_player = True
    
    print("\n" + "="*70)
    print("CIVILIZATION SELECTED: New Kingdom Egypt")
    print("="*70)
    print("\nYou lead the ancient civilization of the Nile,")
    print("wealthy but facing unprecedented threats...")
    input("\nPress Enter to see your starting status...")
    
    # Show initial status
    game.display_status()
    game.display_relationships()
    
    input("\nPress Enter to continue...")
    
    # Demo: Send gift to Ugarit
    print("\n" + "-"*70)
    print("DEMO ACTION 1: DIPLOMACY - Send Gift to Ugarit")
    print("-"*70)
    print("\nUgarit is already Friendly. Let's strengthen our relationship...")
    
    ugarit_before = game.player_civ.relationships["Ugarit"]
    game.player_civ.resources.gold -= 20
    game.player_civ.modify_relationship("Ugarit", 15)
    game.civilizations["Ugarit"].modify_relationship("New Kingdom Egypt", 15)
    ugarit_after = game.player_civ.relationships["Ugarit"]
    
    print(f"\nSent valuable gifts worth 20 gold to Ugarit")
    print(f"Relationship: {ugarit_before:+d} → {ugarit_after:+d}")
    print(f"Status: {game.player_civ.get_relationship_status('Ugarit').value}")
    
    input("\nPress Enter to continue...")
    
    # Demo: Establish trade route
    print("\n" + "-"*70)
    print("DEMO ACTION 2: TRADE - Establish Trade Route with Cyprus")
    print("-"*70)
    print("\nCyprus is rich in copper. Let's establish trade...")
    
    gold_before = game.player_civ.resources.gold
    game.player_civ.resources.gold -= 10
    trade_profit = 28
    game.player_civ.resources.gold += trade_profit
    game.player_civ.modify_relationship("Cyprus", 10)
    gold_after = game.player_civ.resources.gold
    
    print(f"\nPaid 10 gold to establish trade route")
    print(f"Received {trade_profit} gold from initial trade")
    print(f"Net profit: {trade_profit - 10} gold")
    print(f"Gold: {gold_before} → {gold_after}")
    
    input("\nPress Enter to continue...")
    
    # Demo: Produce bronze
    print("\n" + "-"*70)
    print("DEMO ACTION 3: PRODUCTION - Produce Bronze")
    print("-"*70)
    print("\nBronze is essential for military units. Let's produce some...")
    
    tin_before = game.player_civ.resources.tin
    copper_before = game.player_civ.resources.copper
    bronze_before = game.player_civ.resources.bronze
    
    produced = game.player_civ.produce_bronze()
    
    print(f"\nTin: {tin_before} → {game.player_civ.resources.tin}")
    print(f"Copper: {copper_before} → {game.player_civ.resources.copper}")
    print(f"Bronze: {bronze_before} → {game.player_civ.resources.bronze}")
    print(f"Produced: {produced} bronze")
    
    input("\nPress Enter to continue...")
    
    # Demo: Recruit military
    print("\n" + "-"*70)
    print("DEMO ACTION 4: MILITARY - Recruit Naval Forces")
    print("-"*70)
    print("\nStrong navy is crucial for defending against Sea Peoples...")
    
    navy_before = game.player_civ.military.navy
    bronze_before = game.player_civ.resources.bronze
    gold_before = game.player_civ.resources.gold
    
    recruit_count = 5
    game.player_civ.resources.bronze -= 20 * recruit_count
    game.player_civ.resources.gold -= 20 * recruit_count
    game.player_civ.military.navy += recruit_count
    
    navy_after = game.player_civ.military.navy
    
    print(f"\nRecruited {recruit_count} naval units")
    print(f"Cost: {20 * recruit_count} bronze, {20 * recruit_count} gold")
    print(f"Navy: {navy_before} → {navy_after}")
    print(f"Total Military Strength: {game.player_civ.military.get_total_strength()}")
    
    input("\nPress Enter to continue...")
    
    # Demo: Random event - Good Harvest
    print("\n" + "!"*70)
    print("RANDOM EVENT: Good Harvest!")
    print("!"*70)
    
    food_before = game.player_civ.resources.food
    food_gain = 65
    game.player_civ.resources.food += food_gain
    
    print(f"\nThe Nile floods bring abundant harvests!")
    print(f"Food: {food_before} → {game.player_civ.resources.food}")
    print(f"Gained: {food_gain} food")
    
    input("\nPress Enter to continue...")
    
    # Demo: End turn
    print("\n" + "-"*70)
    print("DEMO: END TURN - Processing Turn Results")
    print("-"*70)
    
    print("\nProduction phase:")
    print("  +35 food (base + technology bonus)")
    print("  +20 gold (base + prestige bonus)")
    print("  +10 tin")
    print("  +10 copper")
    
    print("\nConsumption phase:")
    pop_consumption = game.player_civ.resources.population // 20
    mil_consumption = (game.player_civ.military.infantry + 
                      game.player_civ.military.chariots * 2 + 
                      game.player_civ.military.archers + 
                      game.player_civ.military.navy * 2) // 10
    print(f"  -{pop_consumption} food (population upkeep)")
    print(f"  -{mil_consumption} food (military upkeep)")
    
    input("\nPress Enter to continue...")
    
    # Show final status
    print("\n" + "="*70)
    print("CURRENT STATUS AFTER DEMO ACTIONS")
    print("="*70)
    
    game.display_status()
    game.display_relationships()
    
    print("\n" + "="*70)
    print("DEMO COMPLETE")
    print("="*70)
    print("\nThis demonstration showed:")
    print("  ✓ Diplomatic actions (gifts, relationship building)")
    print("  ✓ Trading system (trade routes, resource exchange)")
    print("  ✓ Resource production (bronze making)")
    print("  ✓ Military recruitment (building forces)")
    print("  ✓ Random events (good and bad)")
    print("  ✓ Turn-based mechanics (production & consumption)")
    print("\nIn the full game, you'll also experience:")
    print("  • Raids and warfare")
    print("  • Multiple victory conditions")
    print("  • 6 unique civilizations")
    print("  • Alliances and betrayals")
    print("  • Catastrophic events (droughts, earthquakes, Sea Peoples)")
    print("  • Dynamic AI opponents")
    print("\nReady to play? Run: python3 lbac_game.py")
    print("="*70)


if __name__ == "__main__":
    demo_game()
