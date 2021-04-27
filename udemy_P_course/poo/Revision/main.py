#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|


# *************************EXO2******************
# 1) Ils ont le même nombre de caractére
# 2° ) Vérification si les lettres sont identiques des deux côté

def anagramme(word1, word2):
    ok = False
    if len(word1) == len(word2):
        if sorted(word1.lower()) == sorted(word2.lower()):
            ok = True
    return ok        
          
print(anagramme("police", "PICOLE")) 

print(sorted("THIORO"))