
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #
    # Strategy 1 : go towards the closest zombie
    # zombies_pos = []

    # for i in range(zombie_count):
    #   zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
    #   zombies_pos.append((zombie_xnext, zombie_ynext))
    # nxt_x, nxt_y = 0, 0
    #     min_distance = math.inf
    #     for zomb_pos in zombies_pos:
    #         current_distance = math.sqrt((human_x - zomb_pos[0])**2 +(human_y - zomb_pos[1])**2)
    #         if current_distance < min_distance:
    #             min_distance = current_distance
    #             nxt_x, nxt_y = zomb_pos[0], zomb_pos[1]
    #
    # print(nxt_x, nxt_y)

    # Strategy 2 : define weights for every human. each human has a weight proportional to its distance to its closest zombie
    # i.e. : the closest a zombie is to a human, the heavier its weight is
    #
    # Compute weights of humans
    # Weights depends on 2 factors : 1. the distance between every zombie and that human, 
    # and 2. the distance betweeen Ash and that human
    #
    # Step 1 : standardisation des distances humain-zombie
    # Important, car les distances calculées directement à partir des données sont très grandes, et donc les poids très petits, 
    # ce qui peut poser des problèmes d'approx numérique ou de division par Zéro
    # distances = {}
#     total_distance = 0
#     n_total = 0

#     for human in humans:
#         distances[human] = []
#         for zombie in zombies:
#             diff_x = humans[human][0]-zombies[zombie][0]
#             diff_y = humans[human][1]-zombies[zombie][1]
#             distance = math.sqrt(diff_x**2 + diff_y**2)
#             distances[human].append(distance)
#             total_distance += distance
#             n_total += 1

#     #print(distances)
#     mean = total_distance/n_total

#     ssquare = 0
#     for human in distances:
#         for d in distances[human]:
#             ssquare += (d-mean)**2

#     var = ssquare/n_total
#     std = var**0.5

#     if std == 0: # Case when we have 1 human and 1 zombie (then the standard deviation is 0)
#         std = 1
    
#     #print(mean, std)

#     # Step 2 : actually compute weight for every human
#     # Factor 1 (see comment above)
#     # Factor 2 (see comment above)

#     weights = {}
#     for human in humans:
#         weights[human] = 0
#         # Factor 1
#         for x in distances[human]:
#             std_distance = (x-mean)/std
            
#             try:
#                 weights[human] += 1/std_distance
#             except: # Case when we have 1 human and 1 zombie (then the standard deviation is 0)
#                 weights[human] += 1
            
        
#         # Factor 2
#         diff_x = humans[human][0]-x
#         diff_y = humans[human][1]-y
#         dist_Ash_curr_human = math.sqrt(diff_x**2 + diff_y**2)

#         dist_Ash_curr_human = (dist_Ash_curr_human-mean)/std
        
#         try:
#             weights[human] += (1/dist_Ash_curr_human)
#         except: # Case when we have 1 human and 1 zombie (then the standard deviation is 0)
#             weights[human] += 1
    
#     for w in weights:
#         print(w, weights[w], file = sys.stderr)

#     heaviest_human = None
#     for human in weights:
#         if weights[human] == max(weights.values()):
#             heaviest_human = human

#    print(humans[heaviest_human][0], humans[heaviest_human][1])

    # Strategy 3 : genetic algorithm
    #
    # Step 1 : define a chromosome. A chromosome here is a sequence of Ash's movements
    #
    