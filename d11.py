def flip(arr):
    for i in range( len(arr)):
        for j in range(i, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

def pretty(arr):
    for row in arr:
        for item in row:
            print(item, end='')
        print()


with open("input_d11.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]

blank_rows = []
for i in range(len(data)):
    if all(map(lambda x : x == '.', data[i])):
        blank_rows.append(i)

print(blank_rows)
for row in reversed(blank_rows):
    data.insert(row, ['.']*len(data[0]))

flip(data)
# blank_cols = []
# for i in range(len(data)):
#     if all(map(lambda x : x == '.', data[i])):
#         blank_cols.append(i)

# for row in reversed(blank_cols):
#     data.insert(row, ['.']*len(data[0]))

# flip(data)

pretty(data)
