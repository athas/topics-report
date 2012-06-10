#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

tests={'blackscholes 1000 20000000' :
           ([3*60+26.987, 1*60+51.707, 58.174, 39.158, 31.797, 26.068, 22.948, 21.636, 19.352, 21.150, 17.321, 16.642, 15.399],
            [2*60+4.681, 58.323, 32.971]),
       'parfib_monad "monad" 50 30' :
           ([3*60+44.591, 1*60+52.125, 57.597, 39.657, 29.401, 23.819, 21.227, 18.711, 16.800, 15.063, 13.845, 12.030, 12.179],
            [3*60+34.164, 1*60+47.196, 53.736])
       }

def calc_speedup(xs):
    base=xs[0]
    res=[]
    for x in xs:
        res.append(base/x)
    return res

CPUs=('1', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24')
for desc,timings in tests.items():
    timingseden=timings[0]
    timingsstd=timings[1]
    N=len(timingseden)
    timingsstd += (N-len(timingsstd))*[timingsstd[-1]]
    ymax=max(max(timingseden),max(timingsstd))

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35        # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    improvementseden = calc_speedup(timingseden)
    improvementsstd = calc_speedup(timingsstd)

    # add some
    ax.set_title(desc)
    ax.set_ylabel('Seconds')
    ax.set_xlabel('CPUs')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( CPUs )
    ax.set_ylim((0,ymax))
    ax.grid(True,which="both",ls="-")
    rects1=ax.bar(ind, timingseden, width, color='b')
    rects2=ax.bar(ind+width, timingsstd, width, color='r')

    ax.legend( (rects1[0], rects2[0]), ('Eden', 'Default') )
    fig.savefig(desc.split(' ')[0]+"-runtimes.png")

    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    ax.set_title(desc)
    ax.set_ylabel('Relative speedup')
    ax.set_xlabel('CPUs')
    ax.set_xticks(ind)
    ax.set_xticklabels( CPUs )
    ax.plot(improvementseden, color='b')
    ax.plot(improvementsstd, color='r')
    ax.grid(True,which="both",ls="-")
    ax.legend((rects1[0], rects2[0]), ('Eden', 'Default'),loc=2)
    fig2.savefig(desc.split(' ')[0]+"-speedup.png")
