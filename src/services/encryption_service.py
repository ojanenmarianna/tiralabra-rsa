class Encrypt:
    """
    Luokka salaa viestin.
    """

    def encrypt(self, message, key):
        """
        Salaa viestin.
        """

        in_int = self.string_to_int(message)
        return pow(in_int, key.get_exponent(), key.get_modulus())


    def string_to_int(self, message):
        """
        Muuntaa tekstin ensin tavuiksi ja sitten tavut luvuksi.

        Args:
            message = viesti tavuina
        """

        return int.from_bytes(message.encode(), byteorder='big')
