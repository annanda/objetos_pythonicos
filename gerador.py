def gen_123():
    yield 1
    yield 2
    yield 3

def gen_novo():
    print('iniciando')
    yield 'a'
    print('continuando')
    yield 'b'
    print('finalizando')

# g = gen_123()
# for i in g:
#     print(i)
