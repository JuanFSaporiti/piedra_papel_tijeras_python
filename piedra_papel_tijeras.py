jugador1 = input("Hola Jugador1! Que vas a elegir? Piedra, Papel o Tijeras?: ")
jugador2 = input("Hola Jugador2! Que vas a elegir? Piedra, Papel o Tijeras?: ")

if jugador1 == jugador2:
    print("Ha sido un empate!")
elif(jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ha ganado el jugador1")
else:
    print("Ha ganado el jugador2")
