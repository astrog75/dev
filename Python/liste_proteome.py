import re

# file = open("human-proteome.fasta", "r")

# i = 1

# for line in file:
#     pos = []
#     for j, c in enumerate(line):
#         if c == '|':
#             pos.append(j)
    
#     if pos and i < 100:
#         print("protein " + f"{i:05}" + " " + line[pos[0]+1:pos[1]])
#         i += 1



# file = open("human-proteome.fasta", "r")

# model = re.compile("\|(\w*)\|")

# i = 1

# re.findall(model, line, 


# for line in file:
#     protein_name = re.findall(model, line)
    
#     if protein_name and i < 100:
#         print("protein " + f"{i:05}" + " " + protein_name[0])
#         i += 1
    

# 


with open("human-proteome.fasta", "r") as file:
    content = file.read()
    
protein_codes = re.findall(r"\|(\w*)\|", content, re.MULTILINE)

for i, p in enumerate(protein_codes):
    if i < 50:
        print("protein " + f"{i+1:05}" + " " + p)