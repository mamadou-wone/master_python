#  ___       __   ________  ________   _______
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|



def drow_matrix(dash_num):
    dash = ""
    separator = ""
    display = ""
    for i in range(dash_num):
        dash += '_'
    dash = dash + '\n' + separator
    return dash

print('    |  X |  O ')
print(drow_matrix(15))
print('    |  X |  O ')
print(drow_matrix(15))
print('  O  |  X |  O ')