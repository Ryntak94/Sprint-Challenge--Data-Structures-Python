import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names = BinarySearchTree(names_1[0])
names2 = BinarySearchTree(names_1[0])
duplicates = []
# duplicates2 = []
# duplicates3 = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# length1 = len(names_1)
# length2 = len(names_2)
# length = length1 + length2
# for i in range(1, length):
#     if i <= 9999:
#         if names2.contains(names_1[i]):
#             duplicates2.append(names_1[i])
#         else:
#             names2.insert(names_1[i])
#     else:
#         if names2.contains(names_2[i - 10000]):
#             duplicates2.append(names_2[i - 10000])
#         else:
#             names2.insert(names_1[i - 10000])
length1 = len(names_1)
length2 = len(names_2)
length = length1 + length2
for i in range(1, length):
    if i <= 9999:
        if names2.contains(names_1[i]):
            duplicates.append(names_1[i])
        else:
            names2.insert(names_1[i])
    else:
        if names2.contains(names_2[i - 10000]):
            duplicates.append(names_2[i - 10000])
        else:
            names2.insert(names_1[i - 10000])
# for name_1 in duplicates:
#     for name_2 in duplicates2:
#         if name_1 == name_2:
#             duplicates3.append(name_1)
#
# print(len(duplicates3))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
