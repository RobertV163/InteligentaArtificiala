type('Hello romania')
name='Vadim Tudor'
namee='erisei'
print(name[2])
print(name[:])
print('Hello romania'[2])
print(name[2:])
print(name[-5])
print(name[::1])
print(name[::-1])
print(namee[::-1])
print(name[0:10:2])
print('ola'+'_'+'amigo')
print('$'*22)

print('a doa parte')

print(len('vamos'))
print('  aloha  '.strip())
print('aloha'.strip('a'))
print('si faci uaii'.split())
print('sti unde ma gasesti?'.replace('sti','pe'))
print('ACAS CU TINE'.lower())

print()
print('ex string formating')
print()

name1='Vasile'
name2='Grigore'
print(f'unde e {name1} si {name2}?')
print('unde e {} si {}?'.format(name1,name2))
print('unde e %s si %s ?'%(name1,name2))

print()
print('ex palindrome check')
print()

cuvant='reviver'
p = bool(cuvant.find(cuvant[::-1]) + 1)
print(p)


print()
print('ex boolean')
print()

print(5==5)
print(5==999)

print()
print('ex list')
print()

listamea=[1, 2, '3', True, 2]
print(len(listamea))
print(listamea.index('3'))
print(listamea.count(2))
print(listamea[3])
print(listamea[1:])
print(listamea[:2])
print(listamea[0:4:3])








