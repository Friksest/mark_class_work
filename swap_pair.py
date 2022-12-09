# HW2: swap pair 2,3 and with 4,5

data = [-5, 10, 15, 20, 5, 0, -10]


free      = data[2:4]
data[2:4] = data[4:6]
data[4:6] = free

print(data)