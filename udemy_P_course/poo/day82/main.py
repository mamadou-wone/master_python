#  ___       __   ________  ________   _______
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|



def drow_dash(dash_num):
    dash = ""
    separator = ""
    display = ""
    for i in range(dash_num):
        dash += '_'
    dash = dash + '\n' + separator
    return dash

# print('    |  X |  O ')
# print(drow_dash(15))
# print('    |  X |  O ')
# print(drow_dash(15))
# print('  O  |  X |  O ')

def draw_matrix(x):
    print(f"  {x}   |   |   ")
    print(drow_dash(15))
    print('    |   |   ')
    print(drow_dash(15))
    print('    |   |   ')


  # [0, 4, 0],
  #   [2, 0, 0],
  #   [0, 0, 0],
A = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9],
]
# A[1][0] = 9
B = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]


# A = [
#     [0, 4, 0],
#     [2, 0, 7],
#     [0, 1, 3],
# ]
def verif_list(list):
    stop = False
    for i in range(0, len(list), 1):
        for j in range(1, len(list), 1):
            print(f"{i}" + " " + f"{j}")
            print(f"{list[i][i]}" +" & " + f"{list[i][j]}")
            print(list[i][i] == list[i][j])
            if list[i][i] == list[i][j] or list[i][i] == list[j][i]:
                stop = True


    return stop
# print(A[0][2])
print(verif_list(A))
# print("X" == "X" == "Z")
# start = True
# count = 0
# while start:
#     i = int(input("Enter the column number: "))
#     j = int(input("Enter the row number: "))
#     choice = input("Enter your choice: ")
#     B[j - 1][i - 1] = choice
#     for item in B:
#         for val in item:
#             if val != '':
#                 count += 1
#         if count == 9:
#             start = False
#     count = 0
#
#     print(B)
#
#
# display = ""
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         display += " " + str(B[i][j])
#         if(j == len(B[i]) - 1):
#             display += '\n'
#
# print(display)