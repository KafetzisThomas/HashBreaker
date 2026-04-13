#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import time
import colorama
from colorama import Fore as F, Back as B
from Scripts.crackers import crack_bcrypt, crack_sha

colorama.init(autoreset=True)

hash_algorithms = ["bcrypt", "md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

def main():
    hash_algorithm = sys.argv[1]
    hash_str = sys.argv[2]
    wordlist = None
    with_wordlist = False
    custom_charset = None
    with_custom_charset = False

    if "--wordlist" in sys.argv:
        with_wordlist = True
        wordlist = sys.argv[3]

    if "--charset" in sys.argv:
        with_custom_charset = True
        custom_charset = sys.argv[3]

    if hash_algorithm in hash_algorithms:
        if hash_algorithm == "bcrypt":
            start_time = time.time()
            plain_text, total_attempts = crack_bcrypt(hash_str, wordlist, custom_charset, with_wordlist, with_custom_charset)
            time_elapsed = time.time() - start_time
        else:
            start_time = time.time()
            plain_text, total_attempts = crack_sha(hash_algorithm, hash_str, wordlist, custom_charset, with_wordlist, with_custom_charset)
            time_elapsed = time.time() - start_time

        if plain_text:
            print(f"Password found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} {F.RESET}{B.RESET}")
            print(f"Total attempts: {total_attempts}")
            print(f"Time elapsed: {time_elapsed:.1f}s")
    else:
        print(f"Unsupported hash algorithm: {hash_algorithm}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: uv run python main.py <hash_algo> <hash> [wordlist --wordlist] [charset --charset]")
        sys.exit()

    main()
