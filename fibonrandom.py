import random
def testing_random():
	values = [1,3,5,7,9]
	print(random.choices(values))

	random.shuffle(values)
	print(values)

	print(random.randint(1,6)) 
'''testing_random()	'''

def fibo_generator(n):
	if n < 3:
		return 1
	a,b=0,1
	count = 1
	while count < n:
		count += 1
		a,b=b,a+b
	return b

print(fibo_generator(10))		

