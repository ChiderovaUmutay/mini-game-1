# Salam 👐🏻

### 📖 Repository description: 

This repository presents a mini-game that simulates a battle (shootout) between an intergalactic hero and a terrorist robot. Information about the progress of the battle is displayed in the console.

Below is a description of the task. I wrote each stage in a separate file.

### 🎯 Purpose of the program:  

I wrote this program to refresh my basic knowledge of Python. The functionality is implemented using Python functions.

## Task  📝

### Stage #1

```
At the first stage, write the main game cycle, during which only the hero’s moves are made. Each hero's move is performed according to the following rules:

The hero tries to hit the robot, 75% probability:
    ▫ If you hit:   
        Damage = hero gun - robot defense;
        The robot loses health equal to damage;
        A message about the damage done is displayed.
    
    ▫ If you don't get it:
        A message is displayed indicating that the hero did not hit.

At the end of the turn, display a message about the robot's remaining health.

The main loop should repeat the hero's moves until the robot has 0 HP left.

▫ If the robot no longer has vital energy:
    Show a message that the hero has won;
    Exit the loop.
```

 ### Stage #2

```
At this stage you need to add the robot's move. The robot's move is performed after the hero's turn and checking that the robot is still alive. 

With a 1/3 chance, the robot can choose one of the following actions:
    ▫ Use homing missiles and accurately hit the hero:
        Damage = robot gun + 30% of robot gun - hero defense;
        Damage dealt is subtracted from the hero's health;
        Display a message about the damage caused.
        
    ▫ Use regular ammo:
        There is a 50/50 chance that the robot will hit the hero:
            ▫ If you hit:
                Damage = robot gun - hero defense;
                Damage dealt is subtracted from the hero's health;
                Display a message about the damage caused.
            ▫ If you don't get it:
                A message is displayed indicating that the robot did not hit.
                
    ▫ Jam:
        Display a message indicating that the robot is jammed.
        
    At the end of the turn, display a message about the hero's remaining health.

After the robot's turn, in the main loop you need to check the amount of remaining health the hero has.

▫ If the hero runs out of life energy:
    Show a message that the hero has lost;
    Exit the loop.

You can display messages about the state of both characters: the robot and the hero, after each move.
```

### Stage #3

```
During the hero's turn, add the ability for the player to choose what the hero will do:
    ▫ Attack - in this case, the hero attacks, as in stage 1.
    ▫ Defend yourself:
        If a hero defends, the value of the hero's protective field is added to his defense until the end of the turn.
        The hero does not attack this turn.
        After the robot's next move, the hero must remove the protective field.
    ▫ Do nothing, skip a move - the hero does not attack or defend.

The choice is made by entering one of the commands: attack, pass, defense.
```

### Stage #4

###### This stage consists of two additional tasks.

#### Task №1
```
Add the ability to “Throw a poison grenade” to the robot.

The robot has a 25% chance of throwing a grenade. The grenade deals double damage from the robot's weapon, and poisons the hero directly through the armor, but the hero can protect himself from it using a protective field. If the robot throws a grenade, it does nothing else on its turn.
    ▫ Damage = robot weapon * 2
    ▫ If the hero defends himself this turn, he reflects the grenade with a protective field and takes no damage.
```

#### Task №2
```
Add the action of “Injecting adrenaline” to the hero.

The hero has several syringes with adrenaline lying around in his backpack, which he can inject in battle to heal.
    ▫ Each adrenaline syringe heals 500 health (change this number as desired).
    ▫ Using an adrenaline syringe counts as a turn. The hero cannot attack or defend this turn.
    ▫ If the adrenaline syringes run out, the player must choose another action.
```