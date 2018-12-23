#def sum():
english = ['first', 'second', 'third']
#i = 0
#if i < len(english):
n = []
sum = 0
for i in range(len(english)):
    m = (input('please enter the {0} num:'.format(english[i])))
    sum = sum + int(m)
    n.append(str(m))
    #print('please enter the {0} num:{1}'.format(english[i], i))
a = n[0]
    #i += 1
b = n[1] 
    #i += 1
c = n[2]
print('a is {0},b is {1},c is {2},a+b+c={3}'.format(a,b,c,sum))

