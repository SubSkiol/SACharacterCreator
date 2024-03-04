import random as ran

class CharacterOptions:
    """Data that the randomizer will pull from.
    These values can be freely changed"""

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
            "tech_level":["Atavistic","Advanced","On par with humans","Hyper Advanced",
                "Slightly Less","Slightly More"],
    
            # Below is True Alien Only
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
            # More?
        }
    
    @staticmethod
    def monster_options():
        return {
            "alignment":["Chaotic Good","Chaotic Evil","Neutral","True Evil","True Good"],
            "type":["Cryptid","Spider","Dragon","Skinwalker","Mythical","Zombie","Vampire",
                "Werewolf","Ghost","Ghoul","Demon","Wraith","Wendigo","Chupacabra","Banshee",
                "Mummy","Kraken","Griffin","Cyclops","Nymph","Chimera"],
        }

character_options = CharacterOptions()

# Store random Class
class CharacterBuilder():
    """Grabs data from the above class, then builds the character."""

    @staticmethod
    def base_attributes():
        return {
            "topics":["Topic: ", ran.choice(character_options.base_attributes()["topics"])],
            "gender":["Gender: ", ran.choice(character_options.base_attributes()["gender"])],
            "build":["Build: ", ran.choice(character_options.base_attributes()["build"])],
            "hair":["Hair: ", ran.choice(character_options.base_attributes()["hair"])],
            "hair_color":["Hair Color: ",
                ran.choice(character_options.base_attributes()["hair_color"])],
        }
    
    @staticmethod
    def human_options():
        return {
            "occupation":["Occupation: ",
                ran.choice(character_options.human_options()["occupation"])],

            "clothing_style":["Clothing Stye: ",
                ran.choice(character_options.human_options()["clothing_style"])],

            "ethnicity":["Ethnicity: ", ran.choice(character_options.human_options()["ethnicity"])],
            "nationality":["Nationality: ",
                ran.choice(character_options.human_options()["nationality"])],

            "age":["Age: ", ran.choice(character_options.human_options()["age"])],
            "facial_features":["Features: ",
                ran.choice(character_options.human_options()["facial_features"])],
        }
    
    @staticmethod
    def alien_options():
        return {
            "type": ["Alien Type: ", ran.choice(character_options.alien_options()["type"])],
            "tech_level": ["Tech Level: ",
                ran.choice(character_options.alien_options()["tech_level"])],
        }
    
    @staticmethod
    def true_alien_options():
        return {
            "eye_number": ["Eye Number: ",
                ran.choice(character_options.alien_options()["eye_number"])],
            
            "limb_number": ["Limb Number: ",
                ran.choice(character_options.alien_options()["limb_number"])],
            
            "pattern": ["Pattern: ", ran.choice(character_options.alien_options()["pattern"])],
            "antenna": ["Antenna: ", ran.choice(character_options.alien_options()["antenna"])],
            "leg_type": ["Leg Type: ", ran.choice(character_options.alien_options()["leg_type"])],    
        }

    @staticmethod
    def animal_options():
        return {
            "species": ["Species: ", ran.choice(character_options.animal_options()["species"])],
            "pattern": ["Animal Pattern: ",
                ran.choice(character_options.animal_options()["pattern"])],

            "size": ["Size: ", ran.choice(character_options.animal_options()["size"])],
        }

    @staticmethod
    def monster_options():
        return {
            "alignment": ["Alignment: ",
                ran.choice(character_options.monster_options()["alignment"])],

            "type": ["Monster Type: ", ran.choice(character_options.monster_options()["type"])],
        }

