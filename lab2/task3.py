n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

def median(lst):
    m = len(lst)
    if m % 2 == 1:
        return lst[m // 2]
    else:
        return (lst[m // 2 - 1] + lst[m // 2]) / 2.0

Q2 = median(data)

lower_half = [x for x in data if x < Q2]
upper_half = [x for x in data if x > Q2]

Q1 = median(lower_half)
Q3 = median(upper_half)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = sum(1 for x in data if x < lower_bound or x > upper_bound)

print(outliers)
