### this analyser use Jaccard similarity to make 2-cluser result
import sys

A = []
B = []
NumOfAttr = 0
Max = 0
Min = 0
def getJaccardCoefficent(idx, sim, tot):
    global NumOfAttr
    global Max
    global Min
    global A
    global B

    if idx == NumOfAttr:
        if tot == 0:
            return 0
        if sim/tot > Max:
            Max = sim/tot
        if sim/tot < Min:
            Min = sim/tot
        return 0
    case = A[idx] | B[idx]
    if case == 1:
        getJaccardCoefficent(idx + 1, sim + 1, tot + 1)
    elif case == 2:
        getJaccardCoefficent(idx + 1, sim, tot)
    elif case == 3:
        getJaccardCoefficent(idx + 1, sim, tot + 1)
    elif case == 4:
        getJaccardCoefficent(idx + 1, sim + 1, tot + 1)
        getJaccardCoefficent(idx + 1, sim, tot)
        getJaccardCoefficent(idx + 1, sim, tot + 1)
    elif case == 5:
        getJaccardCoefficent(idx + 1, sim + 1, tot + 1)
        getJaccardCoefficent(idx + 1, sim, tot + 1)
    elif case == 6:
        getJaccardCoefficent(idx + 1, sim, tot)
        getJaccardCoefficent(idx + 1, sim, tot + 1)

def analysDataTo2Clusters(filename):
    global Max
    global Min
    global A
    global B
    global NumOfAttr

    f = open(filename, "r")
    exf1 = open("origin1.csv", "w")
    exf2 = open("origin2.csv", "w")
    simf1 = open("cluster1.csv", "w")
    simf2 = open("cluster2.csv", "w")
    lcnt = 1
    idx = 0
    firstLine = f.readline()
    for c in firstLine.split(','):
            if idx == 0:
                if c == "republican":
                    exf1.write(str(lcnt) + "\n")
                else:
                    exf2.write(str(lcnt) + "\n")
            elif c == "y":
                A.append(1)
            elif c == 'n':
                A.append(2)
            else:
                A.append(4)
            idx += 1
    simf1.write("1\n")   
    NumOfAttr = idx - 1     
    for line in f:
        idx = 0
        lcnt += 1
        B = []
        for c in line.split(','):
            if idx == 0:
                if c == "republican":
                    exf1.write(str(lcnt) + "\n")
                else:
                    exf2.write(str(lcnt) + "\n")
            elif c == "y":
                B.append(1)
            elif c == 'n':
                B.append(2)
            else:
                B.append(4)
            idx += 1
        Max = -100000.
        Min = 100000.
        getJaccardCoefficent(0, 0., 0.)
        if Max-0.5 > 0.5-Min:
            simf1.write(str(lcnt) + "\n")
        else:
            simf2.write(str(lcnt) + "\n")
#        print str(Max) + " " + str(Min)
    
analysDataTo2Clusters(sys.argv[1])
