## IF expression
1. Print out table of truth for expressions:

```
	x and y
	x or y
	x and not y
	(x or z) and (y or z)
```

For `x, y, z = 0 or 1`

2. How infinite can loop look like?


## Loops and If expression

1. Input some number in to your program and 
check if number is prime.

2. Print out all prime numbers from some
defined range.

3. Run in your program in infinit loop on each step 
of ask for user to input some value. If new value 
is equal to letter 'q' finish your program.

4. Find out sum of all Fibonacci  numbers 
which is less than 4000000.

5. Find out all Pythagorean triple in defined range.

## Function

1. Write fucntion without arguments, which 
prints out hello messsga with you'r name

2. Write function with one string argument. 
Function should print out argument

3. Write function which is calculation square value 
of its argument and return reuslt.

4. Write function calculating 
factorial (n! = 1 * 2 * 3 *...* n) of its argument 

5. Write function calculating 
N-th Fibonacci number. Parametr N should 
be function argument.

5. Write function calculating 
N-th Fibonacci number. Parametr N should 
be function argument (recursive).

6. Write function calulating N-th number of aripmetica progression, 
step of progression sould pass to function as argument (default value of for step should be 1)

```
# to define default argument value
def some_function(arg_without_default_value, arg_with_default_value=1):
   # do some work
   # ...
```

7. Write function to reverese the list 
```
# list could be defined as 
l = [] # empty list
l = [1,2] #ist with two items 1, 2
# to appenda value to list
l.append(3)
l.append(4)
# after that list will be looks like [1,2,3,4]

def revert_list(l):
   # your code which is reverting list l
   # and will return l 

print(revert_list(l))
# will print 4,3,2,1
```
