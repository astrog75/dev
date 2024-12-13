import string
import os

import torch
import matplotlib.pyplot as plt

# import pickle

# open a pickle file
filename = 'bigram_matrix.pk'

# Load data
with open("names.txt", 'r') as f:
    list_names = f.read().splitlines()

alphabet = string.ascii_lowercase
# Encoder
stoi = {c:i+1 for i,c in enumerate(alphabet)}
stoi['.'] = 0

# Decoder
itos = {i:c for c,i in stoi.items()}

# Construct bigrams matrix
def train(data):
    N = torch.zeros((27, 27), dtype=torch.int32)
    
    for name in data:
        chars = ['.'] + list(name) + ['.']
        for c1, c2 in zip(chars, chars[1:]):
            N[stoi[c1], stoi[c2]] += 1
    
    # Normalize the matrix N
    Normalized_N = (N+1).float()
    Normalized_N /= Normalized_N.sum(1, keepdim=True)
    
    return Normalized_N

# Creating train set, val set and test set for evaluation
i = int(0.1*len(list_names))
j = int(0.9*len(list_names))
train_set = list_names[:i]
val_test = list_names[i+1:j]
test_set = list_names[j+1:]

weights = train(train_set)

def evaluate_model(data, weights):
    g = torch.Generator().manual_seed(torch.randint(10000,size=(1,)).item())
    nll = 0
    count_bg = 0
    
    for i in range(len(data)):
        # out = []
        ix = torch.randint(low=0, high=27, size=(1,))
        while ix != 0:
            prev = ix
            ix = torch.multinomial(weights[ix], num_samples=1, replacement=True, generator=g).item()
            # out += itos[ix],
            nll -= torch.log(weights[prev, ix])
            count_bg += 1
            
        #print(''.join(out))    
    
    nll /= count_bg
    
    return nll.item()

for data in [train_set, val_test, test_set]:
    print(evaluate_model(data,weights))


