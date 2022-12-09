data = [-5, 10, 15, 20, 5, 0, -10]

# HW1. left half with a value given from a kb
ch_data = int(input("Call a number for change: "))
half_idx = round(len(data) / 2)
for i in range(0, half_idx):
    data[i] = ch_data
print(data)
