
---

## Iteradores e Geradores em Python

### Explicação

Iteradores e geradores são recursos poderosos do Python para trabalhar com sequências de dados, especialmente quando os conjuntos são grandes ou infinitos.

* **Iterador:** é um objeto que percorre uma sequência, lembrando sua posição atual. Ele fornece os elementos **um de cada vez** até que não haja mais nada a entregar. Em Python, qualquer objeto que implemente os métodos `__iter__()` e `__next__()` é considerado um iterador. Um loop `for` normalmente lida automaticamente com esses métodos.

* **Gerador:** é uma forma **mais prática e eficiente** de criar um iterador sem escrever toda a classe. Um gerador é uma função que utiliza `yield` para retornar valores **sob demanda**. Cada chamada ao gerador “retoma” a execução exatamente de onde parou, produzindo apenas o próximo item da sequência.

---

### Analogia

Imagine que você está em uma cafeteria:

* **Iterador:** o barista já preparou um grande lote de café e colocou em uma bancada. Cada vez que você pede um copo, ele pega da bancada. Tudo já está pronto, mas ocupa espaço de uma vez só.

* **Gerador:** o barista não faz nenhum café antecipadamente. Ele tem uma máquina que produz **um copo de cada vez**. Quando você pede, ele prepara exatamente aquele copo e “pausa” a máquina, esperando o próximo pedido. Assim, ele **economiza espaço e tempo**, produzindo apenas o necessário.

> Geradores são ideais quando você não precisa de todos os dados de uma vez ou trabalha com grandes volumes de informação.

---

### Entrevista Técnica

**P: Qual a principal diferença entre um iterador e um gerador?**
**R:** Um iterador é um conceito mais amplo — qualquer objeto que implemente `__iter__` e `__next__`. Um gerador é uma **forma específica e prática** de criar um iterador usando `yield`. Todo gerador é um iterador, mas nem todo iterador é um gerador.

**P: Por que usar um gerador em vez de uma lista?**
**R:** **Eficiência de memória.** Listas carregam todos os elementos na memória. Geradores produzem valores sob demanda, evitando sobrecarga de memória, especialmente útil para milhões de itens ou fluxos infinitos de dados.

**P: Qual a função da palavra-chave `yield`?**
**R:** `yield` transforma uma função em um gerador. Quando o Python encontra `yield`, ele **pausa a execução da função**, entrega o valor atual e salva o estado. Na próxima chamada, a função retoma exatamente de onde parou, produzindo o próximo valor.

---


