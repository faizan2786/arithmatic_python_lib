## FP ARITHMATIC LIBRARY (*version = 1.0.1*)
This is my *first* python library to test and publish python package on PyPI.  
It includes arithmatic functions as follows:
- add -> adds two numbers
- mul -> multiplies two numbers
- sqrt -> computes sqrt of given number
- dot -> returns dot (inner) product of two vectors (lists)
- distance -> computes Euclidean distance between two vectors

### INSTALLATION
```
pip install fp-arithmatic
```

### GET STARTED
How to take dot products of two vectors using this library

```python
import fp_arithmatic as fpa
x = [1,2,3]
y = [2, 3, 5]
result = fpa.dot(x,y)
print(result)

x = [1, 3]
y = [4, 7]
dist = fpa.distance(x,y) # returns 5
```

### Testing
In order to test the library, I have provided 8 test cases using python's built-in *unittest* module in the **tests** folder. Run below command in the root directory to run the test cases.
```
python3 -m unitest tests/arithmatic_tests.py
```
