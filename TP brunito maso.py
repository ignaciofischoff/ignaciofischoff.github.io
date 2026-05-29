import random  

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        apodos = {
            1: "Ancho", 
            10: "Sota",
            11: "Caballo", 
            12: "Rey"
        }
        
        if self.numero in apodos:
            return f"{apodos[self.numero]} de {self.palo}"
        else:
            return f"{self.numero} de {self.palo}"

    def __eq__(self, other):
        if self.numero == other.numero:
            print("Empate")
            return True
        return False


class Mazo:
    def __init__(self):
        self.cartas = []
        palos = ["Espada", "Basto", "Copas", "Oro"]
        for n in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
            for p in palos:
                self.cartas.append(Carta(n, p))

    def mezclar(self):
        random.shuffle(self.cartas)

    def mostrar_mazo(self):
        for carta in self.cartas:
            print(f"- {carta}")

    def sacar_carta(self):
        return self.cartas.pop()

    def cantidad_cartas(self):
        return len(self.cartas)


if __name__ == "__main__":
    mi_mazo = Mazo()
    
    print(f"Cartas iniciales en el mazo: {mi_mazo.cantidad_cartas()}")
    print("--- MAZO INICIAL ORDENADO ---")
    mi_mazo.mostrar_mazo()
    
    print("\n--- MEZCLANDO EL MAZO ---")
    mi_mazo.mezclar()
    
    print("\n--- MAZO MEZCLADO ---")
    mi_mazo.mostrar_mazo()
    print(f"Cantidad de cartas tras mezclar: {mi_mazo.cantidad_cartas()}")
    
    print("\n--- SACANDO UNA CARTA ---")
    carta_aleatoria = mi_mazo.sacar_carta()
    print(f"Tu carta es: {carta_aleatoria}")
    print(f"\nQuedan {mi_mazo.cantidad_cartas()} cartas en el mazo.")