import math
import time
import random
import tkinter

#################################
# Control variables
#################################
gameOver = False
score = 0
humans = []
zombies = []

root = tkinter.Tk()
root.title("Code versus Zombies")

#################################
# Parameters
#################################
humans_count = 2   # number of humans on the board, Ash excluded
zombies_count = 2

size_rendering = 10 # size of each characters for the graphics simulation

scale = 10 # we scaled down every distance by a scale factor for the graphics simulation
width = 16000
height = 9000
canvas = tkinter.Canvas(root, width = 16000 / scale, height = 9000 / scale, bg = "black")
canvas.pack()

max_displ_Zombie = 400
max_displ_Ash = 1000

#################################
# Initial setup
#################################
ash_position = [2000, 0]

# human_count = 2 # MODIFY THIS LINE IN THE CODINGAME
_input = ["0 950 6000", "1 8000 6100"] # MODIFY THIS LINE IN THE CODINGAME
# humans = []
for i in range(humans_count):
    human_id, human_x, human_y = [int(j) for j in _input[i].split()] # MODIFY THIS LINE IN THE CODINGAME
    humans.append([human_x, human_y])
    
# zombie_count = 2 # MODIFY THIS LINE IN THE CODINGAME
_input = ["0 3100 7000 2737 6831", "1 11500 7100 11115 6990"] # MODIFY THIS LINE IN THE CODINGAME
# zombies = []
for i in range(zombies_count):
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in _input[i].split()] # MODIFY THIS LINE IN THE CODINGAME
    zombies.append([zombie_x, zombie_y])


#################################
# Methods
#################################
# Graphical rendering of a character
def draw_perso(x, y, size_rendering, bg):
    canvas.create_oval((x/scale - size_rendering, y/scale - size_rendering), 
                       (x/scale + size_rendering, y/scale + size_rendering), fill=bg)

# Graphical rendering of all the characters
def draw_board(ash_position, humans, zombies):
    draw_perso(ash_position[0], ash_position[1], size_rendering, "blue")
    
    for h in humans:
        draw_perso(h[0], h[1], size_rendering, "green")
        
    for z in zombies:
        draw_perso(z[0], z[1], size_rendering, "red")


# Simulating behavior of zombies
def zombies_moving(ash_position, humans, zombies, max_displ_Zombie):
    humans_in_danger = []
    
    for i in range(len(zombies)):
        zombie_pos = zombies[i]
        
        current_closest = math.inf
        closest_human_pos = None
        
        for human_pos in humans:
            curr_distance = math.dist(human_pos, zombie_pos)
            
            if curr_distance < current_closest:
                current_closest = curr_distance
                closest_human_pos = human_pos
        
        if math.dist(ash_position, zombie_pos) < current_closest:
            closest_human_pos = ash_position
            current_closest = math.dist(ash_position, zombie_pos)
        
        if current_closest < max_displ_Zombie:
            zombies[i][0] = closest_human_pos[0]
            zombies[i][1] = closest_human_pos[1]
            
            humans_in_danger.append(closest_human_pos)
        else:
            prop = max_displ_Zombie / current_closest
            
            delta_x = closest_human_pos[0] - zombie_pos[0]
            delta_y = closest_human_pos[1] - zombie_pos[1]
            
            zombies[i][0] += math.floor(delta_x * prop)
            zombies[i][1] += math.floor(delta_y * prop)
            
    return zombies, humans_in_danger

# Simulating Ash's movement
def ash_moving(ash_position, target_pos, max_displ_Ash):
    
    if math.dist(ash_position, target_pos) < max_displ_Ash:
        ash_position = target_pos
    else:
        prop = max_displ_Ash / math.dist(ash_position, target_pos)
        
        delta_x = target_pos[0] - ash_position[0]
        delta_y = target_pos[1] - ash_position[1]
        
        ash_position[0] += math.floor(delta_x * prop)
        ash_position[1] += math.floor(delta_y * prop)
        
    return ash_position

# Ash's killing
def ash_killing(ash_position, humans, zombies, score):
    new_zombies = []
    for i in range(len(zombies)):
        if math.dist(zombies[i], ash_position) >= 2000:
            new_zombies.append(zombies[i])
            
    nb_zombies_killed = len(zombies)-len(new_zombies)
    # first two fibonacci terms
    a = 1
    b = 2
    
    # Le système de points fonctionne ainsi :
    #     La valeur d'un zombie tué est égal au nombre d'humains encore en vie au carré 
    #     et multiplié par 10, sans inclure Ash.
    #     Si plusieurs zombies sont détruits pendant un même tour, 
    #     la valeur du nème zombie tué est multiplié par le (n+2)ème terme de la 
    #     suite de Fibonacci (1, 2, 3, 5, 8, etc). Vous avez donc tout intérêt à 
    #     tuer un maximum de zombies dans un même tour !
    
    if nb_zombies_killed == 1:
        print(len(humans))
        score += len(humans)**2 * 10
    elif nb_zombies_killed > 1:
        for i in range(1, nb_zombies_killed+1):
            a, b = b, a + b
            score += b * i * len(humans)**2 * 10
               
    return new_zombies, score

# zombies eating
def zombies_eating(humans_in_danger):
    humans_rem = []
    
    for i in range(len(humans)):
        if humans[i] not in humans_in_danger:
            humans_rem.append(humans[i])
                
    return humans_rem

 
#################################
# Tests
#################################
#draw_board(ash_position, humans, zombies)

#################################
# Main loop
#################################
# while not gameOver:
#     draw_board(ash_position, humans, zombies)
#     root.update()
#     time.sleep(1)
#     canvas.delete("all")
    
#     # Zombies are moving to their respective target
#     zombies, humans_in_danger = zombies_moving(ash_position, humans, zombies, max_displ_Zombie)
    
#     # Ash is moving towards its target
#     target_pos = zombies[0] # testing
#     ash_position = ash_moving(ash_position, target_pos, max_displ_Ash)
    
#     # Destroy zombies in an area of 2000 of Ash
#     print(len(humans))
#     zombies, score = ash_killing(ash_position, humans, zombies, score)
    
#     # Every human in an area of 400 of a zombie gets eaten
#     humans = zombies_eating(humans_in_danger)
    
#     print(score)
    
#     # game is over when there are no zombies left or when there are no humans left
#     if len(humans) == 0 or len(zombies) == 0:
#         gameOver = True
        
    
# draw_board(ash_position, humans, zombies)
# root.mainloop()
    

# genetic algorithm
# 1. Create population
# Each chromosome is a sequence of positions
# 2. Selection
# Score every chromosome and compute mean score
# keep the best 50% of the population
# Crossover
# Mutation
# Retain the best scoring chromosome
# Repeat until no significative change of mean score


#################################
# Genetic algorithm
#################################
# Parameters
size_population = 50
size_chromosome = 10

def create_chromosome(ash_position, size_chromosome, max_displ_Ash):
    new_chromosome = []
    
    for i in range(size_chromosome):
        target_x = random.randint(-width//max_displ_Ash, width//max_displ_Ash)
        target_y = random.randint(-height//max_displ_Ash, height//max_displ_Ash)
        
        new_x = max(0, ash_position[0] + target_x*max_displ_Ash)
        new_x = min(ash_position[0] + target_x*max_displ_Ash, width-1)
        
        new_y = max(0, ash_position[1] + target_y*max_displ_Ash)
        new_y = min(ash_position[1] + target_y*max_displ_Ash, height-1)
        
        new_chromosome.append([new_x, new_y])
    
    return new_chromosome
    

ash_moving

print(create_chromosome(ash_position, size_chromosome, max_displ_Ash))


# def create_population():
    
#     ash_moving(ash_position, target_pos, max_displ_Ash)







