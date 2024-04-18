

print("PROMPTAI, by Xavier Sánchez 2024")
prompt = input("Dime la oracion que quieres que recite")
promptup = prompt.upper()
numprompt = len(prompt)
arprompt = list(promptup) #Tengo las letras separadas de uno en uno + detecta la "LL".
print("Reproduciendo",prompt)
l = []
for i in arprompt:
    match i:
        case "A":
         l.append("Alpha")   
        case "B":
         l.append("Bravo")
        case "C":
         l.append("Charlie")
        case "D":
          l.append("Delta")
        case "E":
          print("Echo")
        case "F":
          print("Foxtrot")
        case "G":
          print("Golf")
        case "H":
          print("Hotel")
        case "I":
          print("India")
        case "J":
          print("Juliet")  
        case "K":
          print("Kilo")
        case "L":
          print("Lima")
        case "M":
          print("Mike")
        case "N":
          print("November")
        case "O":
          print("Oscar")
        case "P":
          print("Papa")
        case "Q":
          print("Quebec")
        case "R":
          print("Romeo")
        case "S":
          print("Sierra")
        case "T":
          print("Tango")
        case "U":
          print("Uniform")
        case "V":
          print("Victor")
        case "W":
          print("Whiskey")
        case "Y":
          print("Yankee")
        case "Z":
          print("Zulu")
        case "Ñ":
          print("Ñoño")
        case other:
          print(" ")

print(l)