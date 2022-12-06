## 삽입 정렬

def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] =a[j]
            j -=1
        a[j+1] = key
    return a

x = [5,3,1,4,2,6]
print(x)
b = insertion_sort(x)

print(b)
