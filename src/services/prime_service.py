class PrimeService:
    """
    Luokka alkulukujen luomiseen.
    """

    def __init__(self):

        self.prime_list = self.generate_list(from_number, to_number)

    def generate_list(self, from_number, to_number):
        """
        Luo listan alkuluvuista lukuun to_number asti Erastostheneen seulalla.
        """

        primes = [True for i in range(to_number+1)]
        for i in range(from_number, to_number + 1):
            if primes[i]:
                for j in range(i * i, to_number + 1, i):
                    primes[j] = False
    
        prime_list = []
        for i in range(from_number, to_number + 1):
            if primes[i]:
                prime_list.append(i)
    
        return prime_list
    