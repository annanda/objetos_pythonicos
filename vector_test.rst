===========================
Testes para a classe vector
===========================

Deve ser possível criar um vetor::
    >>> from vector import Vector
    >>> vetor_1 = Vector(1, 2)

Deve ser possível somar dois vetores::
    >>> vetor_2 = Vector(4, 7)
    >>> vetor_1 + vetor_2
    Vector(5, 9)

Deve ser possível multiplicar um vetor por um número::
    >>> vetor_2 * 3
    Vector(12, 21)

Deve ser possível acessar o x e y do vetor através de índices::
    >>> vetor_1[0]
    1
