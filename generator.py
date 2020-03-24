def simple_generator(val):
   while val > 0:
       val -= 1
       yield 1    #генератор единиц

gen_iter = simple_generator(5)

print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))

#  print(next(gen_iter))