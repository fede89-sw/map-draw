import folium
print("""
Questo programma crea una mappa terrestre di un punto di cui l'utente passa le coordinate decimali(DD)!
""")
latitudine=float(input("Inserisci la Latitudine: "))
longitudine=float(input("Inserisci la Longitudine: "))
m=folium.Map(location=[latitudine, longitudine])
m.save('.\\map.html')