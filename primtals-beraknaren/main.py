def main(): # funktion
  numInput = input("Skriv ett tal:")
  if numInput.isdigit():
    num = int(numInput)
  else:
    print("Det där var inget tal försök igen")
    main();
    return

  # primtal är mer än 1
  if num > 1:
    for i in range(2,num): # kolla alla siffror mellan 2(det första primtalet) och ditt tal
        if (num % i) == 0: # det som blir kvar om man delar det på i variabeln
            print(num,"är inte ett primtal")
            print(i,"*",num//i,"är",num)
            break
    else:
        print(num,"är ett primtal")
        
  else:
    print(num,"är inte ett primtal")
main(); # kör funktionen