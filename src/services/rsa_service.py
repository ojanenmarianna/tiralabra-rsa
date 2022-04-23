import math
import random

class RsaService:

    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.eulers_totient = None
        self.exponent = None
   
    def generate_keys(self):
        p, q = self.generate_prime_numbers()
        modulus = p*q
        lambdan = self.compute_lambdan(p - 1, q - 1)
        self.eulers_totient = (p-1)*(q-1)

        self.exponent = self.gcd(modulus, self.eulers_totient)
        d = self.mult_inv()
        self.public_key = (modulus, self.exponent)
        self.private_key = (d, lambdan)
        print(self.public_key)
        print(self.private_key)

    def compute_lambdan(self, p, q):
        """
        Laskee Carmichaelin funktion arvolla p * q.
        """
        return abs(p*q) // math.gcd(p, q)

    def primes_in_range(self, x, y):
        """
        Luo listan alkuluvuista, jotka ovat välillä x, y.
        """
        prime_list = []
        for n in range(x, y+1):
            #is_prime = True
            for num in range(2, n):
                if n % num == 0:
                    break
            else:
                prime_list.append(n)

        return prime_list

    def generate_prime_numbers(self):
        """Luo alkuluvut p ja q niin, että p != q.
        
        Returns:
            Tuple, joka sisältää alkuluvut.
        """
        prime_list = self.primes_in_range(2, 100)
        print(prime_list)
        p = random.choice(prime_list)
        while True:
            q = random.choice(prime_list)
            if q == p:
                continue
            else:
                break
    
        return (p, q)


    def miller_rabin(self):
        pass

    #GCD
    def gcd(self, exponent, eulers_toitent):
        while(eulers_toitent!=0):
            exponent,eulers_toitent=eulers_toitent,exponent%eulers_toitent
        return exponent

    #Extended Euclidean Algorithm
    def eea(self, a,b):
        if(a%b==0):
            return(b,0,1)

        gcd,s,t = self.eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)

    #Multiplicative Inverse
    def mult_inv(self):
        gcd,s,_= self.eea(self.exponent,self.eulers_totient)
        if(gcd!=1):
            return None

        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%self.r))
        elif(s>0):
            print("s=%d."%(s))
        return s%self.eulers_totient
