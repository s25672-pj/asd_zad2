import random
def lomuto_quicksort(A, i, j):
    if i < j:
        pivot = partition(A, i, j)
        lomuto_quicksort(A, i, pivot - 1)
        lomuto_quicksort(A, pivot + 1, j)
def partition(A, i, j):
    pivot = A[j]
    p_index = i
    for k in range(i, j):
        if A[k] <= pivot:
            A[p_index], A[k] = A[k], A[p_index]
            p_index += 1
    A[p_index], A[j] = A[j], A[p_index]
    return p_index
# generowanie losowej tablicy
n = 50
A = [random.randint(1, 100) for _ in range(n)]
# wyświetlenie nieposortowanej tablicy
print("Tablica przed sortowaniem")
print(A)
# sortowanie tablicy
lomuto_quicksort(A, 0, n-1)
# wyświetlenie posortowanej tablicy
print("Tablica po sortowaniu")
print(A)