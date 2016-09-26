import math

def answer(area):

    ret = []
    while area > 0:
        x = int(math.sqrt(area))
        area -= x*x
        ret.append(x*x)
    return ret


print('Inputs\n area = 12')
print(answer(12))

print('Inputs\n area = 256')
print(answer(256))

print('Inputs\n area = 15324')
print(answer(15324))

