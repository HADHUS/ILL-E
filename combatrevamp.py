#<| CURRENT FILE: ~/HADHUSlib.py |>#
#generative data handler that is currently unused
'''
"gen_data": {
            #spawn chance modifiers (-1 = disabled) | min = -1 | max = 1
            "northernsea_MOD": -1,
            "twilighttundra_MOD": -1,
            "shatteredtaiga_MOD": -1,
            "oakensanctuary_MOD": -1,
            "lakeoya_MOD": -1,
            "scintillantrainforest_MOD": -1,
            "darksporeforest_MOD": -1,
            "bogofmangroves_MOD": -1,
            "distantmeadows_MOD": -1,
            "savagesteppe_MOD": -1,
            "verdanthills_MOD": -1,
            "skygrassprairie_MOD": -1,
            "sandyshores_MOD": -1,
            "southeastsea_MOD": -1,
            "forsakenkarst_MOD": -1,
            "sunsetmesa_MOD": -1,
            "islerho_MOD": -1,
            "isletheta_MOD": -1,
            "cragrockbelt_MOD": -1,
            "peaksofdespair_MOD": -1,
            "embersreach_MOD": -1,
            "cloudedspires_MOD": -1
        }
'''

enemies = {
    "goblin": {
        "general": {
            "enemyname": "goblin",
            "enemyhp": 6,
            "enemyac": 12,
            "enemydmg1": 2,
            "enemydmg2": None,
            "enemyacc": 1,
            "enemyweapon1": "charges you and slashes at you with a worn blade.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 0,
            "LOOTsilv": 2,
            "LOOTcopp": 0,
            "LOOTitem1": "goblin sword",
            "LOOTitem2": "goblin war paint",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 8,
            "LtProb2": 20,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "goblin striker": {
        "general": {
            "enemyname": "goblin striker",
            "enemyhp": 13,
            "enemyac": 14,
            "enemydmg1": 4,
            "enemydmg2": None,
            "enemyacc": 3,
            "enemyweapon1": "slashes out with a mighty spiked blade.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 2,
            "LOOTsilv": 0,
            "LOOTcopp": 0,
            "LOOTitem1": "striker blade",
            "LOOTitem2": "scrap metal",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 14,
            "LtProb2": 2,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "goblin sniper": {
        "general": {
            "enemyname": "goblin sniper",
            "enemyhp": 11,
            "enemyac": 16,
            "enemydmg1": 5,
            "enemydmg2": None,
            "enemyacc": 5,
            "enemyweapon1": "fires a deadly shot!",
            "enemyweapon2": None,
            "special1": "scover",
            "special2": None,
            "special3": None,
            "damagetype": "ranged",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 1,
            "LOOTsilv": 0,
            "LOOTcopp": 0,
            "LOOTitem1": "heavytip quiver",
            "LOOTitem2": "reload crank",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 10,
            "LtProb2": 12,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "outlaw": {
        "general": {
            "enemyname": "outlaw",
            "enemyhp": 7,
            "enemyac": 13,
            "enemydmg1": 2,
            "enemydmg2": None,
            "enemyacc": 3,
            "enemyweapon1": "stabs you with a rusty dagger.  Ouch.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 0,
            "LOOTsilv": 7,
            "LOOTcopp": 0,
            "LOOTitem1": "rusty dagger",
            "LOOTitem2": "outlaw bandana",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 10,
            "LtProb2": 15,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "orc": {
        "general": {
            "enemyname": "orc",
            "enemyhp": 8,
            "enemyac": 11,
            "enemydmg1": 3,
            "enemydmg2": None,
            "enemyacc": 2,
            "enemyweapon1": "makes a mighty swing with a battleaxe.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 0,
            "LOOTsilv": 6,
            "LOOTcopp": 0,
            "LOOTitem1": "orcish battleaxe",
            "LOOTitem2": "leather vest",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 10,
            "LtProb2": 12,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "orcish shaman": {
        "general": {
            "enemyname": "orcish shaman",
            "enemyhp": 15,
            "enemyac": 13,
            "enemydmg1": 0,
            "enemydmg2": None,
            "enemyacc": 0,
            "enemyweapon1": "raises a staff and pounds it on the floor, strengthening its allies.",
            "enemyweapon2": None,
            "special1": "orcboost",
            "special2": None,
            "special3": None,
            "damagetype": "generic",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 1,
            "LOOTsilv": 3,
            "LOOTcopp": 0,
            "LOOTitem1": "amulet of life",
            "LOOTitem2": "shaman's staff",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 20,
            "LtProb2": 15,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "darkling": {
        "general": {
            "enemyname": "darkling",
            "enemyhp": 8,
            "enemyac": 9,
            "enemydmg1": 3,
            "enemydmg2": None,
            "enemyacc": 1,
            "enemyweapon1": "slashes at you with a dark knife.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 0,
            "LOOTsilv": 4,
            "LOOTcopp": 0,
            "LOOTitem1": "amber",
            "LOOTitem2": "shadow knife",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 5,
            "LtProb2": 8,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "elf brute": {
        "general": {
            "enemyname": "elf brute",
            "enemyhp": 15,
            "enemyac": 10,
            "enemydmg1": 4,
            "enemydmg2": None,
            "enemyacc": 1,
            "enemyweapon1": "swings a mighty warhammer.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 0,
            "LOOTsilv": 8,
            "LOOTcopp": 0,
            "LOOTitem1": "iron ingot",
            "LOOTitem2": "leather vest",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 6,
            "LtProb2": 10,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "prairie bulette": {
        "general": {
            "enemyname": "prairie bulette",
            "enemyhp": 22,
            "enemyac": 12,
            "enemydmg1": 7,
            "enemydmg2": None,
            "enemyacc": 3,
            "enemyweapon1": "erupts from the ground next to you and pounces.",
            "enemyweapon2": None,
            "special1": "burrow",
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": True,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 1,
            "LOOTgold": 4,
            "LOOTsilv": 0,
            "LOOTcopp": 0,
            "LOOTitem1": "scrap metal",
            "LOOTitem2": "scrap metal",
            "LOOTitem3": "bulette hide",
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 4,
            "LtProb2": 4,
            "LtProb3": 10,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "mage": { #arrowfall crossover boss
        "general": {
            "enemyname": "mage",
            "enemyhp": 45,
            "enemyac": 12,
            "enemydmg1": 5,
            "enemydmg2": None,
            "enemyacc": 3,
            "enemyweapon1": "A bolt of dark energy is fired at you.",
            "enemyweapon2": None,
            "special1": "darken",
            "special2": "drain",
            "special3": "shadoworb",
            "damagetype": "magic",
            "ignoreDR": False,
            "atkbonus": 6
        },
        "loot": {
            "LOOTplat": 4,
            "LOOTgold": 5,
            "LOOTsilv": 0,
            "LOOTcopp": 0,
            "LOOTitem1": "hails of arrows tome",
            "LOOTitem2": "lifedrain staff",
            "LOOTitem3": "book of shadows",
            "LOOTitem4": "mage's robe",
            "LOOTitem5": None,
            "LtProb1": 25,
            "LtProb2": 25,
            "LtProb3": 25,
            "LtProb4": 25,
            "LtProb5": None
        }
    },
    "serpenite": {
        "general": {
            "enemyname": "serpenite",
            "enemyhp": 13,
            "enemyac": 13,
            "enemydmg1": 4,
            "enemydmg2": None,
            "enemyacc": 3,
            "enemyweapon1": "slashes at you with a shiny knife.",
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": "melee",
            "ignoreDR": False,
            "atkbonus": 0
        },
        "loot": {
            "LOOTplat": 0,
            "LOOTgold": 1,
            "LOOTsilv": 3,
            "LOOTcopp": 0,
            "LOOTitem1": "fish scales",
            "LOOTitem2": "steel dagger",
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": 1,
            "LtProb2": 4,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
}

#<| FILE END |>#

#<| CURRENT FILE: ~/main.py |>#
import HADHUSlib as HADLib
#...
def las(listc):
  laas = ", ".join(listc)
  print("[" + laas + "]")
player = {
    "general": {
        "name": None,
        "sclass": None,
        "location": "tutorial",
    },
    "stats": {
        "hunger": 10,
        "maxhunger": 10,
        "hp": 0,
        "maxhp": 0


    }
}
activeenemies = {
    1: {
        "general": {
            "enemyname": None,
            "enemyhp": None,
            "enemyac": None,
            "enemydmg1": None,
            "enemydmg2": None,
            "enemyacc": None,
            "enemyweapon1": None,
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": None,
            "ignoreDR": None,
            "atkbonus": None
        },
        "loot": {
            "LOOTplat": None,
            "LOOTgold": None,
            "LOOTsilv": None,
            "LOOTcopp": None,
            "LOOTitem1": None,
            "LOOTitem2": None,
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": None,
            "LtProb2": None,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    2: {
        "general": {
            "enemyname": None,
            "enemyhp": None,
            "enemyac": None,
            "enemydmg1": None,
            "enemydmg2": None,
            "enemyacc": None,
            "enemyweapon1": None,
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": None,
            "ignoreDR": None,
            "atkbonus": None
        },
        "loot": {
            "LOOTplat": None,
            "LOOTgold": None,
            "LOOTsilv": None,
            "LOOTcopp": None,
            "LOOTitem1": None,
            "LOOTitem2": None,
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": None,
            "LtProb2": None,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    3: {
        "general": {
            "enemyname": None,
            "enemyhp": None,
            "enemyac": None,
            "enemydmg1": None,
            "enemydmg2": None,
            "enemyacc": None,
            "enemyweapon1": None,
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": None,
            "ignoreDR": None,
            "atkbonus": None
        },
        "loot": {
            "LOOTplat": None,
            "LOOTgold": None,
            "LOOTsilv": None,
            "LOOTcopp": None,
            "LOOTitem1": None,
            "LOOTitem2": None,
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": None,
            "LtProb2": None,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    },
    "reset": { #used to clear active enemy slots
        "general": {
            "enemyname": None,
            "enemyhp": None,
            "enemyac": None,
            "enemydmg1": None,
            "enemydmg2": None,
            "enemyacc": None,
            "enemyweapon1": None,
            "enemyweapon2": None,
            "special1": None,
            "special2": None,
            "special3": None,
            "damagetype": None,
            "ignoreDR": None,
            "atkbonus": None
        },
        "loot": {
            "LOOTplat": None,
            "LOOTgold": None,
            "LOOTsilv": None,
            "LOOTcopp": None,
            "LOOTitem1": None,
            "LOOTitem2": None,
            "LOOTitem3": None,
            "LOOTitem4": None,
            "LOOTitem5": None,
            "LtProb1": None,
            "LtProb2": None,
            "LtProb3": None,
            "LtProb4": None,
            "LtProb5": None
        }
    }
}
#...
#it is assumed that there are enemies in the 'enemies' list
def combat(inprog = False, e1= None, e2 = None, e3 = None):
    global activeenemies
    effect1dur = 0
    effect2dur = 0
    effect3dur = 0
    def roll(sides = 20):
        return random.randint(1, sides)
    def read_enemies():
        if e1 != None:
            #define what enemy it is
            activeenemies[1]["general"]["enemyname"] = e1
            #write HADLib.enemies entry to activeenemies for e1
            activeenemies[1]["general"]["enemyname"] = HADLib.enemies[e1]["general"]["enemyname"]
            activeenemies[1]["general"]["enemyhp"] = HADLib.enemies[e1]["general"]["enemyhp"]
            activeenemies[1]["general"]["enemyac"] = HADLib.enemies[e1]["general"]["enemyac"]
            activeenemies[1]["general"]["enemydmg1"] = HADLib.enemies[e1]["general"]["enemydmg1"]
            if HADLib.enemies[e1]["general"]["enemydmg2"] == None:
                activeenemies[1]["general"]["enemydmg2"] = None
            activeenemies[1]["general"]["enemyacc"] = HADLib.enemies[e1]["general"]["enemyacc"]
            activeenemies[1]["general"]["enemyweapon1"] = HADLib.enemies[e1]["general"]["enemyweapon1"]
            if HADLib.enemies[e1]["general"]["enemyweapon2"] == None:
                activeenemies[1]["general"]["enemyweapon2"] = None
            if HADLib.enemies[e1]["general"]["special1"] == None:
                activeenemies[1]["general"]["special1"] = None
            if HADLib.enemies[e1]["general"]["special2"] == None:
                activeenemies[1]["general"]["special2"] = None
            if HADLib.enemies[e1]["general"]["special3"] == None:
                activeenemies[1]["general"]["special3"] = None
            activeenemies[1]["general"]["damagetype"] = HADLib.enemies[e1]["general"]["damagetype"]
            activeenemies[1]["general"]["ignoreDR"] = HADLib.enemies[e1]["general"]["ignoreDR"]
            activeenemies[1]["general"]["atkbonus"] = HADLib.enemies[e1]["general"]["atkbonus"]
            #write HADLib.enemies loot entry to activeenemies for e1
            activeenemies[1]["loot"]["LOOTplat"] = HADLib.enemies[e1]["loot"]["LOOTplat"]
            activeenemies[1]["loot"]["LOOTgold"] = HADLib.enemies[e1]["loot"]["LOOTgold"]
            activeenemies[1]["loot"]["LOOTsilv"] = HADLib.enemies[e1]["loot"]["LOOTsilv"]
            activeenemies[1]["loot"]["LOOTcopp"] = HADLib.enemies[e1]["loot"]["LOOTcopp"]
            if HADLib.enemies[e1]["loot"]["LOOTitem1"] == None:
                activeenemies[1]["loot"]["LOOTitem1"] = None
            if HADLib.enemies[e1]["loot"]["LOOTitem2"] == None:
                activeenemies[1]["loot"]["LOOTitem2"] = None
            if HADLib.enemies[e1]["loot"]["LOOTitem3"] == None:
                activeenemies[1]["loot"]["LOOTitem3"] = None
            if HADLib.enemies[e1]["loot"]["LOOTitem4"] == None:
                activeenemies[1]["loot"]["LOOTitem4"] = None
            if HADLib.enemies[e1]["loot"]["LOOTitem5"] == None:
                activeenemies[1]["loot"]["LOOTitem5"] = None
            if HADLib.enemies[e1]["loot"]["LtProb1"] == None:
                activeenemies[1]["loot"]["LtProb1"] = None
            if HADLib.enemies[e1]["loot"]["LtProb2"] == None:
                activeenemies[1]["loot"]["LtProb2"] = None
            if HADLib.enemies[e1]["loot"]["LtProb3"] == None:
                activeenemies[1]["loot"]["LtProb3"] = None
            if HADLib.enemies[e1]["loot"]["LtProb4"] == None:
                activeenemies[1]["loot"]["LtProb4"] = None
            if HADLib.enemies[e1]["loot"]["LtProb5"] == None:
                activeenemies[1]["loot"]["LtProb5"] = None
        if e2 != None:
            #define what enemy it is
            activeenemies[2]["general"]["enemyname"] = e2
            #write HADLib.enemies entry to activeenemies for e2
            activeenemies[2]["general"]["enemyname"] = HADLib.enemies[e2]["general"]["enemyname"]
            activeenemies[2]["general"]["enemyhp"] = HADLib.enemies[e2]["general"]["enemyhp"]
            activeenemies[2]["general"]["enemyac"] = HADLib.enemies[e2]["general"]["enemyac"]
            activeenemies[2]["general"]["enemydmg1"] = HADLib.enemies[e2]["general"]["enemydmg1"]
            if HADLib.enemies[e2]["general"]["enemydmg2"] == None:
                activeenemies[2]["general"]["enemydmg2"] = None
            activeenemies[2]["general"]["enemyacc"] = HADLib.enemies[e2]["general"]["enemyacc"]
            activeenemies[2]["general"]["enemyweapon1"] = HADLib.enemies[e2]["general"]["enemyweapon1"]
            if HADLib.enemies[e2]["general"]["enemyweapon2"] == None:
                activeenemies[2]["general"]["enemyweapon2"] = None
            if HADLib.enemies[e2]["general"]["special1"] == None:
                activeenemies[2]["general"]["special1"] = None
            if HADLib.enemies[e2]["general"]["special2"] == None:
                activeenemies[2]["general"]["special2"] = None
            if HADLib.enemies[e2]["general"]["special3"] == None:
                activeenemies[2]["general"]["special3"] = None
            activeenemies[2]["general"]["damagetype"] = HADLib.enemies[e2]["general"]["damagetype"]
            activeenemies[2]["general"]["ignoreDR"] = HADLib.enemies[e2]["general"]["ignoreDR"]
            activeenemies[2]["general"]["atkbonus"] = HADLib.enemies[e2]["general"]["atkbonus"]
            #write HADLib.enemies loot entry to activeenemies for e2
            activeenemies[2]["loot"]["LOOTplat"] = HADLib.enemies[e2]["loot"]["LOOTplat"]
            activeenemies[2]["loot"]["LOOTgold"] = HADLib.enemies[e2]["loot"]["LOOTgold"]
            activeenemies[2]["loot"]["LOOTsilv"] = HADLib.enemies[e2]["loot"]["LOOTsilv"]
            activeenemies[2]["loot"]["LOOTcopp"] = HADLib.enemies[e2]["loot"]["LOOTcopp"]
            if HADLib.enemies[e2]["loot"]["LOOTitem1"] == None:
                activeenemies[2]["loot"]["LOOTitem1"] = None
            if HADLib.enemies[e2]["loot"]["LOOTitem2"] == None:
                activeenemies[2]["loot"]["LOOTitem2"] = None
            if HADLib.enemies[e2]["loot"]["LOOTitem3"] == None:
                activeenemies[2]["loot"]["LOOTitem3"] = None
            if HADLib.enemies[e2]["loot"]["LOOTitem4"] == None:
                activeenemies[2]["loot"]["LOOTitem4"] = None
            if HADLib.enemies[e2]["loot"]["LOOTitem5"] == None:
                activeenemies[2]["loot"]["LOOTitem5"] = None
            if HADLib.enemies[e2]["loot"]["LtProb1"] == None:
                activeenemies[2]["loot"]["LtProb1"] = None
            if HADLib.enemies[e2]["loot"]["LtProb2"] == None:
                activeenemies[2]["loot"]["LtProb2"] = None
            if HADLib.enemies[e2]["loot"]["LtProb3"] == None:
                activeenemies[2]["loot"]["LtProb3"] = None
            if HADLib.enemies[e2]["loot"]["LtProb4"] == None:
                activeenemies[2]["loot"]["LtProb4"] = None
            if HADLib.enemies[e2]["loot"]["LtProb5"] == None:
                activeenemies[2]["loot"]["LtProb5"] = None
        if e3 != None:
            #define what enemy it is
            activeenemies[3]["general"]["enemyname"] = e3
            #write HADLib.enemies entry to activeenemies for e3
            activeenemies[3]["general"]["enemyname"] = HADLib.enemies[e3]["general"]["enemyname"]
            activeenemies[3]["general"]["enemyhp"] = HADLib.enemies[e3]["general"]["enemyhp"]
            activeenemies[3]["general"]["enemyac"] = HADLib.enemies[e3]["general"]["enemyac"]
            activeenemies[3]["general"]["enemydmg1"] = HADLib.enemies[e3]["general"]["enemydmg1"]
            if HADLib.enemies[e3]["general"]["enemydmg2"] == None:
                activeenemies[3]["general"]["enemydmg2"] = None
            activeenemies[3]["general"]["enemyacc"] = HADLib.enemies[e3]["general"]["enemyacc"]
            activeenemies[3]["general"]["enemyweapon1"] = HADLib.enemies[e3]["general"]["enemyweapon1"]
            if HADLib.enemies[e3]["general"]["enemyweapon2"] == None:
                activeenemies[3]["general"]["enemyweapon2"] = None
            if HADLib.enemies[e3]["general"]["special1"] == None:
                activeenemies[3]["general"]["special1"] = None
            if HADLib.enemies[e3]["general"]["special2"] == None:
                activeenemies[3]["general"]["special2"] = None
            if HADLib.enemies[e3]["general"]["special3"] == None:
                activeenemies[3]["general"]["special3"] = None
            activeenemies[3]["general"]["damagetype"] = HADLib.enemies[e3]["general"]["damagetype"]
            activeenemies[3]["general"]["ignoreDR"] = HADLib.enemies[e3]["general"]["ignoreDR"]
            activeenemies[3]["general"]["atkbonus"] = HADLib.enemies[e3]["general"]["atkbonus"]
            #write HADLib.enemies loot entry to activeenemies for e3
            activeenemies[3]["loot"]["LOOTplat"] = HADLib.enemies[e3]["loot"]["LOOTplat"]
            activeenemies[3]["loot"]["LOOTgold"] = HADLib.enemies[e3]["loot"]["LOOTgold"]
            activeenemies[3]["loot"]["LOOTsilv"] = HADLib.enemies[e3]["loot"]["LOOTsilv"]
            activeenemies[3]["loot"]["LOOTcopp"] = HADLib.enemies[e3]["loot"]["LOOTcopp"]
            if HADLib.enemies[e3]["loot"]["LOOTitem1"] == None:
                activeenemies[3]["loot"]["LOOTitem1"] = None
            if HADLib.enemies[e3]["loot"]["LOOTitem2"] == None:
                activeenemies[3]["loot"]["LOOTitem2"] = None
            if HADLib.enemies[e3]["loot"]["LOOTitem3"] == None:
                activeenemies[3]["loot"]["LOOTitem3"] = None
            if HADLib.enemies[e3]["loot"]["LOOTitem4"] == None:
                activeenemies[3]["loot"]["LOOTitem4"] = None
            if HADLib.enemies[e3]["loot"]["LOOTitem5"] == None:
                activeenemies[3]["loot"]["LOOTitem5"] = None
            if HADLib.enemies[e3]["loot"]["LtProb1"] == None:
                activeenemies[3]["loot"]["LtProb1"] = None
            if HADLib.enemies[e3]["loot"]["LtProb2"] == None:
                activeenemies[3]["loot"]["LtProb2"] = None
            if HADLib.enemies[e3]["loot"]["LtProb3"] == None:
                activeenemies[3]["loot"]["LtProb3"] = None
            if HADLib.enemies[e3]["loot"]["LtProb4"] == None:
                activeenemies[3]["loot"]["LtProb4"] = None
            if HADLib.enemies[e3]["loot"]["LtProb5"] == None:
                activeenemies[3]["loot"]["LtProb5"] = None
        if e1 == None:
            print("Error: enemy 1 was not defined!")
            return False
        else:
            return True
    def clear_enemy(pos):
        activeenemies[pos] = activeenemies["reset"]
    def combat_start():
        hzline("a", 1)
        if activeenemies[1] != activeenemies["reset"] and activeenemies[2] != activeenemies["reset"] and activeenemies[3] != activeenemies["reset"]:
            print("You see a " + activeenemies[1]["general"]["enemyname"] + ", a " + activeenemies[2]["general"]["enemyname"] + ", and a " + activeenemies[3]["general"]["enemyname"] + "!")
        if activeenemies[1] != activeenemies["reset"] and activeenemies[2] != activeenemies["reset"] and activeenemies[3] == activeenemies["reset"]:
            print("You see a " + activeenemies[1]["general"]["enemyname"] + " and a " + activeenemies[2]["general"]["enemyname"] + "!")
        if activeenemies[1] != activeenemies["reset"] and activeenemies[2] == activeenemies["reset"] and activeenemies[3] == activeenemies["reset"]:
            print("You see a " + activeenemies[1]["general"]["enemyname"] + "!")
        print("")
    def enemyturn()
        if activeenemies[1] != activeenemies["reset"]:
            movecount = 0
            if #STOPPED HERE!!!!!!!!!!!!!!!!!!!!!!!!
            if activeenemies[1]["general"]["special1"] == "scover":
                print("The " + activeenemies[1]["general"]["enemyname"] + " takes cover!")
                effect1dur = 1
            if activeenemies[1]["general"]["special1"] == "orcboost":
                print("The " + activeenemies[1]["general"]["enemyname"] + " raises a staff and pounds it on the floor, strengthening its allies!")
                effect1dur = 3
                
