def max_digits(num):
	sum_digits = 0
	if num:
		sum_digits += num%10
		num = num//10
	return sum_digits

print(max([345, 825, 999, 124], key = max_digits))