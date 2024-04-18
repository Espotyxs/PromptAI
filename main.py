print("PROMPTAI, by Xavier Sánchez 2024")
prompt = input("Dime la oracion que quieres que recite")
promptup = prompt.upper()
numprompt = len(prompt)
arprompt = list(promptup) #Tengo las letras separadas de uno en uno + detecta la "LL".
print("Reproduciendo",prompt)
paster = ""
for i in arprompt:
    match i:
        case "A":
         paster = paster + str("Alpha") + " " 
        case "B":
         paster = paster + str("Bravo") + " "
        case "C":
         paster = paster + str("Charlie") + " "
        case "D":
          paster = paster + str("Delta") + " "
        case "E":
          paster = paster + str("Echo") + " "
        case "F":
          paster = paster + str("Foxtrot") + " "
        case "G":
          paster = paster + str("Golf") + " "
        case "H":
          paster = paster + str("Hotel") + " "
        case "I":
          paster = paster + str("India") + " "
        case "J":
          paster = paster + str("Juliet") + " "
        case "K":
          paster = paster + str("Kilo") + " "
        case "L":
          paster = paster + str("Lima") + " "
        case "M":
          paster = paster + str("Mike") + " "
        case "N":
          paster = paster + str("November") + " "
        case "O":
          paster = paster + str("Oscar") + " "
        case "P":
          paster = paster + str("Papa") + " "
        case "Q":
          paster = paster + str("Quebec") + " "
        case "R":
          paster = paster + str("Romeo") + " "
        case "S":
          paster = paster + str("Sierra") + " "
        case "T":
          paster = paster + str("Tango") + " "
        case "U":
          paster = paster + str("Uniform") + " "
        case "V":
          paster = paster + str("Victor") + " "
        case "W":
          paster = paster + str("Whiskey") + " "
        case "Y":
          paster = paster + str("Yankee") + " "
        case "Z":
          paster = paster + str("Zulu") + " "
        case "Ñ":
          paster = paster + str("Ñoño") + " "
        case other:
          paster = paster + str(" | ")

paster = paster + str(paster)