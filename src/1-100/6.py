squared_sum = sum(i ** 2 for i in range(1, 101))
sum_squared = sum(range(1, 101)) ** 2

difference = sum_squared - squared_sum

print(difference)
