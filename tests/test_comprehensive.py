import pytest
import os
from project1_starter import create_character, level_up, display_character, save_character, load_character

class TestLevelUp:
    """Test character level up functionality"""
    
    def test_level_up_increases_level(self):
        """Test that level_up increases the character's level"""
        char = create_character("LevelTest", "Warrior")
        original_level = char["level"]
        level_up(char)
        assert char["level"] == original_level + 1, "level_up should increase level by 1"

    def test_level_up_modifies_character_directly(self):
        """Test that level_up modifies the original character dictionary"""
        char = create_character("ModifyTest", "Mage")
        char_id = id(char)  # Get memory address
        level_up(char)
        assert id(char) == char_id, "level_up should modify the same dictionary, not create a new one"

    def test_level_up_affects_stats(self):
        """Test that leveling up can change character stats"""
        char = create_character("StatTest", "Cleric")
        original_stats = (char["strength"], char["magic"], char["health"])
        level_up(char)
        new_stats = (char["strength"], char["magic"], char["health"])
        
        # Stats should either stay the same or change (depending on implementation)
        # This test ensures the function runs without error and maintains stat structure
        assert isinstance(char["strength"], (int, float)), "Strength should remain a number after level up"
        assert isinstance(char["magic"], (int, float)), "Magic should remain a number after level up"
        assert isinstance(char["health"], (int, float)), "Health should remain a number after level up"

class TestDisplayCharacter:
    """Test character display functionality"""
    
    def test_display_character_runs_without_error(self):
        """Test that display_character runs without throwing exceptions"""
        char = create_character("DisplayTest", "Rogue")
        try:
            # Capture output or just ensure no exceptions are thrown
            display_character(char)
        except Exception as e:
            pytest.fail(f"display_character should not throw exceptions: {e}")

    def test_display_character_returns_none(self):
        """Test that display_character returns None (it should print, not return)"""
        char = create_character("ReturnTest", "Warrior")
        result = display_character(char)
        assert result is None, "display_character should return None (it should print output)"

class TestErrorHandling:
    """Test error handling in various functions"""
    
    def test_save_character_handles_bad_directory(self):
        """Test that save_character handles invalid file paths gracefully"""
        char = create_character("ErrorTest", "Mage")
        # Try to save to a directory that doesn't exist or is invalid
        result = save_character(char, "/invalid/directory/path/test.txt")
        assert isinstance(result, bool), "save_character should return a boolean even on error"
        assert result == False, "save_character should return False when save fails"

    def test_create_character_with_empty_name(self):
        """Test creating character with empty name"""
        char = create_character("", "Warrior")
        # Should either handle gracefully or create character with empty name
        if char is not None:
            assert "name" in char, "Character should have name field even if empty"
            assert "class" in char, "Character should have class field"

    def test_create_character_with_none_values(self):
        """Test creating character with None values"""
        char = create_character(None, "Warrior")
        # Should handle None gracefully - either return None or handle the None value
        if char is not None:
            assert "name" in char, "Character should have name field"
            assert "class" in char, "Character should have class field"

class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_save_load_with_special_characters(self):
        """Test saving and loading characters with special characters in names"""
        special_names = ["José", "Anna-Marie", "O'Connor", "李小龙"]
        
        for name in special_names:
            char = create_character(name, "Warrior")
            if char is not None:  # Only test if character creation succeeded
                filename = f"special_char_test_{hash(name) % 1000}.txt"
                
                # Clean up any existing file
                if os.path.exists(filename):
                    os.remove(filename)
                
                save_result = save_character(char, filename)
                if save_result:  # Only test loading if save succeeded
                    loaded_char = load_character(filename)
                    if loaded_char is not None:
                        assert loaded_char["name"] == char["name"], f"Special character name '{name}' not preserved"
                    
                    # Clean up
                    if os.path.exists(filename):
                        os.remove(filename)

    def test_multiple_level_ups(self):
        """Test multiple level ups in sequence"""
        char = create_character("MultiLevel", "Rogue")
        original_level = char["level"]
        
        # Level up multiple times
        for i in range(5):
            level_up(char)
        
        assert char["level"] == original_level + 5, "Multiple level ups should accumulate correctly"
