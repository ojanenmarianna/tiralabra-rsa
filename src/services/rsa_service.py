#import math
import random

class RsaService:

    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.n = None
        self.r = None
        self.e = None
   
    def generate_keys(self):
        p, q = self.generate_prime_numbers()
        self.n = p*q
        self.r = (p-1)*(q-1)
        self.e = self.egcd(self.e,self.r)
        self.eugcd(self.e, self.r)
        self.mult_inv(self.e, self.r)
        d = self.mult_inv(self.e, self.r)
        self.public_key = (self.e, self.n)
        self.private_key = (d, self.n)

    def primes_in_range(self, x, y):
        prime_list = []
        for n in range(x, y):
            isPrime = True
       
        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)

        return prime_list

    def generate_prime_numbers(self):
        prime_list = self.primes_in_range(0, 100)
        return random.choice(prime_list)


    def miller_rabin(self):
        pass

    #GCD
    def egcd(self, e,r):
        while(r!=0):
            e,r=r,e%r
        return e

    #Euclid's Algorithm
    def eugcd(self, e,r):
        for i in range(1,r):
            while(e!=0):
                a,b=r//e,r%e
                if(b!=0):
                    print("%d = %d*(%d) + %d"%(r,a,e,b))
                self.r=e
                self.e=b

    #Extended Euclidean Algorithm
    def eea(self, a,b):
        if(a%b==0):
            return(b,0,1)

        gcd,s,t = self.eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)

    #Multiplicative Inverse
    def mult_inv(self, eea):
        gcd,s,_=eea(self.e,self.r)
        if(gcd!=1):
            return None

        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%self.r))
        elif(s>0):
            print("s=%d."%(s))
        return s%self.r
