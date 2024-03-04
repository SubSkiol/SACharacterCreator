from colorama import Fore, init
from character_data import CharacterBuilder

character_builder = CharacterBuilder()

# BEGIN HANDLER SECTION
def print_handler(to_print, pretext=""):
    """Handles cases of printing the character lists"""

    print(f"{Fore.MAGENTA}{pretext}{Fore.LIGHTCYAN_EX}{to_print}{Fore.RESET}")


def human_handler():
    """Handles any instance of humanoid characteristics.
    This includes humans and any character with human specific characteristics"""

    print(f"{Fore.LIGHTGREEN_EX}--HUMAN CHARACTERISTICS--") # Anouncement for user friendliness
    for key in character_builder.human_options():
        print_handler(character_builder.human_options()[key][1],
                pretext=character_builder.human_options()[key][0]) # Print the characteristics

def animal_handler():
    """Handles any instance of animalistic characters.
    This includes animals and any character with animalistic characteristics"""

    print(f"{Fore.LIGHTGREEN_EX}--ANIMAL CHARACTERISTICS--")
    for key in character_builder.animal_options():
        print_handler(character_builder.animal_options()[key][1],
                pretext=character_builder.animal_options()[key][0])

def alien_handler():
    """Handles any instance of alien characteristics
    This includes aliens and any character with alien characteristics"""

    print(f"{Fore.LIGHTGREEN_EX}--ALIEN CHARACTERISTICS--")

    chosen_alien_type = character_builder.alien_options()["type"][1] 
    # Store for later

    for key in character_builder.alien_options():
        print_handler(character_builder.alien_options()[key][1],
                pretext=character_builder.alien_options()[key][0])

    if chosen_alien_type == "True Alien": # Handle instances of True Alien Separately
        for key in character_builder.true_alien_options():
            print_handler(character_builder.true_alien_options()[key][1],
                    pretext=character_builder.true_alien_options()[key][0])

    if chosen_alien_type == "Humanoid":
        human_handler()

    if chosen_alien_type == "Animalistic":
        animal_handler()

    if chosen_alien_type == "Animal Humanoid":
        human_handler()
        animal_handler()

def monster_handler():
    """Handles any instance of monster characteristics
    This includes monsters and any character with monster characteristics"""

    for key in character_builder.monster_options():
        print_handler(character_builder.monster_options()[key][1],
                pretext=character_builder.monster_options()[key][0])

def base_handler(bypass=False):
    """Handles all base attributes
    Most characters will use this, and it will also start other handlers"""

    print(f"{Fore.LIGHTGREEN_EX}\n--CHARACTERISTICS--")
    if not bypass:
        chosen_character_base = character_builder.base_attributes()["topics"][1] 
        #handle topics different than the rest as topics has specific tasks relying on what it is

        print_handler(chosen_character_base,
                pretext=character_builder.base_attributes()["topics"][0])
    
    for key in ["gender", "build"]: #both of these are handled as normal
        print_handler(character_builder.base_attributes()[key][1],
                pretext=character_builder.base_attributes()[key][0])
    
    """
    Hair and hair color are handled differently as hair can be None
    in that senario we no longer want to print a hair color
    """

    chosen_hair_length = character_builder.base_attributes()["hair"][1]
    print_handler(chosen_hair_length, pretext=character_builder.base_attributes()["hair"][0])

    if chosen_hair_length is not None:
        print_handler(character_builder.base_attributes()["hair_color"][1],
                pretext=character_builder.base_attributes()["hair_color"][0])
        
    if not bypass:
        #Start the other handlers 
        if chosen_character_base == "Human":
            human_handler()
        if chosen_character_base == "Alien":
            alien_handler()
        if chosen_character_base == "Animal":
            animal_handler()
        if chosen_character_base == "Monster":
            monster_handler()    

def main():
    """Main program.
    This handes what the user wants to do, and is the main CLI environment
    """

    main_loop = True

    # Various Variables
    version_name = "SubAlternate's Creativity Assistant"
    version_number = "Version 4.2"

    print(f"Runing {version_name} {version_number}")
    while main_loop:
        
        print(f"{Fore.LIGHTGREEN_EX}(R)andomize / (q)uit\n"+
                f"{Fore.LIGHTGREEN_EX}Other options: Human | Animal | Alien | Monster | Clear")
        main_input = input()

        if main_input.lower() == "r":
            base_handler()

        elif main_input.lower() == "q":
            main_loop = False

        elif main_input.lower() == "human":
            base_handler(bypass=True)
            human_handler()

        elif main_input.lower() == "alien":
            base_handler(bypass=True)
            alien_handler()

        elif main_input.lower() == "animal":
            base_handler(bypass=True)
            animal_handler()
    
        elif main_input.lower() == "monster":
            base_handler(bypass=True)
            monster_handler()

        elif main_input.lower() == "clear":
            print('\033c')

        else:
            print(f"{Fore.YELLOW}'{main_input}' is not a valid input!")

if __name__ == "__main__":
    init(autoreset=True)
    main()

