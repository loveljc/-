dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 not in [3,4,5,6]:
        dayup = dayup * (1 + dayfactor)
print("连续努力365天: {:.2f}.".format(dayup))

