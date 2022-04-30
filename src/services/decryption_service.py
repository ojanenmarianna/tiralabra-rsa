class Decrypt:
    """
    Luokka purkaa salatun viestin.
    """

    def decrypt(self, message, size, key):
        """
        Purkaa salatun viestin.
        """

        decrypted = pow(message, key.get_exponent(), key.get_modulus())
        in_text = self.int_to_string(decrypted, size)
        return in_text

    def int_to_string(self, message, size):
        """
        Muuntaa luvun tavuiksi ja sitten tavut tekstiksi.

        Args:
            message = viesti tavuina
        """
        message = message.to_bytes(size, byteorder='big')
        return message.decode()
