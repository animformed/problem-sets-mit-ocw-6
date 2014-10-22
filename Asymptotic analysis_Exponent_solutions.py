#The expression O(g), for some function g(n), represents a set of functions, and a function
#f (n) is such that, for n > 0:
#f(n) ≤ cg(n)
#
#O(g) is the set of functions that do not grow faster than g. Eg, n and 2.4n^2 + 7 belong to the 
#set of O(n^2).
#
#Ω is its complete opposite: a function f is in Ω(g) if it satisfies the following condition:
#f (n) ≥ cg(n)
#
#So, where O forms a so-called asymptotic upper bound, Ω forms an asymptotic lower bound.
#
#Our first two asymptotic operators, O and Ω, are each others’ inverses: if f is O(g), then g is Ω(f).
#
#The sets formed by Θ are simply intersections of the other two, that is, Θ(g) = O(g) ∩ Ω(g). In other
#words, a function f is in Θ(g) if it satisfies the following condition:
#c1g(n) ≤ f (n) ≤ c2g(n)
#
#This means that f and g have the same asymptotic growth. For example, 3n2 + 2 is Θ(n2), but we could 
#just as well write that n2 is Θ(3n2 + 2). By supplying an upper bound and a lower bound at the
#same time, the Θ operator is the most informative of the three.
#See link:
#http://fooplot.com/index.php?&type0=0&type1=0&type2=0&type3=0&type4=0&y0=%282.4*x%5E2%29%2B7&y1=x%5E2&y2=%283*x%5E2%29%2B2&y3=&y4=&r0=&r1=&r2=&r3=&r4=&px0=&px1=&px2=&px3=&px4=&py0=&py1=&py2=&py3=&py4=&smin0=0&smin1=0&smin2=0&smin3=0&smin4=0&smax0=2pi&smax1=2pi&smax2=2pi&smax3=2pi&smax4=2pi&thetamin0=0&thetamin1=0&thetamin2=0&thetamin3=0&thetamin4=0&thetamax0=2pi&thetamax1=2pi&thetamax2=2pi&thetamax3=2pi&thetamax4=2pi&ipw=0&ixmin=-5&ixmax=5&iymin=-3&iymax=3&igx=10&igy=10&igl=1&igs=0&iax=1&ila=1&xmin=-38.58841740812352&xmax=41.666417187175426&ymin=-5.214597275440731&ymax=38.14997068518734

def exp1(a, b):             # linear complexity
    ans = 1
    while(b > 0):
        ans *= a
        b -= 1
    return ans
#order is 2 + 3b, so it grows O(n). 3 while steps times b and 2 steps, ans = 1 and return a
def exp2(a, b):             # linear complexity
    if b == 1:
        return a
    else:
        return a * exp2(a, b-1)
#Recursive exponentiater, 
#t(b) = number of steps required to solve the problem size b
#Here, one test, multiplication and subtraction; that's three steps, plus whatever steps it takes
#to solve the problem size (b-1), called recurrence relation. So to write the expression for (b-1),
#t(b) = 3 + t(b-1)
#t(b) = 3 + 3 + t(b-2)
#     = 3k + t(b-k)    # in general
#when done , b-k =1, k = b-1, when in the base case
#     = 3(b-1) + t(1)
#     = 3(b-1) + 2
#     = 3b - 1
#     Therefore order is 3b-1, grows O(n) 


def exp3(a, b):             # logarithmic complexity
    if b == 1:
        return a
    if b % 2 == 0:
        return exp3(a*a, b/2)
    else:
        return a * exp3(a, b-1)
    
#Here, if b is even,
#a ** b = (a*a) ** (b/2)
#       = a * a**(b-1)   # next step is odd, but b is even in next step, problem is halved again
# t(b)  = 5 + t(b/2)     # when even. b == 1, b % 2, b%2 == 0, a*a and b/2
#       = 5 + t(b-1)     # when odd
#       = 5 + 5 + t((b-1)/2)
#       = 10 + t(b/2)       # in general, after 10 steps
#       = 10 + 10 + t(b/4)
#       = 10 + 10 + 10 + t(b/8)
#       = 10k + t(b/2**k)
#       base case when b/2**k = 1
#       Therefore k = (log2)b, order of O(logb)
       
def exp4(a, b):             # quadratic complexity
    res = 0
    for i in range(a):
        for j in range(b):
            res += 1
    return res

#order is a * b
#if a = b, order is a**2, order is O(n**2)

    

     
        
    