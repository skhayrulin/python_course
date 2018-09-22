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
# to define default argument value so called named argumnets
def some_function(arg_without_default_value, arg_with_default_value=1):
   # do some work
   # ...

# you can use it than
some_function(12, 13) # it will run function some_function 
		      # with arg_without_default_value=12, arg_with_default_value=13

# or
some_function(12) # it will run function some_function
		  # with arg_without_default_value=12, arg_with_default_value=1

# or
some_function(12, arg_with_default_value=7) # it will run function some_function
		  # with arg_without_default_value=12, arg_with_default_value=7


# order of arguments is important! First should be defined arguments withour default value! 


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

## List, slice tuples, generator, string

1. Crete list of numbers from 0 to 100 (by loop and by list comprehension)
2. Crete list of squares of previous list (by loop and by list comprehension)
3. Crete list of odd elements of previous list (by loop and by list comprehension)
4. We have a string: 'rewlkdfsklgjdflkjglkdsfjgkldfsjglkjeroitewuiotujdigjsdfklg;klsdfgkl;jsdfkl;gjldk;sfjgjlk;sdfjlk;gjsdfl;kgl;kdsfjgl;kjsdfl;kgjl;sdfkjg;lkjsdflbvjdfslkglkrewjhtiowerjutioerutopiytuilyhjdsfl;kghjl;sdkf;gjdffffffffflkgjlkdfjglkasjdfoitweigheripjgierglisjdfkjlghsdfkj;l;hgkljasdhfglk;hsdfkjlghlk;sdfhg;kljsdflkgjlk;sdfjgl;ksdfjl;kgjsdfl;kjglk;sdfjgkjsdfl;kgjs;dlkfjgoiw3eujtio34wuytiergoijherjhlgjsdflkjgkl;dfjgkl;sdfjkl;gjsdf;lkjg;lsjeriotuerl;kjdsfkl;jgh;lksdfjg;lksdfjg;lksdfkjg;lkjreopyulidsjfl;kghjs;ldkjg;lkkjr5l;h;kljyhkl;rirtiririiiiiiiiiiiiiierwtsj;kldfjg;lksdfjgl;ksdjfl;gj;lsdfjg;lk' - remove from it's all repated chars print string with unique chars
5. What sub sequance of repeated letters is longest?
6. Write function which deleting some defined letter from string test it on prev. string
7. We have list of some integer numbers - 2,3,3,45,4,23,43,54,34,5,32,423,4,23542354,3422,243,4,3,3,254,5643,3233,3,3,4,43,2,423,3,3,45,5,43,2,1,4,34234,34,3,342,23,4543,534,32423,23,4,4,4,3,423,3245,23,3,34254,235,234,5,235,4,345,235,23,5523,5,234,52,67,756,76,57,345,23,31,7,8,56,346,345,756,4343,754,674,8,568,9,65,34,3,5474,5687,56,2,3 - calc summ of this numbers
8. Find out max/min elements of prev. list
9. Sort list by buuble sort (write by yours)
10. Write programm which is asking user to how many Fibonacci numbers it should generate and than generate it.
11. Write function which is generating matrix as list of list (by loop and generator)
12. Write fuction for transposing matrix
13. Write fuction for summing of matrix
14. Write fuction for multipliyng of matrix
15. Write function for resolve of System of linear equations by [Gauss method](https://en.wikipedia.org/wiki/Gaussian_elimination).

