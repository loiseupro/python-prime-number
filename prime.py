def isPrime(num):
	cont = 0
	i = 1

	for i in range(0, num):
		i+=1
		if (num%i == 0):
			cont+=1;

	if cont == 2:
		return True
	
	return False
