from itertools import permutations
nums = ["777", "7", "77", "77"]
target = "7777"
# [i + j == target for i, j in permutations(nums, 2)]

perm = permutations(nums, 2)
count = 0
for i in list(perm):
    k, v = i[0], i[1]
    if k+v == target:
        count += 1
print(count)
