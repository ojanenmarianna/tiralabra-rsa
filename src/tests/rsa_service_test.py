import unittest
import random
import string

from services.rsa_service import RsaService
from services.encryption_decryption_service import EncryptAndDecrypt
from services.prime_service import PrimeService
from services.rsa_key import RsaKey

class TestRsaService(unittest.TestCase):
    def setUp(self):
        self.prime_p = 1000079910000813100008191000083110000849100008671000087110000873
        self.prime_q = 6260585756555452515049484645444240393836353433323028272625242221
        self.not_prime = self.prime_q*self.prime_p
        self.test_service = RsaService(1024, PrimeService, RsaKey)
        self.test_service.generate_keys()
        self.pub_key = self.test_service.pub_key
        self.pvt_key = self.test_service.pvt_key

    def test_compute_lambdan(self):
        self.assertEqual(1565271509992087335897474486663626894536348253905871066930100982678848556060572245437474835499160580751165493921375878352803960, self.test_service.compute_lambdan(self.prime_p, self.prime_q)) # pylint: disable=C0301

    def test_miller_rabin_with_prime(self):
        self.assertEqual(True, self.test_service.miller_rabin(self.prime_q))

    def test_miller_rabin_with_not_prime(self):
        self.assertEqual(False, self.test_service.miller_rabin(self.not_prime))

    def test_trial_devision(self):
        self.assertEqual(True, self.test_service.trial_division(self.prime_p))

    #def test_trial_division_with_not_prime(self):
        #self.assertEqual(False, self.test_service.trial_division(self.not_prime))

    def test_is_prime(self):
        self.assertEqual(True, self.test_service.is_number_prime(self.prime_q))

    def test_is_prime_with_not_prime(self):
        self.assertEqual(False, self.test_service.is_number_prime(self.not_prime))

    def test_generate_keys_generates_keys(self):
        self.assertEqual(True, self.test_service.pub_key is not None)
        self.assertEqual(True, self.test_service.pvt_key is not None)

    def test_rsa_get_modulus_returns_modulus(self):
        self.assertEqual(True, self.test_service.pub_key.get_modulus() is not None)

    def test_rsa_key_get_exponent_returns_exponent(self):
        self.assertEqual(True, self.test_service.pvt_key.get_exponent() is not None)

    def test_encryption_and_decryption(self):
        length = 127
        letters = string.ascii_lowercase

        test_string = ''.join(random.choice(letters) for i in range(length))
        encrypted = EncryptAndDecrypt().encrypt(test_string, self.pub_key)

        self.assertEqual(test_string, EncryptAndDecrypt().decrypt(int(encrypted), length, self.pvt_key)) # pylint: disable=C0301
