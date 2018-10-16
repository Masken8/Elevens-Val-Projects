print("Välkommen till sträck beräknaren") #välkommen meddelande
def main(): #funktion
  global v,t,vT,sT #Bug fix: variablerna måste vara globala för att skrivas igen om funktionen körs om. Använd INTE global om du inte behöver kan bli ett problem i större skript!
  vT = input("Skriv in din hastighet: ") #input från tangentbordet till sträng variabel
  sT = input("Skriv in din tid: ") #input från tangentbordet till sträng variabel
  if vT.isdigit(): #kolla om strängen är bara nummer
    v = int(vT) #gör om strängen till integer
  else: #annars
    print("talet du angav är en ogiltlig integer")
    main() #kör funktionen igen
    return #stoppa den nuvarande funktionen så att sträckan inte skrivs ut två gånger
  if sT.isdigit(): #kolla om strängen är bara nummer
    t = int(sT) #gör om strängen till integer
  else: #annars
    print("talet du angav är en ogiltlig integer")
    main() #kör funktionen igen
    return #stoppa den nuvarande funktionen så att sträckan inte skrivs ut två gånger
  s=v*t #räkna ut sträcka
  print("Din sträcka är:", s) #skriv ut sträckan
main() #kör funktionen
