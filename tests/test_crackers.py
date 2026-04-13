import os
import unittest
from unittest.mock import patch
from Scripts.crackers import crack_bcrypt, crack_sha


class TestHashCrackers(unittest.TestCase):
    def setUp(self):
        self.patcher = patch("builtins.print")
        self.mock_print = self.patcher.start()
        self.current_directory = os.getcwd()
        self.wordlist = f"{self.current_directory}/tests/example_wordlist.txt"
        self.password_length = 1
        self.expected_result = "a"

        # test hashes
        self.bcrypt_hash = "$2b$12$.pdcdWnjEA/2GOvHfEfMkupP/BXSsdJjLs5Sh63E0B/5JG/YeB9cu"
        self.md5_hash = "0cc175b9c0f1b6a831c399e269772661"
        self.sha1_hash = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"
        self.sha224_hash = "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5"
        self.sha256_hash = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
        self.sha384_hash = "54a59b9f22b0b80880d8427e548b7c23abd873486e1f035dce9cd697e85175033caa88e6d57bc35efae0b5afd3145f31"
        self.sha512_hash = "1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75"

    # -- bcrypt ---

    def test_bcrypt_hash_with_wordlist(self):
        result, _ = crack_bcrypt(self.bcrypt_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_bcrypt_hash_without_wordlist(self):
        result, _ = crack_bcrypt(self.bcrypt_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- md5 ---

    def test_md5_hash_with_wordlist(self):
        result, _ = crack_sha("md5", self.md5_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_md5_hash_without_wordlist(self):
        result, _ = crack_sha("md5", self.md5_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- sha1 ---

    def test_sha1_hash_with_wordlist(self):
        result, _ = crack_sha("sha1", self.sha1_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_sha1_hash_without_wordlist(self):
        result, _ = crack_sha("sha1", self.sha1_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- sha224 ---

    def test_sha224_hash_with_wordlist(self):
        result, _ = crack_sha("sha224", self.sha224_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_sha224_hash_without_wordlist(self):
        result, _ = crack_sha("sha224", self.sha224_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- sha256 ---

    def test_sha256_hash_with_wordlist(self):
        result, _ = crack_sha("sha256", self.sha256_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_sha256_hash_without_wordlist(self):
        result, _ = crack_sha("sha256", self.sha256_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- sha384 ---

    def test_sha384_hash_with_wordlist(self):
        result, _ = crack_sha("sha384", self.sha384_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_sha384_hash_without_wordlist(self):
        result, _ = crack_sha("sha384", self.sha384_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    # --- sha512 ---

    def test_sha512_hash_with_wordlist(self):
        result, _ = crack_sha("sha512", self.sha512_hash, self.wordlist, self.password_length, True)
        self.assertEqual(result, self.expected_result)

    def test_sha512_hash_without_wordlist(self):
        result, _ = crack_sha("sha512", self.sha512_hash, None, self.password_length, False)
        self.assertEqual(result, self.expected_result)

    def tearDown(self):
        self.patcher.stop()

if __name__ == "__main__":
    unittest.main()
