from heranca import Carro as CarroHeranca
from composicao import Motor, Carro as CarroComposicao

def demo_heranca():
    print("=== Exemplo com Herança ===")
    carro = CarroHeranca("Ford", "Mustang", 2)
    carro.mover()
    carro.tocar_radio()

def demo_composicao():
    print("\n=== Exemplo com Composição ===")
    motor_v8 = Motor(450)
    carro = CarroComposicao("Chevrolet", "Camaro", motor_v8)
    carro.mover()

if __name__ == "__main__":
    demo_heranca()
    demo_composicao()
