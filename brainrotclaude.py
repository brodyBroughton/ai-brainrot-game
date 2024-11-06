import random
import time
from typing import Dict, List

class Character:
    def __init__(self, name: str, char_class: str):
        self.name = name
        self.char_class = char_class
        self.health = 100
        self.inventory = []
        # Base stats that will be modified based on class
        self.stats = {
            "Rizz": 50,
            "Aura": 50,
            "Skibidiness": 50
        }
        self._apply_class_modifiers()

    def _apply_class_modifiers(self):
        """Apply stat modifiers based on character class"""
        if self.char_class == "Sigma":
            self.stats["Rizz"] += 20
            self.stats["Aura"] += 10
            self.stats["Skibidiness"] -= 10
        elif self.char_class == "Beta":
            self.stats["Rizz"] -= 10
            self.stats["Aura"] += 20
            self.stats["Skibidiness"] += 10
        elif self.char_class == "Alpha":
            self.stats["Rizz"] += 10
            self.stats["Aura"] += 10
            self.stats["Skibidiness"] += 10

class Game:
    def __init__(self):
        self.player = None
        self.current_location = "Baby Gronk's House"
        self.game_state = "running"
        self.locations = {
            "Baby Gronk's House": {
                "description": "You find yourself in Baby Gronk's luxurious mansion. The air smells of baby oil and victory.",
                "connections": ["Ohio", "Talk Tuah Podcast Set"],
                "enemies": ["Baby Gronk", "Freakbob"]
            },
            "Ohio": {
                "description": "The mysterious land of Ohio. Everything feels slightly off here.",
                "connections": ["Baby Gronk's House", "Diddy's House"],
                "enemies": ["Quandale Dingle", "Ohio Resident"]
            }
            # More locations can be added
        }

    def start_game(self):
        """Initialize the game and character creation"""
        delayed_print("Welcome to AI BRAINROT RPG!")
        delayed_print("\nChoose your character class:")
        delayed_print("1. Sigma - High Rizz, Medium Aura, Low Skibidiness")
        delayed_print("2. Beta - Low Rizz, High Aura, Medium Skibidiness")
        delayed_print("3. Alpha - Balanced stats across all attributes")

        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): "))
                if choice not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                delayed_print("Please enter a valid choice (1-3)")

        class_map = {1: "Sigma", 2: "Beta", 3: "Alpha"}
        name = input("\nEnter your character's name: ")
        self.player = Character(name, class_map[choice])
        
        delayed_print(f"\nWelcome, {self.player.name} the {self.player.char_class}!")
        delayed_print("Your starting stats are:")
        for stat, value in self.player.stats.items():
            delayed_print(f"{stat}: {value}")
            while self.game_state == "running":
                delayed_print("\nYou begin your journey...")
                delayed_print(f"\nCurrent Location: {self.current_location}")
                delayed_print(self.locations[self.current_location]["description"])
                delayed_print("\nWhat would you like to do?")
                delayed_print("1. Explore")
                delayed_print("2. Check Inventory")
                delayed_print("3. Move to new location")
                
                choice = input("\nEnter your choice (1-3): ")
                
                if choice == "1":
                    if random.random() < 0.7:  # 70% chance to encounter enemy
                        enemy = random.choice(self.locations[self.current_location]["enemies"])
                        if self.combat_turn(enemy):
                            delayed_print(f"You defeated {enemy}!")
                            enemy = random.choice(self.locations[self.current_location]["enemies"])
                            if self.combat_turn(enemy):
                                drops = {
                                    "Freakbob": "Freakbob's Phone",
                                    "Baby Gronk": "Baby Gronk's Rizz", 
                                    "Ohio Resident": "Ohio Aura",
                                    "Quandale Dingle": "Quandale's Nose",
                                    "Haley": "Haley Welch's Hat",
                                    "Diddy": "Diddy's Oil"
                                }
                                item = drops.get(enemy, f"{enemy}'s Trophy")
                                self.player.inventory.append(item)
                                delayed_print(f"You obtained: {item}")
                            item = f"{enemy}'s Trophy"
                            self.player.inventory.append(item)
                            delayed_print(f"You obtained: {item}")
                        else:
                            delayed_print(f"{enemy} defeated you!")
                            self.game_state = "game_over"
                    else:
                        delayed_print("Area seems quiet...")
                    
                elif choice == "2":
                    if self.player.inventory:
                        delayed_print("\nInventory:")
                        for item in self.player.inventory:
                            delayed_print(f"- {item}")
                    else:
                        delayed_print("\nInventory is empty")
                    
                elif choice == "3":
                    delayed_print("\nAvailable locations:")
                    for i, location in enumerate(self.locations[self.current_location]["connections"], 1):
                        delayed_print(f"{i}. {location}")
                    try:
                        loc_choice = int(input("\nEnter location number: ")) - 1
                        new_location = self.locations[self.current_location]["connections"][loc_choice]
                        self.current_location = new_location
                    except (ValueError, IndexError):
                        delayed_print("Invalid choice!")

    def combat_turn(self, enemy: str) -> bool:
        """Handle a single turn of combat"""
        delayed_print(f"\nFighting {enemy}!")
        enemy_health = 100  # Base enemy health
        
        while enemy_health > 0 and self.player.health > 0:
            delayed_print(f"\nYour Health: {self.player.health}")
            delayed_print(f"Enemy Health: {enemy_health}")
            delayed_print("\nChoose your action:")
            delayed_print("1. Twerk - Light damage with chance to stun")
            delayed_print("2. Goon - Heal yourself")
            delayed_print("3. Baby Oil Shuffle - Heavy damage with instant kill chance")
            
            while True:
                try:
                    choice = int(input("\nEnter your choice (1-3): "))
                    if choice not in [1, 2, 3]:
                        raise ValueError
                    break
                except ValueError:
                    delayed_print("Please enter a valid choice (1-3)")

            if choice == 1:  # Twerk
                damage = random.randint(15, 25)
                enemy_health -= damage
                delayed_print(f"You dealt {damage} damage with your twerk!")
                if random.random() < 0.5:  # 50% chance to stun
                    delayed_print("Enemy is stunned by your moves! You get another turn!")
                    continue
                    
            elif choice == 2:  # Goon
                heal = random.randint(20, 35)
                self.player.health = min(100, self.player.health + heal)
                delayed_print(f"You healed for {heal} health!")
                
            else:  # Baby Oil Shuffle
                if random.random() < 0.1:  # 10% chance to instant kill
                    enemy_health = 0
                    delayed_print("CRITICAL HIT! Instant kill!")
                else:
                    damage = random.randint(30, 45)
                    enemy_health -= damage
                    delayed_print(f"You dealt {damage} damage with your Baby Oil Shuffle!")

            # Enemy turn (if they're still alive)
            if enemy_health > 0:
                damage = random.randint(15, 25)
                self.player.health -= damage
                delayed_print(f"\n{enemy} attacks you for {damage} damage!")

        return self.player.health > 0
def delayed_print(message: str, delay: float = 1.0) -> None:
    """Print a message with a delay.
    
    Args:
        message: The message to print
        delay: Delay in seconds before next action
    """
    print(message)
    time.sleep(delay)
def main():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()