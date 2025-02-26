import matplotlib.pyplot as plt


# 산점도

y_value = [10,50,20,10]
x_value = [1,2,3,4]

size = []

for y in y_value:
	size.append(y*5)


plt.scatter(x_value,y_value, s= size, c=range(4), cmap='jet')

# 우측에 color bar 를 추가함
plt.colorbar()
plt.show()