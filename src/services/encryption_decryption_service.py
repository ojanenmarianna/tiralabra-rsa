# pylint: disable=no-self-use
class EncryptAndDecrypt:
    """
    Luokka salaa ja purkaa viestin.
    """

    def encrypt(self, message, key):
        """
        Salaa viestin.
        """
        in_int = int.from_bytes(message.encode(), byteorder='big')
        return pow(in_int, key.get_exponent(), key.get_modulus())

    def decrypt(self, message, size, key):
        """
        Purkaa salatun viestin.
        """

        decrypted = pow(message, key.get_exponent(), key.get_modulus())
        message = decrypted.to_bytes(size, byteorder='big')
        in_text = message.decode()
        return in_text
