# This file was created by: Gannon O'Leary

'''
Algorithms:
set of instructions to solve problems
- counting number of people in a room
- N is variable
- For each person in the room N will increase by 1
-Set N equal to 2 for pairs


'''
# N = 0

# room = ["Bill", "Ted", "Socrates", "Sam", "Frodo"]
# # a for loop goes for a set number for times based on some perameter
# # # the i in this case holds the values in the list room
# for i in room:
#    print(i)
#    N += 1
#    print(N)

# pair = 0

# for i in room:
#     pair += 1
#     if pair == 2:
#         # print("we have a pair!")
#         N += 2
#         print(pair)
#         pair = 0
#         if N % 2 == 1:
#             N += 1
#     print(N)

level1 = [".E...",
          ".WW..",
          ".....",
          "..p..",
          "WWWWW",]

print(level1)
print(level1[0])
print(level1[0][0])

# print(list(enumerate(level1)))

# nested for loop
for row in level1:
    print(row)
    for col in row:
        print(col)
