base_attributes = {
    "topics":["Human","Alien","Animal","Monster"],
    "gender":["male","female","ambiguous"],
    "build":["Obese","Fat","Chubby","Healthy","Lean","Skinny","Underweight"],
    "hair":["Long","Medium","Short",None],
    "hair_color":["Red","Orange","Yellow","Green","Blue","Purple","Black","White"],
}
human_options = {
    "occupation":["Engineer","Artist","Doctor","Teacher","Pilot","Scientist","Musician"],
    "clothing_style":["Casual","Formal","Sporty","Bohemian","Business Casual","Vintage"],
    "ethnicity":["Caucasian","African American","Asian","Hispanic","Middle Eastern"],
    "nationality":["American","Chinese","Indian","Russian","Brazilian"],
    "age":list(range(0,100)),
    "facial_features":["Scar","Tattoo","Piercing","Burn"],
}

alien_options = {
    "type":["Humanoid","Animalistic","Animal Humanoid","True Alien"],
    "home planet":["Xenon","Zephyrion","Quadrantia","Nebulon"],
    "tech level":["Atavistic","Advanced","On par with humans","Hyper Advanced","Slightly Less","Slightly More"],
    #True Alien Only
    "eye_number":list(range(1,8)),
    "limb_number":list(range(2,9,2)),
    "pattern":[None,"Spotted","Splotches","Digital Camo","Striped","Swirl"],
    "Antenna":[True,False],
    "leg_type":["Tentacles","Digitigrade","Plantigrade","Hooves"],
}

animal_options = {
    "species":["Lion","Tiger","Penguin","Elephant","Kangaroo"],
    "pattern":["Striped","Spotted","Spiral","Zigzag"],
    "size":["Tiny","Small","Realistic","Large","Comically Big"],
    #More?
}

monster_options = {
    "alignment":["Chaotic Good","Chaotic Evil","Neutral","True Evil","True Good"],
    "type":["Cryptid","Spider","Dragon","Skinwalker","Mythical","Zombie","Vampire","Werewolf","Ghost",
            "Ghoul","Demon","Wraith","Wendigo","Chupacabra","Banshee","Mummy","Kraken","Griffin",
            "Cyclops","Nymph","Chimera"],
}
