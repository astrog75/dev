import string
import os

import torch
import matplotlib.pyplot as plt

import pickle

# open a pickle file
# filename = 'trigram_matrix.pk'
filename = None

# Load data
with open("names.txt", 'r') as f:
    list_names = f.read().splitlines()

alphabet = string.ascii_lowercase
# Encoder bigrams
stoi_chars = {c:i+1 for i,c in enumerate(alphabet)}
stoi_chars['.'] = 0

stoi_bigrams = {}
i = 0
for l1 in '.'+alphabet:
    for l2 in '.'+alphabet:
        stoi_bigrams[l1+l2] = i
        i+=1

# Decoder
#itos = {i:c for c,i in stoi.items()}


N = torch.zeros((len(stoi_bigrams), 27), dtype=torch.int32)

for name in list_names:
    chars = ['.'] + list(name) + ['.']
    for c1, c2, c3 in zip(chars, chars[1:], chars[2:]):
        N[stoi_bigrams[c1+c2], stoi_chars[c3]] += 1

# try:
#     if filename is not None:
#         f = open(filename, 'rb')
#         N = pickle.load(f)
# except:
#     if f != None:
#         # f = open(filename, 'wb')

#     # Construct trigrams matrix
#     N = torch.zeros((len(stoi_bigrams), 27), dtype=torch.int32)
    
#     for name in list_names[:10]:
#         chars = ['.'] + list(name) + ['.']
#         for c1, c2, c3 in zip(chars, chars[1:], chars[2:]):
#             print(c1+c2,c3)
#             N[stoi_bigrams[c1+c2], stoi_chars[c3]] += 1
        
#         #pickle.dump(N, f)
#         #f.close()

#plt.figure(figsize=(16,16))
#index_sample = n_nexts
#g = torch.Generator().manual_seed(42)
#index = torch.randint(0, n_formers, (index_sample,), generator = g)
# plt.imshow(N, cmap='Blues')
# for i in range(27):
#     for j in range(27):
#         for k in range(27):
#             chstr = itos[i]+itos[j]+itos[k]
#             plt.text((i,j), k, chstr, ha="center", va="bottom", color='k')
#             plt.text((i,j), k, N[(i,j), k].item(), ha="center", va="top", color='k')
# plt.axis('off');

print(N.shape)
plt.imshow(N, cmap="Blues", aspect="auto")

# # Normalize the matrix N1
# Normalized_N = (N+1).float()
# Normalized_N /= Normalized_N.sum(1, keepdim=True)

# Construct some names using bigrams distributions
# g = torch.Generator().manual_seed(150)
# nll = 0
# count_tg = 0

# for i in range(100):
#     out = []
#     a = 5
#     while a != 0:
#         b = torch.multinomial(Normalized_N1[a], num_samples=1, replacement=True, generator=g).item()
#         nll -= torch.log(Normalized_N1[a, b])
#         if itos[b] != '.':
#             c = torch.multinomial(Normalized_N2[b], num_samples=1, replacement=True, generator=g).item()
#             nll -= torch.log(Normalized_N2[b, c])
#         else:
#             out += '.'
#             break
#         out += itos[b], itos[c]
#         a = b
#         count_tg += 2
        
#     print(''.join(out))    

# nll /= count_tg

# print(f"{nll.item()=}")




