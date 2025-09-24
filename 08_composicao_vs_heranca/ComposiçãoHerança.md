Ótimo. Aqui está um guia completo em Markdown sobre Composição e Herança.

# Composição vs. Herança em Python

Em programação orientada a objetos (POO), **composição** e **herança** são os dois principais mecanismos para reutilizar código e modelar relações entre classes. A escolha entre eles é uma decisão de design crucial que afeta a flexibilidade e a manutenibilidade do seu código.

  * **Herança:** Representa uma relação "é um".
  * **Composição:** Representa uma relação "tem um".

## 1\. Herança (Relação "É um")

A **herança** é um conceito em que uma classe (subclasse) herda atributos e métodos de outra classe (superclasse). Ela é ideal para modelar hierarquias naturais e comportamentos compartilhados.

### Analogia:

Pense em um `Carro` e um `Caminhão`. Ambos **são um** `Veículo`.

  * `Veículo` é a classe base.
  * `Carro` e `Caminhão` são subclasses que herdam as características e comportamentos de `Veículo`.

### Exemplo em Python:

```python
class Veiculo:
    def __init__(self, marca):
        self.marca = marca
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} ligou.")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def dirigir(self):
        if self.ligado:
            print(f"O {self.modelo} está sendo dirigido.")
        else:
            print(f"O {self.modelo} precisa estar ligado para dirigir.")

# Uso
meu_carro = Carro("Ford", "Focus")
meu_carro.ligar()
meu_carro.dirigir()
```

**Vantagens da Herança:**

  * Reutilização de código: Evita a duplicação de métodos e atributos comuns.
  * Clareza em hierarquias: Deixa a estrutura do sistema mais organizada.

**Desvantagens da Herança:**

  * **Acoplamento Forte:** A subclasse fica fortemente acoplada à superclasse. Uma mudança na classe base pode ter um impacto não intencional nas subclasses.
  * **Herança Múltipla:** Pode levar a complexidade e ambiguidade, como o problema do "diamante", embora Python lide com isso de forma mais controlada.
  * **Relação Rígida:** Não permite mudanças em tempo de execução. A hierarquia de classes é definida no momento da codificação.

-----

## 2\. Composição (Relação "Tem um")

A **composição** é um conceito em que uma classe contém instâncias de outras classes. A classe principal delega responsabilidades a essas instâncias contidas nela.

### Analogia:

Pense em um `Carro`. Um `Carro` não "é um" `Motor`. Um `Carro` **tem um** `Motor`.

  * A classe `Carro` contém uma instância da classe `Motor` como um de seus atributos.
  * A classe `Carro` delega a responsabilidade de "ligar" ao seu objeto `Motor`.

### Exemplo em Python:

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def ligar(self):
        print(f"O motor {self.tipo} ligou.")
        
    def desligar(self):
        print(f"O motor {self.tipo} desligou.")

class Pneus:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def rodar(self):
        print(f"Os {self.quantidade} pneus estão rodando.")

class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor) # Composição: Carro tem um Motor
        self.pneus = Pneus(4)          # Composição: Carro tem Pneus

    def ligar(self):
        self.motor.ligar() # Delega a responsabilidade para o objeto Motor
        
    def andar(self):
        self.pneus.rodar() # Delega a responsabilidade para o objeto Pneus

# Uso
meu_carro = Carro("Ford", "Focus", "gasolina")
meu_carro.ligar()
meu_carro.andar()
```

**Vantagens da Composição:**

  * **Acoplamento Fraco:** As classes são mais independentes. Você pode trocar o `Motor` por um elétrico ou a gasolina sem alterar a classe `Carro`.
  * **Flexibilidade:** Permite criar objetos com comportamentos mais dinâmicos. Você pode mudar a implementação de um componente em tempo de execução.
  * **SRP (Princípio da Responsabilidade Única):** Cada classe tem uma responsabilidade única (o `Motor` liga, os `Pneus` rodam, o `Carro` orquestra).

-----

## Conclusão: "Prefira Composição à Herança"

Essa frase é um dos conselhos de design mais importantes em POO. Use-a como regra geral, mas não como uma lei inquebrável.

  * Use **Herança** quando você tiver uma relação "é um" clara e bem definida, e a hierarquia de classes for estável e previsível.
  * Use **Composição** na maioria dos outros casos, quando a relação é "tem um" e você precisa de flexibilidade, baixo acoplamento e um sistema mais fácil de testar e manter.

Lembre-se: um sistema bem projetado usa ambos, mas tende a favorecer a composição para criar partes modulares e intercambiáveis.