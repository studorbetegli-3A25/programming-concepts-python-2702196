def applica_sconto_benvenuto(prezzo_iniziale):
   return prezzo_iniziale - 5

prezzo_scarpe = 80
prezzo_finale_scarpe = applica_sconto_benvenuto(prezzo_scarpe)
print(f"il prezzo delle scarpe è: {prezzo_finale_scarpe}")

prezzo_pantaloni = 60
prezzo_finale_pantaloni = applica_sconto_benvenuto(prezzo_pantaloni)
print(f"il prezzo dei pantaloni è: {prezzo_finale_pantaloni}")

prezzo_maglietta = 25
prezzo_finale_maglietta = applica_sconto_benvenuto(prezzo_maglietta)
print(f"il prezzo della maglietta è: {prezzo_finale_maglietta}")