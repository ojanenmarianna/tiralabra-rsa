class PrimeService:
    """
    Luokka alkulukujen luomiseen.
    """

    def __init__(self, n):

        self.to_number = n
        self.prime_list = self.generate_list(self.to_number)

    def generate_list(self, n):
        """
        Eratostheneen seula pienten alkulukujen luontiin.

        Returns:
            Lista mahdollisista alkuluvuista.
        """
        prime_list = []

        prime = [True for i in range(n+1)]
        for i in range(2, n+1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False

        for i in range(2, n+1):
            if prime[i]:
                prime_list.append(i)
        return prime_list
