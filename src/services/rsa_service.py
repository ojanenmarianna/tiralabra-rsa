import random
import math

class RsaService:

    """
    Luokka vastaa RSA-avainten luomisesta.
    """

    def __init__(self, length, prime_service, rsa_key):
        prime_service = prime_service(1500)
        self.primes_list = prime_service.prime_list
        self.rsa_key = rsa_key
        self.length = length
        self.exponent_e = 65537
        self.pub_key = None
        self.pvt_key = None

    def generate_keys(self):
        """
        Luo ja tallentaa RSA-avainparin.

        Args:
            modulus = käytetään moduulina julkiselle ja yksityiselle avaimelle
            lambdan = compute_lambdan(p-1, q-1)
            exponent_d = yksityisen avaimen eksponentti.
        """

        prime_p, prime_q = self.generate_prime_numbers()
        modulus = prime_p*prime_q
        lambdan = self.compute_lambdan(prime_p, prime_q)
        exponent_d = pow(self.exponent_e, -1, lambdan)
        self.pub_key = self.rsa_key(modulus, self.exponent_e)
        self.pvt_key = self.rsa_key(modulus, exponent_d)

    def generate_prime_numbers(self):
        """
        Luo alkuluvut p ja q, niin että p != q.
        """

        while True:
            prime_p = random.getrandbits(self.length//2)
            if prime_p % 2 == 0:
                continue
            if self.is_number_prime(prime_p):
                break
        while True:
            prime_q = random.getrandbits(self.length//2)
            if prime_q % 2 == 0 or prime_q == prime_p:
                continue
            if self.is_number_prime(prime_q):
                break
        return (prime_p, prime_q)

    def compute_lambdan(self, prime_p, prime_q):
        """
        Laskee Carmichaelin funktion alkuluvuilla p ja q (lambda(n) = lcm(p-1, q-1)).
        """

        return abs((prime_p-1)*(prime_q-1)) // self.gcd(prime_p-1, prime_q-1)

    def gcd(self, num_a, num_b):
        """
        Laskee suurimman yhteisen jakajan a:lle ja p:lle.
        """
        while num_b != 0:
            num_a, num_b = num_b, num_a % num_b

        return num_a

    def is_number_prime(self, possible_prime):
        if not self.trial_division(possible_prime):
            return False
        if not self.miller_rabin(possible_prime):
            return False
        return True

    def trial_division(self, possible_prime):
        """
        Tekee alustavan tarkistuksen alkulukuehdokkaalle jakamalla sitä pienillä alkuluvuilla.

        Args:
            possible_prime = mahdollinen alkuluku
        """
        for prime in self.primes_list:
            if prime >= math.sqrt(possible_prime): 
               return True 
            if possible_prime % prime == 0:
                return False
        return True

    def miller_rabin(self, possible_prime):
        """
        Tekee mahdolliselle alkuluvulle Miller-Rabin alkuluku testin 40 kertaa (optimaalinen määrä).

        Args:
            possible_prime = mahdollinen alkuluku
        """

        num_r, num_s = 0, possible_prime-1
        while num_s % 2 == 0:
            num_r += 1
            num_s = num_s // 2

        for _ in range(40):
            num_a = random.randint(2, possible_prime-2)
            if self.gcd(possible_prime, num_a) != 1:
                return False
            num_x = pow(num_a, num_s, possible_prime)
            if num_x in (1, possible_prime-1):
                continue
            for _ in range(num_r-1):
                num_x = pow(num_x, 2, possible_prime)
                if num_x == possible_prime-1:
                    break
            else:
                return False
        return True
