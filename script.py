import matplotlib.pyplot as plt

datax = []
datay = []
for line in open("array_info.txt"):
    values = line.split()
    datax.append(int(values[0]))
    datay.append(float(values[1]))

# for x, y in zip(datax, datay):
#     print(x, "-" ,y)
fig, ax = plt.subplots()
ax.scatter(datax, datay)
ax.locator_params(integer=True)
ax.set(xlim=(94,100), ylim=(0,20))
plt.show()
