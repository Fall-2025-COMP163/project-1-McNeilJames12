"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: James McNeil
Date: 10/24/25

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

import os


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health

    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80}
    """
    # Use calculate_stats() for stat calculation
    strength, magic, health = calculate_stats(character_class)

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100,  # keeping your gold field; tests ignore it
    }

    return character


def calculate_stats(character_class, level=1):
    """
    Calculates base stats based on class and level
    Returns: tuple: (strength, magic, health)

    The tests require support for: Warrior, Mage, Rogue, Cleric.
    """
    # Normalize to Title Case so inputs like "mage" or "MAGE" work
    cls = str(character_class).title()

    if cls == "Warrior":
        strength = 15 + level * 3
        magic = 3 + level
        health = 120 + level * 10

    elif cls == "Mage":
        strength = 5 + level
        magic = 20 + level * 3
        health = 80 + level * 7

    elif cls == "Rogue":
        strength = 10 + level * 2
        magic = 8 + level
        health = 90 + level * 8

    elif cls == "Cleric":
        strength = 8 + level
        magic = 15 + level * 2
        health = 110 + level * 9

    else:
        # Default balanced stats (covers your extra classes like Fighter/Tanker/etc.)
        strength = 7 + level * 2
        magic = 7 + level * 2
        health = 100 + level * 10

    # normalize to ints so file values and display are clean
    return int(strength), int(magic), int(health)


# STOPPING RIGHT HERE AT 2:10AM SAT OCT 25
# had ai explain how to do this
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred

    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # Handle basic input validation
    if character == {} or filename == "":
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {int(character['level'])}\n")
        file.write(f"Strength: {int(character['strength'])}\n")
        file.write(f"Magic: {int(character['magic'])}\n")
        file.write(f"Health: {int(character['health'])}\n")
        file.write(f"Gold: {int(character.get('gold', 0))}\n")
    return True


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # Handle file not found
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    character = {}

    for line in lines:
        # Ignore empty/malformed lines quietly
        if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)

        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(float(value))
        elif key == "Strength":
            character["strength"] = int(float(value))
        elif key == "Magic":
            character["magic"] = int(float(value))
        elif key == "Health":
            character["health"] = int(float(value))
        elif key == "Gold":
            character["gold"] = int(float(value))

    return character


# STOPPING RIGHT HERE AT 12:09AM TUE OCT 28


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    if "gold" in character:  # optional field check
        print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # Increase level
    character["level"] += 1

    # Recalculate stats using the updated level (only 3 stats per tests)
    strength, magic, health = calculate_stats(
        character["class"],
        character["level"],
    )

    # Update the dictionary with new stats
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # Optional: print confirmation
    print(f"{character['name']} leveled up to Level {character['level']}!")


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Create a new character
    name = input("Enter your name: ")
    character_class_input = input(
        "Enter your class name (Warrior, Mage, Rogue, Cleric, or your custom class): "
    )
    char = create_character(name, character_class_input)
    print("Created new character!\n")
    display_character(char)

    # Level up the character
    print("\n--- Leveling Up ---")
    level_up(char)
    display_character(char)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
