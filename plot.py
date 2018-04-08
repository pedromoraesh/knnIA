import matplotlib.pyplot as plt
import csv

xh = []
yh = []
xm = []
ym = []
wd = csv.reader(open('alturapeso.csv'))
for line in wd:
	if line[2] == '0':
		xh.append(float(line[0]))
		yh.append(float(line[1]))
	else:
		xm.append(float(line[0]))
		ym.append(float(line[1]))

plt.plot(xm,ym, 'ro', label='Mulhere', color = 'r')	
plt.plot(xh,yh, 'ro', label='Homem', color = 'b')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.title('Peso/Altura')
plt.legend()
plt.show()