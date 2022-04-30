import unittest

from services.rsa_service import *
from services.prime_service import PrimeService
from services.rsa_key import RsaKey

class TestRsaService(unittest.TestCase):
    def setUp(self):
        self.p = 23
        self.q = 59
        self.not_prime = 8
        self.test_service = RsaService(1024, PrimeService, RsaKey)
        self.test_service.generate_keys()

    def test_compute_lambdan(self):
        self.assertEqual(638, self.test_service.compute_lambdan(self.p, self.q))

    def test_miller_rabin_with_prime(self):
        self.assertEqual(True, self.test_service.miller_rabin(self.q))

    def test_miller_rabin_with_not_prime(self):
        self.assertEqual(False, self.test_service.miller_rabin(self.not_prime))

    def test_trial_devision(self):
        self.assertEqual(True, self.test_service.trial_division(self.p))

    def test_trial_division_with_not_prime(self):
        self.assertEqual(False, self.test_service.trial_division(self.not_prime))

    def test_is_prime(self):
        self.assertEqual(True, self.test_service.is_prime(self.q))

    def test_is_prime_with_not_prime(self):
        self.assertEqual(False, self.test_service.is_prime(self.not_prime))

    def test_generate_keys_generates_keys(self):
        self.assertEqual(True, self.test_service.pub_key is not None)
        self.assertEqual(True, self.test_service.pvt_key is not None)

    def test_rsa_get_modulus_returns_modulus(self):
        self.assertEqual(True, self.test_service.pub_key.get_modulus() is not None)

    def test_rsa_key_get_exponent_returns_exponent(self):
        self.assertEqual(True, self.test_service.pvt_key.get_exponent() is not None)
