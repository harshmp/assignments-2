n = input("Enter the size of array: ")
a = []

print("Enter the numbers: ")
i = 0
while i < n:
    a.append(input())
    i = i + 1

a.sort()

key = input("Enter the number to be searched: ")

left = 0
right = n - 1
mid = (left + right) // 2

if key not in a:
    print("Not found!")
else:
    while left <= right:
        if key == a[mid]:
            print("Found at position: " + str(mid + 1))
            break
        elif key > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
