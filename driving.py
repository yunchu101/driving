country = input('what is you country?')
age = input('what is your age?')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can get a driving license')
	else:
		print('you can not get a license yet')