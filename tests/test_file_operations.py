import pytest
import os
import tempfile
from project1_starter import create_character, save_character, load_character

class TestFileOperations:
    """Test file save and load functionality"""
    
    def test_save_and_load_character(self):
        """Test saving and loading a character maintains data integrity"""
        char = create_character("SaveTest", "Mage")
        filename = "test_save_character.txt"
        
        # Clean up any existing file
        if os.path.exists(filename):
            os.remove(filename)
        
        # Test saving
        result = save_character(char, filename)
        assert result == True, "save_character should return True on success"
        assert os.path.exists(filename), "Save file should be created"
        
        # Test loading
        loaded_char = load_character(filename)
        assert loaded_char is not None, "load_character should return character data"
        assert loaded_char["name"] == char["name"], "Loaded character name should match original"
        assert loaded_char["class"] == char["class"], "Loaded character class should match original"
        assert loaded_char["level"] == char["level"], "Loaded character level should match original"
        assert loaded_char["strength"] == char["strength"], "Loaded character strength should match original"
        assert loaded_char["magic"] == char["magic"], "Loaded character magic should match original"
        assert loaded_char["health"] == char["health"], "Loaded character health should match original"
        assert loaded_char["gold"] == char["gold"], "Loaded character gold should match original"
        
        # Clean up
        os.remove(filename)

    def test_file_format_compliance(self):
        """Test that save file uses the required format"""
        char = create_character("FormatTest", "Rogue")
        filename = "format_test.txt"
        
        # Clean up any existing file
        if os.path.exists(filename):
            os.remove(filename)
        
        save_character(char, filename)
        
        with open(filename, 'r') as f:
            content = f.read()
        
        # Check required format
        required_lines = [
            "Character Name:",
            "Class:",
            "Level:",
            "Strength:",
            "Magic:",
            "Health:",
            "Gold:"
        ]
        
        for line in required_lines:
            assert line in content, f"Save file should contain '{line}'"
        
        # Check that actual values are present
        assert "FormatTest" in content, "Character name should be in file"
        assert "Rogue" in content, "Character class should be in file"
        
        os.remove(filename)

    def test_load_nonexistent_file(self):
        """Test loading a file that doesn't exist"""
        result = load_character("this_file_absolutely_does_not_exist.txt")
        assert result is None, "load_character should return None for nonexistent files"

    def test_save_character_return_value(self):
        """Test that save_character returns appropriate boolean values"""
        char = create_character("ReturnTest", "Cleric")
        filename = "return_test.txt"
        
        # Clean up any existing file
        if os.path.exists(filename):
            os.remove(filename)
        
        # Test successful save
        result = save_character(char, filename)
        assert isinstance(result, bool), "save_character should return a boolean"
        assert result == True, "save_character should return True on success"
        
        os.remove(filename)

    def test_multiple_save_load_cycles(self):
        """Test that multiple save/load cycles work correctly"""
        chars = [
            create_character("Hero1", "Warrior"),
            create_character("Hero2", "Mage"),
            create_character("Hero3", "Rogue")
        ]
        
        filenames = ["hero1.txt", "hero2.txt", "hero3.txt"]
        
        # Save all characters
        for char, filename in zip(chars, filenames):
            if os.path.exists(filename):
                os.remove(filename)
            result = save_character(char, filename)
            assert result == True, f"Failed to save {char['name']}"
        
        # Load all characters and verify
        for original_char, filename in zip(chars, filenames):
            loaded_char = load_character(filename)
            assert loaded_char is not None, f"Failed to load {filename}"
            assert loaded_char["name"] == original_char["name"], "Name mismatch after load"
            assert loaded_char["class"] == original_char["class"], "Class mismatch after load"
            os.remove(filename)
