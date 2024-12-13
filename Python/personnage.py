class Perso:
    def __init__(self, id_, position, type_):
        self.id_ = id_
        self.position = position
        self.type_ = type_
        
    def get_x(self):
        return self.position[0]
    
    def get_y(self):
        return self.position[1]
    

# Humans
# humans = [Perso(0, (950, 6000), "human"), Perso(0, (8000, 6100), "human")]
# for h in humans:
#     draw_perso(h.get_x(), h.get_y(), "green")

# # Zombies
# zombies = [Perso(0, (3100, 7000), "zombie"), Perso(0, (11500, 7100), "zombie")]
# for z in zombies:
#     draw_perso(z.get_x(), z.get_y(), "red")
        