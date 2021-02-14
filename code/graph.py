import numpy as np
import matplotlib.pyplot as plt

x = np.array(['a','b','c'])
y = np.array([22,5,8])
# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)

n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.pie(Z, explode=Z*.05, colors=['%f' % (i/float(n)) for i in range(n)],
        wedgeprops={"linewidth": 1, "edgecolor": "black"})
plt.gca().set_aspect('equal')
plt.xticks([]), plt.yticks([])

# savefig('../figures/pie_ex.png',dpi=48)
plt.show()