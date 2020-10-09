import itertools
nums = [1,2,3]
print(list(itertools.permutations(nums)))
print(list(map(list,itertools.permutations(nums))))