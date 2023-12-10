import csv

def median(a):
    size = len(a)
    if size % 2 == 1:
        return a[size//2]
    else:
        return (a[(size // 2) - 1] + a[size // 2]) / 2.0

def quartile1(v):
    n = len(v)
    first = []
    for i in range(n // 2):
        first.append(v[i])
    return median(first)

def quartile3(v):
    n = len(v)
    last = []
    if n % 2 == 0:
        for i in range(n // 2, n):
            last.append(v[i])
    else:
        for i in range(n // 2 + 1, n):
            last.append(v[i])
    return median(last)

arr = []
with open('exp6/data6.csv', 'r') as in_file:
    csv_reader = csv.reader(in_file)
    next(csv_reader)  # Skip header
    for line in csv_reader:
        x = int(line[0])
        arr.append(x)

n = len(arr)
arr.sort()

with open('exp6/exp6_output.csv', 'w') as out_file:
    out_file.write("Minimum value: ," + str(arr[0]) + "\n")
    out_file.write("Quartile1 value: ," + str(quartile1(arr)) + "\n")
    out_file.write("Median value: ," + str(median(arr)) + "\n")
    out_file.write("Quartile3 value: ," + str(quartile3(arr)) + "\n")
    out_file.write("Maximum value: ," + str(arr[n-1]) + "\n")

print("Minimum value is", arr[0])
print("Q1:", quartile1(arr))
print("Median:", median(arr))
print("Q3:", quartile3(arr))
print("Maximum value is", arr[n - 1])



