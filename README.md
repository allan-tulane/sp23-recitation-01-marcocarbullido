# CMPS 2200  Recitation 01

**Name (Team Member 1):**Marco Carbullido

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment. 
- Click on your personal github repository for the assignment.
- Login in Repls https://replit.com/repls and then create a new replit by importing from github repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.
- Make sure the dependencies are installed. Please use 'pip install -r requirements.txt'.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**The worst case input value for both linear_search and binary_search would be when the given key does not exist in the list. This would result in the entire list being searched for linear search and for binary search the list would be divided until the key is not found at all.**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**The best case scenario for linear_search would be where the key is found at the first index of the list. For binary_search, it would be that the key is found at the middle index of the list (the first index to be checked).**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**/Users/marcocarbullido/PycharmProjects/sp23-recitation-01-marcocarbullido/venv/bin/python /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/_jb_pytest_runner.py --target test_main.py::test_compare_search 
Testing started at 7:23 PM ...
Launching pytest with arguments test_main.py::test_compare_search in /Users/marcocarbullido/PycharmProjects/sp23-recitation-01-marcocarbullido

============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-5.0.0, py-1.11.0, pluggy-0.13.1 -- /Users/marcocarbullido/PycharmProjects/sp23-recitation-01-marcocarbullido/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/marcocarbullido/PycharmProjects/sp23-recitation-01-marcocarbullido
collecting ... collected 1 item

test_main.py::test_compare_search PASSED                                 [100%][[10, 0.00095367431640625, 0.0019073486328125], [100, 0.0021457672119140625, 0.00095367431640625]]


=========================== 1 passed in 0.45 seconds ===========================

Process finished with exit code 0**

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**Yes. The theoretical and empirical Big-O runtime is consistent as can be seen in the results above. This is due to the implementation of the algorithms.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **This would be O(kn^2)**
  + For binary search? **O(klog2n)**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **When the list is small, it is usually faster to search through the list without sorting it -- the time it takes to sort the list is more than the time saved by using binary search. However, as the list gets larger, the advantage of sorting the list and using binary search becomes more significant.**
