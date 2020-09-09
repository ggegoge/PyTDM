sub10 = {
	0: "serraw",
	1: "yeah denn",
	2: "dvah",
	3: "tshi",
	4: "chtehrri",
	5: "pienntch",
	6: "sheshtch",
	7: "shehdehm",
	8: "oshehm",
	9: "jevvienntch"
}

teen = {
	10: "jehshienntch",
	11: "yeah dennashtch yeah",
	12: "dvahnashtch yeah",
	13: "tshinashtch yeah",
	14: "chternashtch yeah",
	15: "piehttnashtch yeah",
	16: "shessnashtch yeah",
	17: "shehdehmnashtch yeah",
	18: "oshehmnashtch yeah",
	19: "jevvienntnashtch yeah"
}

dec = {
	20: "dvahjehshtchiah",
	30: "tshijehshtchee",
	40: "chterjehshtchee",
	50: "piennjehshawnt",
	60: "sheshjehshawnt",
	70: "shehdehmjehshawnt",
	80: "oshehmjehshawnt",
	90: "jevviehnjehshawnt",
	100: "staw"
}


def num_to_speech(n):
	if n < 0:
		return "meenoos " + num_to_speech(-n)
	if n < 10:
		return sub10[n]
	elif n >= 10 and n < 20:
		return teen[n]
	elif n <= 100:
		if n % 10 == 0:
			return dec[n]
		else:					
			return dec[n - (n % 10)] + " " + sub10[n%10]
	else:
		return dec[100] + num_to_speech(n%100)
	
