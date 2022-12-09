# HW3: swap left and right halfs of the list respecting the order 

data = [-5, 10, 15, 20, 5, 0, -10]

half_left_idx = int(len(data) / 2)
half_right_idx = round(len(data) / 2)


free      = data[0:half_left_idx]
data[0:half_left_idx] = data[half_right_idx:len(data)]
data[half_right_idx:len(data)] = free

print(data)

