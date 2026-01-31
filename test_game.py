#!/usr/bin/env python3
"""
Test script to validate LBAC game mechanics
"""

import sys
from lbac_game import (
    Game, Civilization, Resources, MilitaryForce, 
    RelationshipStatus, EventType
)


def test_resources():
    """Test resource management"""
    print("Testing Resources...")
    r1 = Resources(food=100, bronze=50, gold=30)
    r2 = Resources(food=20, bronze=10, gold=5)
    
    assert r1.can_afford(r2), "Should be able to afford cost"
    r1.subtract(r2)
    assert r1.food == 80, "Food should be 80"
    assert r1.bronze == 40, "Bronze should be 40"
    assert r1.gold == 25, "Gold should be 25"
    
    r1.add(Resources(food=20, gold=10))
    assert r1.food == 100, "Food should be back to 100"
    print("✓ Resources test passed")


def test_military():
    """Test military calculations"""
    print("Testing Military...")
    m = MilitaryForce(infantry=100, chariots=10, archers=50, navy=5)
    strength = m.get_total_strength()
    # 100 + (10*5) + (50*2) + (5*3) = 100 + 50 + 100 + 15 = 265
    assert strength == 265, f"Military strength should be 265, got {strength}"
    print("✓ Military test passed")


def test_civilization():
    """Test civilization mechanics"""
    print("Testing Civilization...")
    civ = Civilization(
        name="Test Civ",
        description="Test",
        resources=Resources(bronze=0, tin=30, copper=30),
        military=MilitaryForce()
    )
    
    # Test bronze production
    produced = civ.produce_bronze()
    assert produced == 30, f"Should produce 30 bronze, got {produced}"
    assert civ.resources.bronze == 30, f"Bronze should be 30, got {civ.resources.bronze}"
    assert civ.resources.tin == 0, "Tin should be consumed"
    assert civ.resources.copper == 0, "Copper should be consumed"
    
    # Test relationships
    civ.modify_relationship("Enemy", -50)
    status = civ.get_relationship_status("Enemy")
    assert status == RelationshipStatus.UNFRIENDLY, "Should be unfriendly"
    
    civ.modify_relationship("Friend", 80)
    status = civ.get_relationship_status("Friend")
    assert status == RelationshipStatus.ALLIED, "Should be allied"
    
    print("✓ Civilization test passed")


def test_game_initialization():
    """Test game initialization"""
    print("Testing Game Initialization...")
    game = Game()
    
    assert len(game.civilizations) == 6, "Should have 6 civilizations"
    assert game.turn == 1, "Should start at turn 1"
    assert not game.game_over, "Game should not be over"
    
    # Check all civilizations are initialized
    expected_civs = [
        "Mycenaean Greece",
        "Hittite Empire", 
        "New Kingdom Egypt",
        "Ugarit",
        "Cyprus",
        "Assyria"
    ]
    
    for civ_name in expected_civs:
        assert civ_name in game.civilizations, f"{civ_name} should exist"
        civ = game.civilizations[civ_name]
        assert civ.is_alive, f"{civ_name} should be alive"
        assert civ.resources.population > 0, f"{civ_name} should have population"
        assert len(civ.relationships) == 5, f"{civ_name} should have 5 relationships"
    
    print("✓ Game initialization test passed")


def test_relationship_mechanics():
    """Test relationship status boundaries"""
    print("Testing Relationship Mechanics...")
    civ = Civilization(name="Test", description="Test")
    
    # Test all relationship levels
    test_cases = [
        (100, RelationshipStatus.ALLIED),
        (75, RelationshipStatus.ALLIED),
        (50, RelationshipStatus.FRIENDLY),
        (25, RelationshipStatus.FRIENDLY),
        (0, RelationshipStatus.NEUTRAL),
        (-24, RelationshipStatus.NEUTRAL),
        (-50, RelationshipStatus.UNFRIENDLY),
        (-75, RelationshipStatus.UNFRIENDLY),
        (-99, RelationshipStatus.HOSTILE),
        (-100, RelationshipStatus.HOSTILE),
    ]
    
    for value, expected_status in test_cases:
        civ.relationships["Other"] = value
        status = civ.get_relationship_status("Other")
        assert status == expected_status, \
            f"At {value}, expected {expected_status}, got {status}"
    
    print("✓ Relationship mechanics test passed")


def test_resource_consumption():
    """Test resource consumption"""
    print("Testing Resource Consumption...")
    civ = Civilization(
        name="Test",
        description="Test",
        resources=Resources(food=100, population=1000),
        military=MilitaryForce(infantry=100, chariots=10, archers=50, navy=5)
    )
    
    # Population consumes food/20, military consumes (total/10)
    # Population: 1000/20 = 50
    # Military: (100 + 10*2 + 50 + 5*2)/10 = 180/10 = 18
    # Total: 68
    
    result = civ.consume_resources()
    assert result is None, "Should not starve with enough food"
    assert civ.resources.food == 32, f"Food should be 32, got {civ.resources.food}"
    
    # Test starvation
    civ.resources.food = 10
    result = civ.consume_resources()
    assert result is not None, "Should have starvation message"
    assert civ.resources.food == 0, "Food should be 0 after starvation"
    assert civ.resources.population < 1000, "Population should decrease"
    
    print("✓ Resource consumption test passed")


def run_all_tests():
    """Run all tests"""
    print("="*70)
    print("LBAC Game Mechanics Test Suite")
    print("="*70)
    print()
    
    try:
        test_resources()
        test_military()
        test_civilization()
        test_game_initialization()
        test_relationship_mechanics()
        test_resource_consumption()
        
        print()
        print("="*70)
        print("✓ ALL TESTS PASSED!")
        print("="*70)
        return 0
    
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
