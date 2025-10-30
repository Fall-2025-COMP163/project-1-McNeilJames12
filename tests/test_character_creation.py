import pytest
import sys
import os

# Import student's code
try:
    from project1_starter import create_character, calculate_stats
except ImportError:
    pytest.fail("Could not import required functions from project1_starter.py")

class TestCharacterCreation:
    """Test character creation functionality"""
    
    def test_create_character_warrior(self):
        """Test creating a warrior character"""
        char = create_character("TestHero", "Warrior")
        assert char is not None, "create_character should return a character dictionary"
        assert char["name"] == "TestHero", "Character name not set correctly"
        assert char["class"] == "Warrior", "Character class not set correctly"
        assert "level" in char, "Character should have a level"
        assert "strength" in char, "Character should have strength stat"
        assert "magic" in char, "Character should have magic stat"
        assert "health" in char, "Character should have health stat"
        assert "gold" in char, "Character should have gold"

    def test_create_character_all_classes(self):
        """Test creating characters of all required classes"""
        required_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
        for cls in required_classes:
            char = create_character("Test", cls)
            assert char is not None, f"Failed to create {cls} character"
            assert char["class"] == cls, f"Character class not set correctly for {cls}"

    def test_character_stats_are_numbers(self):
        """Test that character stats are reasonable numbers"""
        char = create_character("Test", "Warrior")
        assert isinstance(char["strength"], (int, float)), "Strength should be a number"
        assert isinstance(char["magic"], (int, float)), "Magic should be a number"
        assert isinstance(char["health"], (int, float)), "Health should be a number"
        assert isinstance(char["gold"], (int, float)), "Gold should be a number"
        assert isinstance(char["level"], (int, float)), "Level should be a number"

    def test_character_stats_are_positive(self):
        """Test that character stats are positive values"""
        char = create_character("Test", "Mage")
        assert char["strength"] > 0, "Strength should be positive"
        assert char["health"] > 0, "Health should be positive"
        assert char["magic"] >= 0, "Magic should be non-negative"
        assert char["gold"] >= 0, "Gold should be non-negative"
        assert char["level"] > 0, "Level should be positive"

    def test_calculate_stats_function(self):
        """Test the calculate_stats function"""
        stats = calculate_stats("Warrior", 1)
        assert isinstance(stats, tuple), "calculate_stats should return a tuple"
        assert len(stats) == 3, "Should return tuple of (strength, magic, health)"
        
        strength, magic, health = stats
        assert isinstance(strength, (int, float)), "Strength should be a number"
        assert isinstance(magic, (int, float)), "Magic should be a number"
        assert isinstance(health, (int, float)), "Health should be a number"

    def test_different_classes_different_stats(self):
        """Test that different classes have different stat distributions"""
        warrior_stats = calculate_stats("Warrior", 1)
        mage_stats = calculate_stats("Mage", 1)
        # At least one stat should be different between classes
        assert warrior_stats != mage_stats, "Different classes should have different stat distributions"

    def test_invalid_character_class(self):
        """Test handling of invalid character classes"""
        char = create_character("BadClass", "InvalidClass")
        # Should either return None or handle gracefully
        # Implementation dependent - adjust based on your requirements
        assert char is None or "class" in char, "Should handle invalid class gracefully"
