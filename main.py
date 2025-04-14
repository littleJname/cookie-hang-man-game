teBetalen = 0
nogEenProduct = "ja"
while nogEenProduct == "ja":
  prijs = float(input("Wat is de prijs van het product dat u koopt?"))
  teBetalen = teBetalen + prijs
  
  nogEenProduct = input("Wilt u nog een product invoeren?")
print("TOTAAL: " + str(teBetalen) + " EUR.")