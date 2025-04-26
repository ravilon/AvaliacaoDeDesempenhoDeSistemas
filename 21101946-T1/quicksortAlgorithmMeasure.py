import sys
import random
import time

# Constantes
studentId = '21101946'
startRangeSeed = 0.0
endRangeSeed = 1000.0

def createRandomNumbersList(numberOfItens):
    numbersList = []
    for i in range(numberOfItens):
        numbersList.append(random.uniform(startRangeSeed, endRangeSeed))
    return numbersList

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Input
numberOfItens = int(sys.argv[1])

# Create Randomized List
randomNumbersList = createRandomNumbersList(numberOfItens)

## Começando a contar o tempo apenas quando iniciamos o quick sort
start_time = time.time()

quicksort(randomNumbersList, 0, len(randomNumbersList) - 1)

## Finalizando o timer
elapsed = (time.time() - start_time)

print(f"{studentId},{elapsed:.8f}")
