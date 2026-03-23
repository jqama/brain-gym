# Problem  Name : Single Function

## Source
- Platform : CodeSignal 
- Link : https://app.codesignal.com/practice-question/question/singleFunction?context=otherTypes

---

## Problem Statement
You are given a two-digit integer n. Return the sum of its digits.

---

## Approach
- Get Unit place digit and add recursively till all digits are covered.
- Complexity : Time = O(n) ; Space = O(1)
- Edge cases considered : Negative Number is made positive by taking absolute value

---

## Solution
```java
#1
public static int sumOfDigits_stream(int n){
    return String.valueOf(Maths.abs(n))
        .chars()
        .map(Characters::getNumber)
        .sum();
}
//Time Complexity = O(k)  String creation + stream traversal
// Space Complexity =  O(k) String + stream pipeline overhead

#2
public static int sumOfDigits_core(int n){
    int total =0;
    n = Maths.abs(n);
    while(n>0){
        total += n%10;
        n=n/10;
    }
    return total;
}
//Time Complexity = O(k)  Loop O(k)
//Space Complexity =  O(1) Only few variables are used

#3
public static int sumOfDigits_recursive(int n){
    n= Maths(n);
    if(n<10) return n;
    return (n%10) * sumOfDigits_recursive(n/10);
}
//Time Complexity = O(k)  One recursive call per digit
//Space Complexity =  O(k) Call stack grows with digits

```
```python
# your code here
def sum_of_digits_core(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n%10
        n //= 10
    return total

## TIME COMPLEXITY = O(k)
## SPACE COMPLEXITY = O(1)

def sum_of_digits_string(n):
    return sum(int(d) for d in str(abs(n)))
## TIME COMPLEXITY = O(k) => str(n) takes O(k) ; Iterating over digits takes O(k)
## SPACE COMPLEXITY = O(1) => String representation stores all digits

sum_of_digits_one_liner = lambda n : sum(map(int,str(abs(n))))
## TIME COMPLEXITY = O(k) =>Same as string approach
## SPACE COMPLEXITY = O(k) => String + iterator overhead
```
## Self Note
See Python one line solution 