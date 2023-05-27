"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if left > right:
		return -1
	mid = (left + right) // 2
	if mylist[mid] == key:
		return mid
	elif key < mylist[mid]:
		return _binary_search(mylist, key, left, mid - 1)
	else:
		return _binary_search(mylist, key, mid + 1, right)

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1, 2, 3, 4, 5], 8) == -1
	assert binary_search([1, 2, 3, 4, 5], 3) == 2

def time_search(search_fn, mylist, key):
  start_time=time.time()
  result = search_fn(mylist, key)
  elapsed_seconds = time.time()-start_time
  elapsed_miliseconds = 1000 * elapsed_seconds
  return elapsed_miliseconds

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  comparison = []
  for n in sizes:
    lst = list(range(0, n-1))
    linear_search_time = time_search(linear_search, lst, -1)
    binary_search_time = time_search(binary_search, lst, -1)
    result = [n, linear_search_time, binary_search_time]
    comparison.append(result)
  return comparison

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
