#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

timingseden=(19, 10.614, 6.721, 4.767)
timingsstd=(3.423, 1.867, 1.086, 1.354)

def calc_speedup(xs):
    base=xs[0]
    res=[]
    for x in xs:
        res.append(base/x)
    return res

improvementseden = calc_speedup(timingseden)
improvementsstd = calc_speedup(timingsstd)

# add some
ax.set_ylabel('s')
ax.set_xlabel('CPUs')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1', '2', '4', '8') )
ax.set_ylim((0,60))
ax.grid(True,which="both",ls="-")
rects1=ax.bar(ind, timingseden, width, color='b')
rects2=ax.bar(ind+width, timingsstd, width, color='r')

ax.legend( (rects1[0], rects2[0]), ('Eden', 'Default') )
fig.savefig("runtimes.png")
#fig.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.set_ylabel('Speedup')
ax.set_xlabel('CPUs')
ax.set_xticks(ind)
ax.set_xticklabels( ('1', '2', '4', '8') )
ax.plot(improvementseden, color='b')
ax.plot(improvementsstd, color='r')
ax.grid(True,which="both",ls="-")
ax.legend( (rects1[0], rects2[0]), ('Eden', 'Default') )
fig2.savefig("speedup.png")
#fig2.show()
