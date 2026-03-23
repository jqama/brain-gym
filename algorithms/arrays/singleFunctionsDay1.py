##1
#You are given a two-digit integer n. Return the sum of its digits.

def sum_of_digits (n):
    total=0
    n=abs(n)
    while n>0:
        total +=n%10
        n //= 10
    return total

def sum_of_digits_string(n):
    return sum(int(d) for d in str(abs(n)))

sum_of_digits_singleLine = lambda n : sum(map(int,str(abs(n))))

#print(sum_of_digits(1239))
#print(sum_of_digits_string(1239))
print(sum_of_digits_singleLine(1239))
