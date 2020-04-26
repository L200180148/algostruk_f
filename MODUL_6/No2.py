#Nomor 2

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def gabung(a,b):
    c = []
    c = a+b
    n = len(c)
    for i in range(n):
        for j in range(0, n-i-1):
            if c[j] > c[j+1]:
                c[j], c[j+1] = c[j+1], c[j]
    return c

a = [9, 15, 90, 27, 1, 55, 129]
b = [77, 76, 5, 25, 17]
a,b = bubblesort(a),bubblesort(b)

print(a)
print(b)
print(gabung(a,b))
