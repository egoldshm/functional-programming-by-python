def shiftL(num, shift):
	return num[shift:] + shift*"0"
def shiftCL(num, shift):
	return num[shift:] + num[0:shift]
def shiftR(num, shift):
	return shift*"0" + num[0:-shift]
def shiftCR(num, shift):
	return num[0:shift] + num[0:-shift]
