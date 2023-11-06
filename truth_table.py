n=int(input('no. of variables: '))
exp=str(input('enter boolean expression: '))

exp = exp.replace('&',' and ').replace('*',' and ').replace('!',' not ').replace('|',' or ').replace('+',' or ').replace('  ',' ')

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\n'+'|'.join(list(abc.lower()[:n]))+'|F')
print('-'*(2*n+1))
for i in range(2**n):
    inp=list(format(i, f"0{n}b"))
    expt=exp
    for i in range(n): 
        expt=expt.replace(abc[i],f"({inp[i]})")
    try:
        print('|'.join(inp)+'|'+str(int(eval(expt))))
    except (SyntaxError,TypeError) as e:
        print('|'.join(inp)+'|',e)
input('')
