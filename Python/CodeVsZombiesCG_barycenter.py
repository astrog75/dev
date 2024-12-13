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