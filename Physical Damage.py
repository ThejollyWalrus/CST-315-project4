import numpy as df
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#This will be the function that returns the ODE


def model  (y, t, p):
    # part 1 of the equation
    # the equation after its last derivative
    # s1 = (p / ) * (s * s)
    s = (y / 100) * (.5 * 1.3038)
    s1 = s * (p * 1.64)

    return s1
    # setting our y variable
    # amout of years used


y0 = 20
# creating the line spacing in our graph
t = df.linspace(0, 2048)
# p = amout of data backs ups
p0 = 7
#these are the 3 different version that solve our ODE
run1 = odeint(model, y0, t, args=(p0,))
#This where we plot our results
plt.plot(t, run1, 'r--', label='Amount of data transfers 7')

plt.xlabel('Amount of data getting lost')
plt.ylabel('Time')
plt.legend(loc='upper left')
plt.title('Physical Damage data integrity')
plt.show()

