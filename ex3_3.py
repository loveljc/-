dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 1 in [3,4,5,6]:
        dayup = dayup * (1 + dayfactor)
print("10天休息一次: {:.2f}.".format(dayup))
for i in range(365):
    if i % 16 in [4,5,6,7,11,12,13,14]:
        dayup = dayup * (1 + dayfactor)
print("15天休息一次: {:.2f}.".format(dayup))
