def gen_123():
    yield 1
    yield 2
    yield 3


g = gen_123()
for i in g:
    print(i)
