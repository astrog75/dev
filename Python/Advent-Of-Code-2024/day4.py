with open("input.txt", "r") as f:
    data = f.read().splitlines()

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

target = 'XMAS'

# rows
res = sum(row.count(target) + row.count(target[::-1]) for row in data)
print(res)

# columns
res += sum(''.join(col).count(target) + ''.join(col).count(target[::-1]) for col in zip(*data))
print(res)

sub_data = [d[:5] for d in data[:5]]
for d in sub_data:
    print(d)

# data = sub_data
# diagonals
print()
# diagonals starting from leftmost column
# for i in range(len(data)):
#     curr_diag = ""
#     for j, k in zip(range(i, len(data)), range(len(data))):
#         curr_diag += data[j][k]
#     #print(curr_diag)
#     res += curr_diag.count(target) +  curr_diag.count(target[::-1])

# # diagonals starting from top row
# for i in range(1,len(data)):
#     curr_diag = ""
#     for j, k in zip(range(len(data)), range(i, len(data))):
#         curr_diag += data[j][k]
#     #print(curr_diag)
#     res += curr_diag.count(target) +  curr_diag.count(target[::-1])

# # antidiagonals starting from leftmost column
# for i in range(len(data)):
#     curr_diag = ""
#     for j, k in zip(range(len(data)-1-i,-1,-1), range(len(data))):
#         curr_diag += data[j][k]
#     #print(curr_diag)
#     res += curr_diag.count(target) +  curr_diag.count(target[::-1])

# # antidiagonals starting from bottom row
# for i in range(1,len(data)):
#     curr_diag = ""
#     for j, k in zip(range(len(data)-1, -1, -1), range(i, len(data))):
#         curr_diag += data[j][k]
#     print(curr_diag)
#     res += curr_diag.count(target) +  curr_diag.count(target[::-1])

# print(res)

n = len(data)
for k in range(n):
    curr_diag = ""
    for i in range(n-k):
        curr_diag += data[i][i+k]
    print(curr_diag)
    
for k in range(n):
    curr_diag = ""
    for i in range(n-k):
        curr_diag += data[i+k][i]
    print(curr_diag)

