class RsaKey:
    """
    Luokka muodostaa RSA-avain olion.
    """

    def __init__(self, modulus, exponent):
        """
        Luokan konstruktori.
        """

        self.modulus = modulus
        self.exponent = exponent

    def get_modulus(self):
        """
        Palauttaa avaimen moduluksen.
        """

        return self.modulus

    def get_exponent(self):
        """
        Palauttaa avaimen eksponentin.
        """

        return self.exponent
