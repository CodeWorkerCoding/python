print ("hello world");
print('The quick brown fox', 'jumps over', 'the lazy dog');


# name = input('please enter your name:');
# print("hello ", name);

# print(10*PI);


def recursion(n):
	if n==1:
		return 1
	elif n > 1:
		n += recursion(n-1)
		pass
	return n

number = recursion(10)
print(number)


def muliParamter(a, b):
	return a;
	pass

print(muliParamter(1,3))
print(muliParamter(4, 4))

