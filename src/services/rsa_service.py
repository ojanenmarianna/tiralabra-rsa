import math
import random

from prime_service import PrimeService

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

    def generate_prime_numbers(self):
        """Luo alkuluvut p ja q niin, että p != q.
        
        Returns:
            Tuple, joka sisältää alkuluvut.
        """
        prime_list = PrimeService().generate_list(2, 100)
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

    def gcd(self, exponent, eulers_toitent):
        """
        Laskee suurimman yhteisen nimittäjän Eukleideen funktiolla.
        
        Returns: 
            Suurin yhteinen nimittäjä.
        """
        while(eulers_toitent!=0):
            exponent,eulers_toitent = eulers_toitent,exponent%eulers_toitent
        return exponent

    def eea(self, a,b):
        """
        Laajennettu Eukleideen funktio.

        Args:
            a, b: Verrattavat luvut.
        """
        if a%b==0:
            return b,0,1

        gcd,s,t = self.eea(b,a%b)
        s = s-((a//b) * t)
        return gcd,s,t

    def mult_inv(self):
        """
        Laskee purkuavaimen d yksityiselle avaimelle.
        """
        gcd,s,_= self.eea(self.exponent,self.eulers_totient)
        if gcd!=1:
            return None
        else:
            return s%self.eulers_totient
