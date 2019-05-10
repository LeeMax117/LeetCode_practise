# Description:

>Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

> Example 1:

> Input:
> s = "aaabb", k = 3

> Output:
> 3

> The longest substring is "aaa", as 'a' is repeated 3 times.
> Example 2:

> Input:
> s = "ababbc", k = 2

> Output:
> 5

> The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# Solutions:
- look up all the letters number and create a dict to record them and their position in the string

- find all the letter dict that num less than given k

- use them to seperate the original string and calculate the max of seperated string
