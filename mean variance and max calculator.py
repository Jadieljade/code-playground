import numpy as np


def calculate(list):
    try:
        array = np.array(list)
        array.shape = (3, 3)

        m1 = array.mean(axis=0)
        m2 = array.mean(axis=1)
        m3 = array.mean()

        var1 = array.var(axis=0)
        var2 = array.var(axis=1)
        var3 = array.var()

        max1 = array.max(axis=0)
        max2 = array.max(axis=1)
        max3 = array.max()

        min1 = array.min(axis=0)
        min2 = array.min(axis=1)
        min3 = array.min()

        sum1 = array.sum(axis=0)
        sum2 = array.sum(axis=1)
        sum3 = array.sum()

        std1 = array.std(axis=0)
        std2 = array.std(axis=1)
        std3 = array.std()

        calculations = {}
        calculations['mean'] = [m1, m2, m3]
        calculations['variance'] = [var1, var2, var3]
        calculations['standard deviation'] = [std1, std2, std3]
        calculations['max'] = [max1, max2, max3]
        calculations['min'] = [min1, min2, min3]
        calculations['sum'] = [sum1, sum2, sum3]
    except ValueError:
        print('List must contain nine numbers')


jade = range(0, 9)
