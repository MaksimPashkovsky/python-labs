from heapq import heappush, heappop


def shaker_sort(data):
	up = range(len(data) - 1)
	while True:
		for indexes in (up, reversed(up)):
			print(indexes)
			swapped = False
			for i in indexes:
				print(i)
				if data[i] > data[i + 1]:
					data[i], data[i + 1] = data[i + 1], data[i]
					swapped = True
			print(data)
			if not swapped:
				return data


def insertion_sort(data):
	for i in range(len(data)):
		j = i - 1
		temp = data[i]
		while data[j] > temp and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = temp
	return data


def selection_sort(data):
	for i, e in enumerate(data):
		mn = min(range(i, len(data)), key=data.__getitem__)
		data[i], data[mn] = data[mn], e
	return data


def heap_sort(data):
	h = []
	for value in data:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]


