def quicksort(vetor, indiceinicial=0, indiceparada=None):
    if indiceparada == None:
        indiceparada = len(vetor) - 1

    if indiceinicial < indiceparada:
        pivor = particao(vetor, indiceinicial, indiceparada)
        quicksort(vetor, indiceinicial, pivor - 1)
        quicksort(vetor, pivor + 1, indiceparada)


def particao(vetor, indiceinicial, indiceparada):
    indice_de_inicio = indiceinicial
    pivor = vetor[indiceparada][1]
    for i in range(indiceinicial, indiceparada):
        if vetor[i][1] >= pivor:
            vetor[indice_de_inicio], vetor[i] = vetor[i], vetor[indice_de_inicio]
            indice_de_inicio += 1

    else:
        vetor[indice_de_inicio], vetor[indiceparada] = vetor[indiceparada], vetor[indice_de_inicio]
    print(indice_de_inicio)
    return indice_de_inicio


lista = [['lose', -15], ['win', 55], ['a', 50]]
a = quicksort(lista)
print(lista)
