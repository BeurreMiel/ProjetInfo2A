import os

# Fonction permettant de vider la console

def clear(): 
    return os.system('cls')

def listString(l : list): 
    return "[" + ", ".join(str(elem) for elem in l) + "]"

def listrotate(l, n):
    return l[n:] + l[:n]