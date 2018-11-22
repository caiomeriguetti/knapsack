# Explicação

Dado um conjunto de elementos x1, x2, ..., xn, seus respectivos valores v1, v2, ..., vn e pesos p1, p2, ..., pn. Precisamos
colocar um conjunto de elementos xi numa mochila de peso máximo P de modo que a soma dos valores dos elementos que foram
colocados dentro da mochila seja a máxima possível.

para cada peso 0, 1, ..., P calculamos a moxila maxima para o respectivo peso.


se f(i, p) é uma funcao que retorna a soma maxima para os i primeiros elementos, temos:

Se pi > p

f(i, p) = f(i - 1, p) // pois p não cabe na mochila

Se p1 <= p

f(i, p) = f(i - 1, p - pi) + vi // caso xi esteja dentro da mochila máxima

e

f(i, p) = f(i - 1, p) // caso xi não esteja dentro da mochila máxima

além disso f(i, 0) = f(0, p) = 0

