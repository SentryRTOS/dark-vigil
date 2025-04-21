import random
import os
import time

os.system("cls")
player = ""
notice = 0
"""
To-do

[ ] Dashboard needs to be built
    - Placeholders
        [x] Team Rosters
        [ ] Odds for bet
        [x] Gold Indicator
        [x] 1. Place Bet
        [ ] 2. Buy Drink
            - Drink system
                - Buying drink reveals random facts about combatants sometimes.
                - Each drink can make you drunk, causing you to miss this
                  round.
                - Flavor text needs to be built for Combatant Attributes
                    - Needs to be sorted so most stand out stats are commented
                      on first, the way normal humans would.
        [ ] 3. Gossip
            - Bullshitting system
                - Gives players the chance to learn about combatants, but costs
                  nothing and is very unreliable.
        [x] 4. Start Round
                - Each round you're given a certain number of actions before
                  the next round starts, this just starts the next round. 
[x] Combatant Teams need to be built
    - 6 Combatants Total
    - Assigned to Team A and Team B
    - Functions designed to make one team fight the other
[x] Combat system needs rework.
    - Max number of turns to prevent infinite rounds.
    - Attack v Defense rolls are trash
        - Could be an item thing
        - Could be an internal math thing.
[ ] Item system consideration
[ ] Flavor text


"""


class Lobby:
    lobby_name = "The Copper Coins"

    def __init__(self, team_a, team_b):
        """This is the lobby draw, it should include:
        Roster
        ----------------------------------------
        Team A       | Team B       |../Odds\..|
        Combatant 1A | Combatant 1B |          |
        Combatant 1A | Combatant 1B |          |
        Combatant 1A | Combatant 1B |          |
        ---------------------------------------|
        Gold |                                 |
        ---------------------------------------|
        1. Place Bet
        2. Buy Drink
        3. Gossip
        4. Start Round
        SCROLLING FLAVOR TEXT
        input()

        NOTE!
        This grid has to align to a 79 character terminal limit.
        """
        self.team_a = team_a
        self.team_b = team_b

    def update(self):
        Lobby(TeamA, TeamB)


class TeamA:
    def __init__(self, team_name, combatant_1, combatant_2, combatant_3):
        self.team_name = team_name
        self.combatant_1 = combatant_1
        self.combatant_2 = combatant_2
        self.combatant_3 = combatant_3


class TeamB:
    def __init__(self, team_name, combatant_1, combatant_2, combatant_3):
        self.team_name = team_name
        self.combatant_1 = combatant_1
        self.combatant_2 = combatant_2
        self.combatant_3 = combatant_3


class Combatant:
    def __init__(
        self, name, strength, defence, speed, dodge, health, weapon, armor, flavor
    ):
        """_summary_

        Args:
            name (_type_): Comes from the name_generator
            strength (_type_): Comes from combatant_generator
            defence (_type_): _description_
            speed (_type_): _description_
            dodge (_type_): _description_
            health (_type_): _description_
            weapon (_type_): _description_
            armor (_type_): _description_
            flavor (_type_): _description_
        """

        self.name = name
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.time_counter = speed
        self.dodge = dodge
        self.health = int(health)
        self.weapon = weapon
        self.armor = armor
        self.flavor = flavor
        # self.vitality = self.vigor()
        self.score = strength + defence + health
        self.score_revealed = False

    def attack(self, target):
        self.time_counter = self.speed
        fail = 20 == random.randint(0, 20)
        if fail:
            print(Flavor.fail(self.name))
            print("\n")
        else:
            hit_roll = 10 > random.randint(0, target.dodge)
            if hit_roll:
                damage_roll = (
                    (self.strength / 2) + random.randint(0, self.strength)
                ) * self.weapon.attack
                defense_roll = (
                    (self.defence / 2) + random.randint(0, self.defence)
                ) * self.armor.protection
                total_damage = damage_roll - defense_roll
                if total_damage <= 0:
                    message = f"{self.name} strikes {target.name} feebly!"
                    typed = ""
                    for m in message:
                        typed += m
                        print(typed, end="\r", flush=True)
                        time.sleep(0.01)
                    print("\n")
                else:
                    target.health -= total_damage
                    message = f"{self.name} strikes {target.name}. {target.name} looks {target.vigor()}."
                    typed = ""
                    for m in message:
                        typed += m
                        print(typed, end="\r", flush=True)
                        time.sleep(0.01)
                    print("\n")

            else:
                message = f"{target.name} deftly dodged {self.name}'s attack!"
                typed = ""
                for m in message:
                    typed += m
                    print(typed, end="\r", flush=True)
                    time.sleep(0.01)
                print("\n")

    def vigor(self):
        """This is meant to be the health concealer flavor text."""
        if self.health >= 100:
            return "fresh."
        elif self.health > 60:
            return "okay."
        elif self.health > 30:
            return "bloodied."
        elif self.health > 0:
            return "close to death."
        else:
            return "dead."


class Weapon:
    def __init__(self, name, attack=1, weight=1):
        """
        Names are to be mundane, 'iron sword', 'steel dagger'
        Attack is a multiplier of Strength, 1 = 100%, .5 = 50%
        The higher the strength, the stronger the attack.
        Weight is a multiplier of Speed. 1 = 100% action time, .5 = 50% action
        time.
        """
        self.name = name
        self.attack = attack
        self.weight = weight


class Armor:
    def __init__(self, name, protection=0, weight=1):
        """
        Names are to be mundane, 'leather coat', 'iron shirt'
        Protection is a multiplier of defence, 1 = 100% (complete protection), .5 = 50%
        The higher the defence, the greater the protection.
        Weight is a multiplier of Speed. 1 = 100% action time, .5 = 50% action
        time.
        """
        self.name = name
        self.protection = protection
        self.weight = weight


class Flavor:
    def __init__(self):
        pass

    def fail(name):
        return f"As {name} fumbles, the crowd boos!"


def name_generator():
    first_name = [
        "Radiant",
        "Sneering",
        "Wicked",
        "Noble",
        "Cruel",
        "Pious",
        "Cunning",
        "Vile",
        "Gallant",
        "Sinister",
        "Righteous",
        "Merciful",
        "Brutal",
        "Just",
        "Corrupt",
        "Zealous",
        "Malicious",
        "Kindly",
        "Wrathful",
        "Virtuous",
    ]

    last_name = [
        "Adler",
        "Bailey",
        "Barton",
        "Becker",
        "Bennett",
        "Blake",
        "Brandt",
        "Carver",
        "Chapman",
        "Clark",
        "Coleman",
        "Crawford",
        "Dawson",
        "Donovan",
        "Doyle",
        "Draper",
        "Ellis",
        "Fletcher",
        "Gibson",
        "Granger",
        "Grant",
        "Greene",
        "Harlan",
        "Harris",
        "Hawkins",
        "Hayward",
        "Holt",
        "Keller",
        "Klein",
        "Langley",
        "Lawson",
        "Marshall",
        "Mason",
        "Merrick",
        "Nolan",
        "Parker",
        "Payne",
        "Porter",
        "Quincy",
        "Reeves",
        "Rogers",
        "Sawyer",
        "Shepard",
        "Spencer",
        "Stanton",
        "Thorne",
        "Turner",
        "Walker",
        "Wells",
        "Whitman",
    ]
    flip = random.randint(0, 2)
    if flip == 1:
        return f"{last_name[random.randint(0, len(last_name) - 1)]} the {first_name[random.randint(0, len(first_name) - 1)]}"
    else:
        return f"{first_name[random.randint(0, len(first_name) - 1)]} {last_name[random.randint(0, len(last_name) - 1)]}"


def strength_generator():
    return random.randint(8, 12)


def defense_generator():
    return random.randint(8, 12)


def speed_generator():
    return random.randint(8, 12)


def dodge_generator():
    return random.randint(8, 12)


def health_generator():
    return random.randint(80, 120)


def weapon_generator():
    name = "iron blade"  # placeholder
    attack = random.randint(8, 12)
    weight = (random.randint(30, 100)) / 100
    return Weapon(name, attack, weight)


def armor_generator():
    name = "iron chest"  # placeholder
    protection = random.randint(8, 12) / 10
    weight = (random.randint(30, 100)) / 100
    return Armor(name, protection, weight)


def flavor_generator(name):
    return f"{name} is a combatant at {Lobby.lobby_name}!"


def combatant_generator():
    name = name_generator()
    strength = strength_generator()
    defense = defense_generator()
    speed = speed_generator()
    dodge = dodge_generator()
    health = health_generator()
    weapon = weapon_generator()
    armor = armor_generator()
    flavor = flavor_generator(name)
    return Combatant(
        name, strength, defense, speed, dodge, health, weapon, armor, flavor
    )


def tick(combatant):
    combatant.time_counter -= 1


def action(combatant):
    pass


## Combatant testing
combatant_1 = combatant_generator()
combatant_2 = combatant_generator()
combatant_3 = combatant_generator()
combatant_4 = combatant_generator()
combatant_5 = combatant_generator()
combatant_6 = combatant_generator()


def fresh_combatants(
    combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6
):
    if combatant_1.health > 0:
        pass
    else:
        combatant_1 = combatant_generator()
    if combatant_2.health > 0:
        pass
    else:
        combatant_2 = combatant_generator()
    if combatant_3.health > 0:
        pass
    else:
        combatant_3 = combatant_generator()
    if combatant_4.health > 0:
        pass
    else:
        combatant_4 = combatant_generator()
    if combatant_5.health > 0:
        pass
    else:
        combatant_5 = combatant_generator()
    if combatant_6.health > 0:
        pass
    else:
        combatant_6 = combatant_generator()
    return combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6


team_a = [combatant_1, combatant_2, combatant_3]
team_b = [combatant_4, combatant_5, combatant_6]


def reset_game():
    global gold, wager, round_number, bet_number, side, drink_count, player, notice
    gold = 100
    wager = 0
    round_number = 0
    bet_number = 0
    drink_count = 0
    notice = 0
    side = ""
    player = start_window()
    dashboard()


def start_window():
    global player
    os.system("cls")
    message = "And your back? Alright. What should I call you this time?"
    typed = ""
    for m in message:
        typed += m
        print(typed, end="\r", flush=True)
        time.sleep(0.05)
    name = input("\n ")
    os.system("cls")
    message = f"{name.title()}? Alright. Just keep your head down."
    typed = ""
    for m in message:
        typed += m
        print(typed, end="\r", flush=True)
        time.sleep(0.03)
    time.sleep(3)
    os.system("cls")
    print(f"Press any key to enter, {name.title()}.")
    stop = input()
    return name.title()


def attack_team_a():
    select = random.randint(1, 3)
    if select == 1:
        return combatant_1
    if select == 2:
        return combatant_2
    if select == 3:
        return combatant_3


def attack_team_b():
    select = random.randint(1, 3)
    if select == 1:
        return combatant_4
    if select == 2:
        return combatant_5
    if select == 3:
        return combatant_6


def vigor_printout():
    print("Team A")
    print(f"{combatant_1.name} looks {combatant_1.vigor()}")
    print(f"{combatant_2.name} looks {combatant_2.vigor()}")
    print(f"{combatant_3.name} looks {combatant_3.vigor()}\n")
    print("Team B")
    print(f"{combatant_4.name} looks {combatant_4.vigor()}")
    print(f"{combatant_5.name} looks {combatant_5.vigor()}")
    print(f"{combatant_6.name} looks {combatant_6.vigor()}\n")


def battle_tick():
    tick(combatant_1)
    tick(combatant_2)
    tick(combatant_3)
    tick(combatant_4)
    tick(combatant_5)
    tick(combatant_6)


def drink():
    global drink_count
    drink_count += 1
    reveal_roll = random.randint(1, 10)
    if reveal_roll == 1:
        print(f"I've heard something about {combatant_1.name}, sure.")
        combatant_1.score_revealed = True
    if reveal_roll == 2:
        print(f"I've heard something about {combatant_2.name}, sure.")
        combatant_2.score_revealed = True
    if reveal_roll == 3:
        print(f"I've heard something about {combatant_3.name}, sure.")
        combatant_3.score_revealed = True
    if reveal_roll == 4:
        print(f"I've heard something about {combatant_4.name}, sure.")
        combatant_4.score_revealed = True
    if reveal_roll == 5:
        print(f"I've heard something about {combatant_5.name}, sure.")
        combatant_5.score_revealed = True
    if reveal_roll == 6:
        print(f"I've heard something about {combatant_6.name}, sure.")
        combatant_6.score_revealed = True
    else:
        print("I haven't been paying much attention. They're deaders anyway.")
    time.sleep(3)


def gossip():
    reveal_roll = random.randint(1, 30)
    if reveal_roll == 1:
        print(f"I've heard something about {combatant_1.name}, sure.")
        combatant_1.score_revealed = True
    if reveal_roll == 2:
        print(f"I've heard something about {combatant_2.name}, sure.")
        combatant_2.score_revealed = True
    if reveal_roll == 3:
        print(f"I've heard something about {combatant_3.name}, sure.")
        combatant_3.score_revealed = True
    if reveal_roll == 4:
        print(f"I've heard something about {combatant_4.name}, sure.")
        combatant_4.score_revealed = True
    if reveal_roll == 5:
        print(f"I've heard something about {combatant_5.name}, sure.")
        combatant_5.score_revealed = True
    if reveal_roll == 6:
        print(f"I've heard something about {combatant_6.name}, sure.")
        combatant_6.score_revealed = True
    if reveal_roll >= 20:
        global notice
        notice += 5
        print(f"Hey, aren't you that guy?")
    elif reveal_roll > 7:
        index = random.randint(0, 19)
        flavor = {
            0: "He used to be a dentist, y'know. Till *that* happened.",
            1: "I'm tellin' ya, that one's got a knife hidden somewhere.",
            2: "Two silvers says he bites before he swings.",
            3: "That ain't bloodlust... that's heartbreak.",
            4: "See the way he stands? Military. Or maybe prison.",
            5: "Last time he fought, they had to mop the walls.",
            6: "They say she doesn't blink. Ever.",
            7: "That one's cursed. Look at his shadow—go on!",
            8: "Lost everything. Wife, farm, dog. Just rage left now.",
            9: "They don’t pay me to *not* scream when he fights.",
            10: "One time I saw him knock out a *horse*.",
            11: "She only fights on the full moon. This ain’t it.",
            12: "He drinks blood before every match. His own.",
            13: "Watch his left hand. No, not that one.",
            14: "They're all bark. Wait 'til someone *actually* hits 'em.",
            15: "You think this is fighting? I’ve seen riots softer.",
            16: "He don't feel pain. Not even from his kids.",
            17: "Once saw her rip a man's beard *off*.",
            18: "Yeah, he wins. But he cries after. Loud.",
            19: "That one’s got a debt to settle tonight.",
        }
        print("I haven't been paying much attention. " + flavor[index])
    time.sleep(5)


def end_round():
    global combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6, round_number, wager, gold, side
    round_number += 1
    team_a_health = combatant_1.health + combatant_2.health + combatant_3.health
    team_b_health = combatant_4.health + combatant_5.health + combatant_6.health
    if team_a_health > team_b_health:
        if side == "A":
            gold += wager * 2
            print(f"You've won {wager * 2}!")
        wager = 0
        side = ""
        return "\nTeam A is victorious!"
    else:
        if side == "B":
            gold += wager * 2
            print(f"You've won {wager * 2}!")
        wager = 0
        side = ""
        return "\nTeam B is victorious!"


def round_start():
    global combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6
    os.system("cls")
    message = "Welcome to The Copper Coins!"
    typed = ""
    for m in message:
        typed += m
        print(typed, end="\r", flush=True)
        time.sleep(0.05)
    print("\n")
    message = "Are we ready for some blood?"
    typed = ""
    for m in message:
        typed += m
        print(typed, end="\r", flush=True)
        time.sleep(0.01)
    print("\n")
    message = "Combatants!"
    typed = ""
    for m in message:
        typed += m
        print(typed, end="\r", flush=True)
        time.sleep(0.2)
    print("|----------3-----------|")
    time.sleep(0.3)
    print("|----------2-----------|")
    time.sleep(0.3)
    print("|----------1-----------|")
    time.sleep(0.3)
    print("|--------FIGHT---------|")
    time.sleep(0.5)
    battle_timer = 0
    move = 0
    os.system("cls")
    vigor_printout()
    while battle_timer <= 10000:
        team_a_health = combatant_1.health + combatant_2.health + combatant_3.health
        team_b_health = combatant_4.health + combatant_5.health + combatant_6.health
        if team_a_health > 0 and team_b_health > 0:
            battle_timer += 1
            battle_tick()
            if combatant_1.health > 0 and combatant_1.time_counter == 0:
                move = 1
                combatant_1.attack(attack_team_b())
            if combatant_2.health > 0 and combatant_2.time_counter == 0:
                move = 1
                combatant_2.attack(attack_team_b())
            if combatant_3.health > 0 and combatant_3.time_counter == 0:
                move = 1
                combatant_3.attack(attack_team_b())
            if combatant_4.health > 0 and combatant_4.time_counter == 0:
                move = 1
                combatant_4.attack(attack_team_a())
            if combatant_5.health > 0 and combatant_5.time_counter == 0:
                move = 1
                combatant_5.attack(attack_team_a())
            if combatant_6.health > 0 and combatant_6.time_counter == 0:
                move = 1
                combatant_6.attack(attack_team_a())
            if move == 1:
                move = 0
                print("\nIt's not over yet!")
                time.sleep(2)
                os.system("cls")
                vigor_printout()
            time.sleep(0.1)
        else:
            win_text = end_round()
            print(win_text)
            time.sleep(5)
            (
                combatant_1,
                combatant_2,
                combatant_3,
                combatant_4,
                combatant_5,
                combatant_6,
            ) = fresh_combatants(
                combatant_1,
                combatant_2,
                combatant_3,
                combatant_4,
                combatant_5,
                combatant_6,
            )
            dashboard()
    win_text = end_round()
    print(win_text)
    time.sleep(5)
    combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6 = (
        fresh_combatants(
            combatant_1, combatant_2, combatant_3, combatant_4, combatant_5, combatant_6
        )
    )
    dashboard()


def dashboard():
    global gold, wager, side, round_number, bet_number, notice, player
    os.system("cls")
    print("|----------------------|")
    print("|---The Copper Coins---|")
    print("|----------------------|")
    print("|--------Team A--------|")
    if not combatant_1.score_revealed:
        print(f"| {combatant_1.name}")
    else:
        print(f"| {combatant_1.name} + {combatant_1.score}")
    if not combatant_2.score_revealed:
        print(f"| {combatant_2.name}")
    else:
        print(f"| {combatant_2.name} + {combatant_2.score}")
    if not combatant_3.score_revealed:
        print(f"| {combatant_3.name}")
    else:
        print(f"| {combatant_3.name} + {combatant_3.score}")
    print("|--------Team B--------|")
    if not combatant_4.score_revealed:
        print(f"| {combatant_4.name}")
    else:
        print(f"| {combatant_4.name} + {combatant_4.score}")
    if not combatant_5.score_revealed:
        print(f"| {combatant_5.name}")
    else:
        print(f"| {combatant_5.name} + {combatant_5.score}")
    if not combatant_6.score_revealed:
        print(f"| {combatant_6.name}")
    else:
        print(f"| {combatant_6.name} + {combatant_6.score}")
    print("|----------------------|")
    print(f"| Gold : {gold}")
    print(f"| Wager: {wager}")
    print(f"| Side : {side}")
    print("|----------------------|")
    print("1. Place Bet")
    print("2. Drink Wine (-1g)")
    print("3. Gossip")
    print("4. Start Round")
    print("|----------------------|")
    if gold == 0 and wager == 0:
        print("A guard has noticed you, it's time to leave..")
        time.sleep(5)
        print("For now...")
        time.sleep(5)
        print("Ending 1. A debter, still.")
        time.sleep(5)
        os.system("cls")
        reset_game()
    if round_number == 1 or notice >= 10:
        print("Someone is looking at you from the other side of the room.")
    if round_number == 2 or notice >= 25:
        print("You can see the guards talking to one another and looking around.")
    if round_number == 3 or notice >= 40:
        print("You see your informant looking at you intently.")
    if notice > 50:
        print(
            "A guard grabs you by the wrist,\"Well, well, well. You'll pay for what you've done, this time.\""
        )
        time.sleep(5)
        print("The guard wrenchs your wrist, nearly breaking it, but you get away. . .")
        time.sleep(5)
        print("Ending 5. The social shadow.")
        time.sleep(5)
        os.system("cls")
        reset_game()
    if round_number == 4 and gold >= 500:
        print('Your informant grabs you by the wrist,"Sir, they know you\'re here."')
        time.sleep(5)
        print("You make your get away.")
        time.sleep(5)
        print("Ending 2. Never enough time.")
        time.sleep(5)
        os.system("cls")
        reset_game()
    if round_number == 4 and gold >= 1000:
        print("You've made your quota for the night.")
        time.sleep(5)
        print("This will buy you a little more time. . .")
        time.sleep(5)
        print("Ending 3. The things we must do.")
        time.sleep(5)
        os.system("cls")
        reset_game()
    if round_number == 4 and gold >= 1500:
        print("You've made your quota for the night.")
        time.sleep(5)
        print("\"I'm coming, Maria. I'm so sorry it has to be like this.\"")
        time.sleep(5)
        print("Ending 4. Sins of the father.")
        time.sleep(5)
        os.system("cls")
        reset_game()
    else:
        print("The room is very lively, people are drinking and placing bets.")
    selection = input(f"What would you like to do {player}?\n >>> ")
    if selection == "1":
        """
        This is the betting window. It should be able to:
            - Ask you which team to bet on.
            - Update the bet for that team.
        """
        if wager != 0:
            print("You've already placed your bets.")
            dashboard()
        if round_number >= 1 and bet_number >= 1:
            message = "Haven't I seen you before?"
            typed = ""
            for m in message:
                typed += m
                print(typed, end="\r", flush=True)
                time.sleep(0.05)
            print("\n")
            time.sleep(1)
        if bet_number == 0:
            print(
                "A large man in a beer stained sack turns to you when you approach the bar."
            )
        print(f"Place your bets.\n")
        try:
            wager = int(input("How much will you wager?\n"))
        except ValueError:
            print("What was that? Speak up. Numbers only!")
        if wager == 0:
            print('He pushes you back. "I don\'t have time for this."')
            notice += 1
            time.sleep(5)
            dashboard()
        while wager > gold:
            wager = int(input("You don't have that much. How much will you wager?\n"))
        print(f"Aye. {wager} gold pieces.\n")
        while side not in ("A", "B"):
            try:
                side = (str(input("Which Team? A or B.\n"))).strip().upper()
            except ValueError:
                print("A, or B.")
        print(
            f"{side}? Okay. So that's {wager} on {side.title()}."
        )  # Consider setting his confirmation phrases from a dictionary.
        print("He's starting to look a little impatient.")
        confirm = input("Sound good? y / n\n").strip().lower()
        if confirm == "y":
            print("Got it. Rest in peace, oh ye troubled.")
            gold = gold - wager
            time.sleep(5)
            dashboard()

        else:
            print(
                "I have people actually placing bets here. Come back when you're not wasting my time!"
            )
            wager = 0
            side = ""
            time.sleep(5)
            dashboard()
    if selection == "2":
        """
        This should take you to the Bar Screen, where you can bullshit with
        patrons to try and figure out which team has a likelier chance of
        winning.
        """
        if gold == 0:
            print("You can't afford it.")
            time.sleep(3)
            dashboard()
        if drink_count <= 10:
            gold -= 1
            'You order a drink and sit next to the bar. You ask no one in particular,"Who looks good on the roster?"'
            time.sleep(3)
            drink()
            dashboard()
        else:
            "You've had too much tonight."
            time.sleep(3)
            dashboard()
    if selection == "3":
        """
        This is basically a bullshit section, where I'll dump random funnies.
        These funnies should also scroll at random along the bottom of the
        screen.
        """
        notice += 1
        gossip()
        dashboard
    if selection == "4":
        """
        This just starts the round. No fan-fare for now.
        """
        round_start()
    else:
        os.system("cls")
        dashboard()


reset_game()
