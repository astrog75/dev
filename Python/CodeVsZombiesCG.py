import math

# Genetic algorithm to solve "Code vs Zombies" from CodinGame
#
# A chromosome here is a sequence of positions of Ash
# Each gene is then a position
# 
# We must then generate a random population at first
# And scoring each chromosome using the scoring function from the Game.
#
# 
# Goal : given the game starting state below, print the best (highest score)
# sequence of movements "best_movements"
x_start, y_start = [int(i) for i in input().split()]

human_count = int(input())
humans = {}
for i in range(human_count):
    human_id, human_x, human_y = [int(j) for j in input().split()]
    humans[human_id] = (human_x, human_y)

zombie_count = int(input())
zombies = {}
for i in range(zombie_count):
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
    zombies[zombie_id] = (zombie_xnext, zombie_ynext)

# Goal : the final result should look like this :
# for mvt in best_movements:
#     x, y = [int(i) for i in input().split()]
    
#     human_count = int(input())
#     for i in range(human_count):
#         human_id, human_x, human_y = [int(j) for j in input().split()]

#     zombie_count = int(input())
#     for i in range(zombie_count):
#         zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        
#     print(mvt)

# Simulates the movement of a given zombie relative to its closest human
# Ash included
# def zombie_move_to(zombie, human):
#     delta_x = human[0] - zombie[0]
#     delta_y = human[1] - zombie[1]
#     distance = dist(zombie, human)
#     if distance > 400:
#         zombie[0] += math.floor(delta_x)
#         zombie[1] += math.floor(delta_y)
        
# Main simulation
ash_id = 100
x_Ash, y_Ash = x_start, y_start
# L'ordre dans lequel se déroule les actions entre deux tours est celui-ci :

#     Les zombies se déplacent vers leurs cibles.
#     Ash se déplace vers sa cible.
#     Tout zombie se situant dans un rayon de moins de 2000 unités est détruit.
#     Si un zombie se trouve sur un humain alors il le mange.

# Identify the closest human for every zombie
for zombie_id in zombies:
    current_closest = math.inf
    closest_human = -1
    
    for human_id in humans:
        curr_distance = math.dist(humans[human_id], zombies[zombie_id])
        
        if curr_distance < current_closest:
            current_closest = curr_distance
            closest_human = human_id
    
    if math.dist((x_Ash, y_Ash), zombies[zombie_id]) < current_closest:
        closest_human = ash_id
        
    if current_closest < 400:
        zombies[zombie_id] = humans[closest_human]
    else:
        prop = 400 / current_closest
        delta_x = humans[closest_human][0] - zombies[zombie_id][0]
        delta_y = humans[closest_human][1] - zombies[zombie_id][1]
        zombies[zombie_id][0] += math.floor(delta_x * prop)
        zombies[zombie_id][1] += math.floor(delta_y * prop)


    
        

    
