def gcd(num1,num2):	
	my_list1 = []
	for num in range(1,num1+1):
		if num1%num == 0:
			my_list1.append(num)
	print("Factors of " ,num1 ,my_list1)

	my_list2 = []
	for num in range(1,num2+1):
		if num2%num == 0:
			my_list2.append(num)
	print("Factors of " ,num2 ,my_list2)	

	cf = []
	for c in my_list1:
		if c in my_list2:
			cf.append(c)
	print(cf[-1])



def gcd_adv(m,n):
	
	for i in range(1,min(m,n)+1):
		if (m%i)==0 and (n%i) == 0:
			cf=i
	print(cf)
			
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
gcd(a,b)
gcd_adv(a,b)