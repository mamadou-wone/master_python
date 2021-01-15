#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

student_heights = input("Input a list of student heights ").split()
sum = 0
averrage = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum += int(student_heights[n])

averrage = sum / len(student_heights)
print(round(averrage))  
