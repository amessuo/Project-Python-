
def frame(str):
    l=str.split()
    max=l[0]
    for i in range(1,len(l)):
        if len(l[i])>=len(max):
            max=l[i]
    print('*'*(len(max)+4))
    for j in range(len(l)):
        print('*',l[j],' '*(len(max)-len(l[j]))+'*')
    print('*' * (len(max) + 4))
    print('')

print(frame('hello world in a big frame'))