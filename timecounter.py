import time
from collections import Counter
import re

def timer(func):
	def wrapper_timer(*args):
		start_time = time.perf_counter()
		value = func(*args)
		end_time = time.perf_counter()
		run_time = end_time - start_time
		return run_time
	return wrapper_timer

@timer
def generateDictionnary(text):
	d = dict()
	
	for line in text:
		line = line.strip()
		line = line.lower()
		words = line.split(" ")
		for word in words:
			if word in d:
				d[word] = d[word] + 1
			else:
				d[word] = 1
	for key in list(d.keys()):
    		return (key, d[key])
    		
@timer
def counting(text):
	words = re.findall(r'\w+', open('shakespeare.txt').read().lower())
	count = Counter(words).most_common()
	return count
