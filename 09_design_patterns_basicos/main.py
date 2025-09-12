from singleton import Singleton
from factory_method import CachorroFactory, GatoFactory
from observer import Subject, ObservadorConcreto

def demo_singleton():
    print("=== Demo Singleton ===")
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1 is s2? {s1 is s2}\n")

def demo_factory_method():
    print("=== Demo Factory Method ===")
    cachorro_factory = CachorroFactory()
    cachorro = cachorro_factory.criar_animal()
    cachorro.emitir_som()

    gato_factory = GatoFactory()
    gato = gato_factory.criar_animal()
    gato.emitir_som()
    print()

def demo_observer():
    print("=== Demo Observer ===")
    subject = Subject()

    obs1 = ObservadorConcreto("Observer 1")
    obs2 = ObservadorConcreto("Observer 2")

    subject.adicionar_observer(obs1)
    subject.adicionar_observer(obs2)

    subject.notificar_observers("Evento importante chegou!")
    print()

if __name__ == "__main__":
    demo_singleton()
    demo_factory_method()
    demo_observer()
