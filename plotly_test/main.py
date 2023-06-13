import plotly.express as px
import random

qnt = 10

y = [0]
for i in range(qnt):
    new_num = random.randint(y[i] - 2, y[i] + 2)
    y.append(new_num)
    print(f'NUM: {new_num}')

x = []
for i in range(len(y)):
    x.append(i)

fig = px.line(x=x, y=y)
fig.show()