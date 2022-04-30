# pylint: disable=invalid-name
import random
import math


class RsaService:

    """
    Luokka vastaa RSA-avainten luomisesta.
    """

    def __init__(self, length, prime_service, rsa_key):
        """
        Luokan konstruktori.

        Args:
            exponent_e = julkisen avaimen eksponentti, valittu suoraan yleisimmin käytetty arvo
        """

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
            lambdan = lcm(p-1, q-1)
            exponent_d = yksityisen avaimen eksponentti.
        """

        prime_p, prime_q = self.generate_prime_numbers()
        modulus = prime_p*prime_q
        lambdan = self.compute_lambdan(prime_p, prime_q)
        exponent_d = pow(self.exponent_e, -1, lambdan)
        self.pub_key = self.rsa_key(modulus, self.exponent_e)
        self.pvt_key = self.rsa_key(modulus, exponent_d)

    def generate_number(self, length):
        """
        Luo n-bittiä pitkän satunnaisen luvun, jolla alkuluku generoidaan.
        """

        return random.getrandbits(length)


    def generate_prime_numbers(self):
        """
        Luo alkuluvut p ja q, niin että p != q.
        """

        while True:
            prime_p = self.generate_number(self.length//2)
            if prime_p % 2 == 0:
                continue
            if self.is_prime(prime_p):
                break
        while True:
            prime_q = self.generate_number(self.length//2)
            if prime_q % 2 == 0 or prime_q == prime_p:
                continue
            if self.is_prime(prime_q):
                break
        return (prime_p, prime_q)

    def compute_lambdan(self, prime_p, prime_q):
        """
        Lasketaan Carmichaelin funktio arvolla p*q (lambda(n) = lcm(p-1, q-1)).
        """

        return abs((prime_p-1)*(prime_q-1)) // math.gcd(prime_p-1, prime_q-1)

    def is_prime(self, possible_prime):
        """
        Tarkistaa onko luku alkuluku.
        """

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

        r, s = 0, possible_prime-1
        while s % 2 == 0:
            r += 1
            s = s // 2

        for _ in range(40):
            a = random.randint(2, possible_prime-2)
            if math.gcd(possible_prime, a) != 1:
                return False
            x = pow(a, s, possible_prime)
            if x == 1 or x == possible_prime-1:
                continue
            for _ in range(r-1):
                x = pow(x, 2, possible_prime)
                if x == possible_prime-1:
                    break
            else:
                return False
        return True
