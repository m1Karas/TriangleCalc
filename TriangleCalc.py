import math

print('Triangle Dimenssion Calculator:')
print('Put a 0 in the field you are looking for')
opp = float(input('Input the opposite:'))
adj = float(input('Input the adjacent:'))
hyp = float(input('Input the hypontious:'))

if hyp == 0: 
    hypB = math.sqrt(pow(opp,2) + pow(adj,2))
    print('\nThe hypotinous is %0.2f' %hypB)

elif opp == 0: 
    oppB = math.sqrt(pow(hyp,2) - pow(adj,2))
    print('\nThe opposite is %0.2f' %oppB)

elif adj == 0: 
    adjB = math.sqrt(pow(hyp,2) - pow(opp,2))
    print('\nThe adjacent is %0.2f' %adjB)

else :
    print('Why?')
