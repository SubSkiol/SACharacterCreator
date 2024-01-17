import random as ran
from typing import Optional
from colorama import Fore, init


#The choices can be added to, or removed from. 
class CharacterOptions:
    
    @staticmethod
    def base_attributes():
        return {
            "topics":["Human","Alien","Animal","Monster"],
            "gender":["Male","Female","Ambiguous"],
            "build":["Obese","Fat","Chubby","Healthy","Lean","Skinny","Underweight"],
            "hair":["Long","Medium","Short",None],
            "hair_color":["Red","Orange","Yellow","Green","Blue","Purple","Black","White"],
        }
    
    @staticmethod
    def human_options():
        return {
            "occupation":["Engineer","Artist","Doctor","Teacher","Pilot","Scientist","Musician"],
            "clothing_style":["Casual","Formal","Sporty","Bohemian","Business Casual","Vintage"],
            "ethnicity":["Caucasian","African American","Asian","Hispanic","Middle Eastern"],
            "nationality":["American","Chinese","Indian","Russian","Brazilian"],
            "age":list(range(0,100)),
            "facial_features":["Scar","Tattoo","Piercing","Burn"],
        }
    
    @staticmethod
    def alien_options():
        return {
            "type":["Humanoid","Animalistic","Animal Humanoid","True Alien"],
            "tech_level":["Atavistic","Advanced","On par with humans","Hyper Advanced","Slightly Less","Slightly More"],
            #Below is True Alien Only
            "eye_number":list(range(1,8)),
            "limb_number":list(range(2,9,2)),
            "pattern":[None,"Spotted","Splotches","Digital Camo","Striped","Swirl"],
            "antenna":[True,False],
            "leg_type":["Tentacles","Digitigrade","Plantigrade","Hooves"],
        }
    
    @staticmethod
    def animal_options():
        return {
            "species":["Lion","Tiger","Penguin","Elephant","Kangaroo"],
            "pattern":["Striped","Spotted","Spiral","Zigzag","Solid"],
            "size":["Tiny","Small","Realistic","Large","Comically Big"],
            #More?
        }
    
    @staticmethod
    def monster_options():
        return {
            "alignment":["Chaotic Good","Chaotic Evil","Neutral","True Evil","True Good"],
            "type":["Cryptid","Spider","Dragon","Skinwalker","Mythical","Zombie","Vampire","Werewolf","Ghost",
                    "Ghoul","Demon","Wraith","Wendigo","Chupacabra","Banshee","Mummy","Kraken","Griffin",
                    "Cyclops","Nymph","Chimera"],
        }
character_options = CharacterOptions()

#Store random Class
class CharacterBuilder():
    
    @staticmethod
    def base_attributes():
        return {
            "topics":["Topic: ", ran.choice(character_options.base_attributes()["topics"])],
            "gender":["Gender: ", ran.choice(character_options.base_attributes()["gender"])],
            "build":["Build: ", ran.choice(character_options.base_attributes()["build"])],
            "hair":["Hair: ", ran.choice(character_options.base_attributes()["hair"])],
            "hair_color":["Hair Color: ", ran.choice(character_options.base_attributes()["hair_color"])],
        }
    
    @staticmethod
    def human_options():
        return {
            "occupation":["Occupation: ", ran.choice(character_options.human_options()["occupation"])],
            "clothing_style":["Clothing Stye: ", ran.choice(character_options.human_options()["clothing_style"])],
            "ethnicity":["Ethnicity: ", ran.choice(character_options.human_options()["ethnicity"])],
            "nationality":["Nationality: ", ran.choice(character_options.human_options()["nationality"])],
            "age":["Age: ", ran.choice(character_options.human_options()["age"])],
            "facial_features":["Features: ", ran.choice(character_options.human_options()["facial_features"])],
        }
    
    @staticmethod
    def alien_options():
        return {
            "type": ["Alien Type: ", ran.choice(character_options.alien_options()["type"])],
            "tech_level": ["Tech Level: ", ran.choice(character_options.alien_options()["tech_level"])],
            #True Alien settigns moved to true_alien_options
        }
    
    @staticmethod
    def true_alien_options():
        return {
            "eye_number": ["Eye Number: ", ran.choice(character_options.alien_options()["eye_number"])],
            "limb_number": ["Limb Number: ", ran.choice(character_options.alien_options()["limb_number"])],
            "pattern": ["Pattern: ", ran.choice(character_options.alien_options()["pattern"])],
            "antenna": ["Antenna: ", ran.choice(character_options.alien_options()["antenna"])],
            "leg_type": ["Leg Type: ", ran.choice(character_options.alien_options()["leg_type"])],
            }
    @staticmethod
    def animal_options():
        return {
            "species": ["Species: ", ran.choice(character_options.animal_options()["species"])],
            "pattern": ["Animal Pattern: ", ran.choice(character_options.animal_options()["pattern"])],
            "size": ["Size: ", ran.choice(character_options.animal_options()["size"])],
        }
    
    @staticmethod
    def monster_options():
        return {
            "alignment": ["Alignment: ", ran.choice(character_options.monster_options()["alignment"])],
            "type": ["Monster Type: ", ran.choice(character_options.monster_options()["type"])],
        }
character_builder = CharacterBuilder()

def print_handler(to_print, pretext: Optional[str] = ""): # making a function for this as I may decide to reformat the order at which everything is printed and in what style (EG yes or no colorama)
    print(f"{Fore.MAGENTA}{pretext}{Fore.LIGHTCYAN_EX}{to_print}{Fore.RESET}")

#For Human characters, or characters with human characteristics
def human_handler():
    print(f"{Fore.LIGHTGREEN_EX}--HUMAN CHARACTERISTICS--")
    for key in character_builder.human_options().keys():
        print_handler(character_builder.human_options()[key][1], pretext=character_builder.human_options()[key][0])


    
            
#For ANIMAL characters, or characters with ANIMAL characteristics
def animal_handler():
    print(f"{Fore.LIGHTGREEN_EX}--ANIMAL CHARACTERISTICS--")
    for key in character_builder.animal_options().keys():
        print_handler(character_builder.animal_options()[key][1], pretext=character_builder.animal_options()[key][0]) 

#For ALIEN characters, or characters with ALIEN characteristics
def alien_handler():
    print(f"{Fore.LIGHTGREEN_EX}--ALIEN CHARACTERISTICS--")
    chosen_alien_type = character_builder.alien_options()["type"][1] #handle type different as True Alien relies on it
    print_handler(chosen_alien_type, pretext=character_builder.alien_options()["type"][0])
    
    print_handler(character_builder.alien_options()["tech_level"][1], pretext=character_builder.alien_options()["tech_level"][0]) #Not enough to make a full for loop

    if chosen_alien_type == "True Alien":
        for key in character_builder.true_alien_options().keys():
            print_handler(character_builder.true_alien_options()[key][1], pretext=character_builder.true_alien_options()[key][0])
    #"Humanoid","Animalistic","Animal Humanoid"
    if chosen_alien_type == "Humanoid":
        human_handler()
    if chosen_alien_type == "Animalistic":
        animal_handler()
    if chosen_alien_type == "Animal Humanoid":
        human_handler()
        animal_handler()
        
#For monster characters, or characters with monster characteristics
def monster_handler():
    for key in character_builder.monster_options().keys():
        print_handler(character_builder.monster_options()[key][1], pretext=character_builder.monster_options()[key][0])

def base_handler(bypass: Optional[bool] = False):
    print(f"{Fore.LIGHTGREEN_EX}\n--CHARACTERISTICS--")
    if not bypass:
        chosen_character_base = character_builder.base_attributes()["topics"][1] #handle topics different than the rest as topics has specific tasks relying on what it is. 
        print_handler(chosen_character_base, pretext=character_builder.base_attributes()["topics"][0])
    
    for key in ["gender", "build"]: #both of these are handled as normal
        print_handler(character_builder.base_attributes()[key][1], pretext=character_builder.base_attributes()[key][0])

    #Hair and hair color are handled differently as hair can be None, and in that senario we no longer want to print a hair color
    chosen_hair_length = character_builder.base_attributes()["hair"][1]
    print_handler(chosen_hair_length, pretext=character_builder.base_attributes()["hair"][0])
    
    if chosen_hair_length is not None:
        print_handler(character_builder.base_attributes()["hair_color"][1], pretext=character_builder.base_attributes()["hair_color"][0])
        
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


#Main Program
def main():
    main_loop = True
    
    #Various Variables
    version_name = "SubAlternate's Creativity Assistant (Colorama Enabled)"
    version_number = "Version 4.1"
    
    print(f"{Fore.RED}Runing {version_name} {version_number}")
    while main_loop:
        main_input = input(f"{Fore.LIGHTGREEN_EX}\n(R)andomize (Q)uit\nHuman, Animal, Alien, Monster\n{Fore.RESET}")
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
            
        else:
            print(f"{Fore.YELLOW}{main_input} is not a valid input!")

if __name__ == "__main__":
    init(autoreset=True)
    main()


