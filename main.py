import replit
import os
from replit import audio


print("PROMPTAI, by Xavier Sánchez 2024")
prompt = input("Dime la oracion que quieres que recite")
promptup = prompt.upper()
numprompt = len(prompt)
arprompt = list(promptup.replace("LL", "LL")) #Tengo las letras separadas de uno en uno + detecta la "LL".
print("Reproduciendo",prompt)
for i in arprompt:
    match i:
        case "A":
            audio.play_file("A.wav")
        case "B":
            audio.play_file("B.wav")
    """ case "C":
            audio.play_file('C.wav')
        case "D":
            audio.play_file('D.wav')
        case "E":
            audio.play_file('E.wav')
        case "F":
            audio.play_file('F.wav')
        case "G":
            audio.play_file('G.wav')
        case "H":
            continue
        case "I":
            audio.play_file('I.wav')
        case "J":
            audio.play_file('J.wav')
        case "K":
            audio.play_file('C.wav')
        case "L":
            audio.play_file('L.wav')
        case "M":
            audio.play_file('M.wav')
        case "N":
            audio.play_file('O.wav')
        case "P":
            audio.play_file('P.wav')
        case "Q":
            audio.play_file('C.wav')
        case "R":
            audio.play_file('R.wav')
        case "S":
            audio.play_file('S.wav')
        case "T":
            audio.play_file('T.wav')
        case "U":
            audio.play_file('U.wav')
        case "V":
            audio.play_file('B.wav')
        case "W":
            audio.play_file('B.wav')
        case "Y":
            audio.play_file('I.wav')
        case "Z":
            audio.play_file('Z.wav')
        case "Ñ":
            audio.play_file('Ñ.wav')
        case "LL":
            audio.play_file('LL.wav')
            """