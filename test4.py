import math
import numpy as np


def expr(lam):
    return -math.log(np.random.uniform(0, 1)) / lam

service = 100*[0]
for i in range(100):
    service[i] = expr(8)

arrival = 100*[0]
for i in range(1, 100):
    # arrival[i] = arrival[i-1] + expr(0.1)
    arrival[i] = arrival[i-1] + expr(0.1)
    # arrival[i] = arrival[i-1] + np.random.poisson(1)



enter_service_time, leave_service_time = 100*[0], 100*[0]
leave_service_time[0] = service[0]

for i in range(1, 100):
    if leave_service_time[i-1] < arrival[i]:
        enter_service_time[i] = arrival[i]
    else:
        enter_service_time[i] = leave_service_time[i-1]
    leave_service_time[i] = enter_service_time[i] + service[i]
    print(leave_service_time[i])

