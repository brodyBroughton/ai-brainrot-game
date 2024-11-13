import random
import time
from typing import Dict, List

# Add final boss location
RIZZLERS_CASTLE = {
    "description": "You've made it to the legendary Rizzler's Castle fr fr! The ultimate W awaits... if you can handle it 👑",
    "connections": [""],  
    "enemies": ["The Rizzler"]
}
# Add GenZ brainrot items
BRAINROT_ITEMS = [
    "fr fr Rizz Enhancer (real)",
    "No Cap Aura Crystal (bussin)",
    "Bussin Healing Juice (respectfully)",
    "Based Power Ring (W)",
    "Sheeeesh Energy Drink (ice cold)",
    "Ratio'd Enemy Debuff (ong)",
    "Main Character Energy (valid)",
    "Touch Grass Potion (grass rizz)",
    "Skull Issue Resolver (deadahh)",
    "Emotional Damage Shield (ur crazy)",
    "On God Power Up (fr fr)",
    "Caught in 4K Camera (no cap)",
    "Absolutely Zooted Boost (real)",
    "NPC Detector (based)",
    "W Rizz Elixir (its giving)"
]
# Define item effects
ITEM_EFFECTS = {
    "Freakbob's Rizz Phone (real)": {"Rizz": 10},
    "Baby Gronk's W Rizz Chain": {"Rizz": 15},
    "Cursed Ohio Aura Crystal": {"Aura": 10},
    "Quandale's Iconic Nose Ring": {"Skibidiness": 10},
    "Haley's Verified Badge": {"Aura": 5},
    "Diddy's Blessed Oil": {"Aura": 20},
    "JB's Valid Chain": {"Rizz": 10},
    "Jojo's Energy Bow": {"Skibidiness": 15},
    "fr fr Rizz Enhancer (real)": {"Rizz": 20},
    "No Cap Aura Crystal (bussin)": {"Aura": 20},
    "Bussin Healing Juice (respectfully)": {"Aura": 15},
    "Based Power Ring (W)": {"Rizz": 10},
    "Sheeeesh Energy Drink (ice cold)": {"Skibidiness": 20},
    "Ratio'd Enemy Debuff (ong)": {"Skibidiness": 15},
    "Main Character Energy (valid)": {"Rizz": 15},
    "Touch Grass Potion (grass rizz)": {"Aura": 10},
    "Skull Issue Resolver (deadahh)": {"Skibidiness": 10},
    "Emotional Damage Shield (ur crazy)": {"Aura": 5},
    "On God Power Up (fr fr)": {"Rizz": 15},
    "Caught in 4K Camera (no cap)": {"Skibidiness": 15},
    "Absolutely Zooted Boost (real)": {"Aura": 10},
    "NPC Detector (based)": {"Skibidiness": 10},
    "W Rizz Elixir (its giving)": {"Rizz": 25}
}

# Location descriptions updated with GenZ lingo
LOCATIONS = {
    "Baby Gronk's House": {
        "description": "Nah fr fr, you're in Baby Gronk's bussin mansion rn. The whole place lowkey smells like protein shakes and TikTok clout 💯. Livvy Dunne poster hittin different on the wall no cap.",
        "connections": ["Talk Tuah Podcast Set","Ohio", "Diddy's House"],
        "enemies": ["Baby Gronk", "Freakbob"]
    },
    "Ohio": {
        "description": "Ong you're in Ohio rn 💀 Everything here got that cursed energy frfr. No cap this place ain't bussin.",
        "connections": ["Baby Gronk's House", "Diddy's House", "Talk Tuah Podcast Set"],
        "enemies": ["Quandale Dingle", "Ohio Resident"]
    },
    "Talk Tuah Podcast Set": {
        "description": "Sheeeesh! The legendary podcast set do be hitting different tho 🎤 Mics still warm fr fr, that's how you know it's real.",
        "connections": ["Baby Gronk's House", "Ohio", "Diddy's House" ],
        "enemies": ["Hailey", "Jojo Siwa"]
    },
    "Diddy's House": {
        "description": "Nah this crib is actually bussin bussin fr fr. Smells like exotic oils and straight cash. Diddy's energy got the whole place on lock no cap 💅",
        "connections": ["Baby Gronk's House", "Ohio", "Talk Tuah Podcast Set", ],
        "enemies": ["Diddy", "Justin Bieber"]
    }
}

class Character:
    def __init__(self, name: str, char_class: str):
        self.name = name
        self.char_class = char_class
        self.health = 100
        self.inventory = []
        # Base stats
        self.stats = {
            "Rizz": 50,
            "Aura": 50,
            "Skibidiness": 50
        }
        self._apply_class_modifiers()

    def _apply_class_modifiers(self):
        """Apply stat modifiers based on character class"""
        if self.char_class == "Sigma":
            self.stats["Rizz"] += 2000
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

    def add_item(self, item: str):
        """Add item to inventory and apply its stat effect"""
        self.inventory.append(item)
        if item in ITEM_EFFECTS:
            for stat, increase in ITEM_EFFECTS[item].items():
                self.stats[stat] += increase
            delayed_print(f"{item} added to inventory! {stat} increased by {increase} 🥶")

class Game:

    def check_all_enemies_defeated(self) -> bool:
        """Check if all enemies in all locations have been defeated"""
        all_defeated = all(len(location["enemies"]) == 0 for location in self.locations.values())
        
        if all_defeated and self.current_location != "Rizzler's Castle":
            delayed_print("\nNAH FR FR! YOU'VE DEFEATED ALL THE OPS! 🔥")
            delayed_print("THE RIZZLER WANTS TO SEE YOU IN HIS CASTLE NO CAP! 👑")
            self.locations.update({"Rizzler's Castle": RIZZLERS_CASTLE})
            self.current_location = "Rizzler's Castle"
            
        return all_defeated


    def __init__(self):
        self.player = None
        self.current_location = "Baby Gronk's House"
        self.game_state = "running"
        self.locations = LOCATIONS

    def start_game(self):
        """Initialize the game and character creation"""
        delayed_print("YURRR! Welcome to AI BRAINROT RPG! 🔥")
        delayed_print("\nPick your vibe check (character class) fr fr:")
        delayed_print("1. Sigma - Rizz maxed out, decent Aura, mid Skibidiness (real)", delay=0.1)
        delayed_print("2. Beta - Rizz kinda mid, Aura bussin, valid Skibidiness (no cap)", delay=0.1)
        delayed_print("3. Alpha - Everything balanced fr fr (perfectly balanced as all things should be)", delay=0.1)

        while True:
            try:
                choice = int(input("\nDrop your choice (1-3) no cap: "))
                if choice not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                delayed_print("Nah fam that ain't it, try again (1-3) 💀")

        class_map = {1: "Sigma", 2: "Beta", 3: "Alpha"}
        name = input("\nDrop your character name (go crazy): ")
        self.player = Character(name, class_map[choice])
        
        delayed_print(f"\nYURRR! {self.player.name} the {self.player.char_class} HAS ENTERED THE CHAT! 🔥")
        delayed_print("\nTime to get this bread fr fr...")
        just_fought = False
        
        while self.game_state == "running":
            if self.current_location == "Baby Gronk's House":  # Only runs once at start
                self.current_location = random.choice(list(self.locations.keys()))
            delayed_print(f"\nCurrent Location (real): {self.current_location}")
            delayed_print(self.locations[self.current_location]["description"])
            delayed_print("\nWhat's the move bestie?")
            delayed_print("1. Explore the vibes", delay=0.1)
            delayed_print("2. Check the inventory check (real)", delay=0.1)
            delayed_print("3. Switch locations fr fr", delay=0.1)
            delayed_print("4. Heal up fam (costs one turn no cap)", delay=0.1)
            
            choice = input("\nWhat's good (1-4)?: ")
            
            if choice == "1":
                if just_fought:
                    delayed_print("Nah you gotta chill fr fr after that last fight... 😮‍💨")
                    just_fought = False
                elif len(self.locations[self.current_location]["enemies"]) == 0:
                    delayed_print("No ops left in this area fr fr, they all got packed 💀")
                elif random.random() < 0.7:  # 70% chance to encounter enemy  
                    enemy = random.choice(self.locations[self.current_location]["enemies"])
                    if self.combat_turn(enemy):
                        delayed_print(f"HUGE W! You just packed {enemy} fr fr! 🔥")
                        drops = {
                            "Freakbob": "Freakbob's Rizz Phone (real)",
                            "Baby Gronk": "Baby Gronk's W Rizz Chain", 
                            "Ohio Resident": "Cursed Ohio Aura Crystal",
                            "Quandale Dingle": "Quandale's Iconic Nose Ring",
                            "Haley": "Haley's Verified Badge", 
                            "Diddy": "Diddy's Blessed Oil",
                            "Justin Bieber": "JB's Valid Chain",
                            "Jojo Siwa": "Jojo's Energy Bow"
                        }
                        # Remove defeated enemy from location
                        self.locations[self.current_location]["enemies"].remove(enemy)
                        item = drops.get(enemy, f"{enemy}'s Rare W")
                        delayed_print(f"WWWW YOU GOT: {item} 🔥")
                        self.player.add_item(item)
                        
                        just_fought = True
                    else:
                        delayed_print(f"NAH {enemy} JUST VIOLATED YOU FR FR 💀")
                        self.game_state = "game_over"
                else:
                    delayed_print("Area lowkey quiet rn...")
                    if random.random() < 0.4:
                        found_item = random.choice(list(ITEM_EFFECTS.keys()))
                        delayed_print("HOLD UP WAIT A MINUTE-")
                        time.sleep(0.5)
                        delayed_print(f"NAH FR?! YOU JUST FOUND A {found_item}! THAT'S ACTUALLY CRAZY! 🔥")
                        self.player.add_item(found_item)
                
            elif choice == "2":
                if self.player.inventory:
                    delayed_print("\nInventory check (real real):")
                    for item in self.player.inventory:
                        delayed_print(f"- {item} ✨ (W rizz)")
                else:
                    delayed_print("\nNah inventory empty fr fr no cap 💀")
                
            elif choice == "3":
                delayed_print("\nWhere we dropping? 👀")
                for i, location in enumerate(self.locations[self.current_location]["connections"], 1):
                    delayed_print(f"{i}. {location} (valid fr)", delay=0.1)
                try:
                    loc_choice = int(input("\nDrop the location number bestie: ")) - 1
                    new_location = self.locations[self.current_location]["connections"][loc_choice]
                    self.current_location = new_location
                    just_fought = False
                except (ValueError, IndexError):
                    print("Nah that ain't it fam 💀")

            elif choice == "4":
                heal_amount = random.randint(20, 35)
                self.player.health = min(100, self.player.health + heal_amount)
                delayed_print(f"HUGE W! Healed for {heal_amount}! Current health: {self.player.health} (valid)")

    def combat_turn(self, enemy: str) -> bool:
        """Handle a single turn of combat"""
        delayed_print(f"\nNAH {enemy} WANTS THE SMOKE FR FR! 😤")
        enemy_health = 100
        
        while enemy_health > 0 and self.player.health > 0:
            delayed_print(f"\nYour Health: {self.player.health} (real)", delay=0.1)
            delayed_print(f"{enemy}'s Health: {enemy_health} (fr fr)", delay=0.1)
            delayed_print("\nWhat's the move?!")
            delayed_print("1. Twerk (light damage + stun chance no cap)", delay=0.1)
            delayed_print("2. Goon (heal up fr fr)", delay=0.1)
            delayed_print("3. Baby Oil Shuffle (HEAVY DAMAGE + rare instant kill)", delay=0.1)
            
            choice = int(input("\nPick your move (1-3) expeditiously: "))

            if choice == 1:  # Twerk
                # Damage scales with Rizz stat
                damage = random.randint(10, 20) + int(self.player.stats["Rizz"] * 0.2)
                enemy_health -= damage
                delayed_print(f"YOUR TWERK JUST DID {damage} DAMAGE! GYATT! 😳")
                
                # Stun chance scales with Skibidiness
                if random.random() < self.player.stats["Skibidiness"] / 100:
                    delayed_print("NAH THEY'RE STUNNED BY THE MOVEMENT! GO CRAZY! 🔥")
                    continue

            elif choice == 2:  # Goon
                # Healing scales with Aura stat
                heal = random.randint(15, 25) + int(self.player.stats["Aura"] * 0.2)
                self.player.health = min(100, self.player.health + heal)
                delayed_print(f"YOU JUST HEALED {heal}! W RIZZ! 💯")
                
            elif choice == 3:  # Baby Oil Shuffle
                # Instant kill chance scales with Skibidiness
                if random.random() < self.player.stats["Skibidiness"] / 200:
                    enemy_health = 0
                    delayed_print("NAH THAT'S CRAZY! INSTANT KILL! YOU'RE HIM FR FR! 🐐")
                else:
                    # Heavy damage scales with Rizz stat
                    damage = random.randint(25, 40) + int(self.player.stats["Rizz"] * 0.3)
                    enemy_health -= damage
                    delayed_print(f"BABY OIL SHUFFLE DAMAGE: {damage}! SHEEEESH! 🥶")

            if enemy_health > 0:
                # Enemy attacks player if still alive
                damage = random.randint(15, 25)
                self.player.health -= damage
                delayed_print(f"\n{enemy} JUST VIOLATED YOU FOR {damage} DAMAGE! 💀")

        return self.player.health > 0

def delayed_print(message: str, delay: float = 0.5) -> None:
    """Print a message with a delay."""
    print(message)
    time.sleep(delay)

def main():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()