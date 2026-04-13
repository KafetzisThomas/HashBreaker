#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: HashBreaker (https://github.com/KafetzisThomas/HashBreaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import sys
import time
import colorama
from colorama import Fore as F, Back as B
from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash
from Scripts.hash_algorithms.sha_hash import crack_sha_hash

# Initialize colorama for colored output
colorama.init(autoreset=True)

# Dictionary mapping hash algorithm names to their respective functions
hash_algorithms = ["bcrypt", "md5", "sha1", "sha224", "sha256", "sha384", "sha512"]


def commandline_args():
    """Handle command-line arguments to crack hashes."""
    hash_algorithm = sys.argv[1]
    hash_str = sys.argv[2]
    wordlist = None
    with_wordlist = False
    custom_charset = None
    with_custom_charset = False

    if "--wordlist" in sys.argv:
        wordlist = sys.argv[3]
        with_wordlist = True

    if "--charset" in sys.argv:
        custom_charset = sys.argv[3]
        with_custom_charset = True

    if hash_algorithm in hash_algorithms:
        if hash_algorithm == "bcrypt":
            start_time = time.time()
            plain_text, total_attempts = crack_bcrypt_hash(
                hash_str=hash_str,
                wordlist=wordlist,
                custom_charset=custom_charset,
                with_wordlist=with_wordlist,
                with_custom_charset=with_custom_charset,
            )
            end_time = time.time()
            time_elapsed = end_time - start_time
        else:
            start_time = time.time()
            plain_text, total_attempts = crack_sha_hash(
                hash_type=hash_algorithm,
                hash_str=hash_str,
                wordlist=wordlist,
                custom_charset=custom_charset,
                with_wordlist=with_wordlist,
                with_custom_charset=with_custom_charset,
            )
            end_time = time.time()
            time_elapsed = end_time - start_time

        if plain_text:
            print(
                f"Password found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} {F.RESET}{B.RESET}"
                f"\nTotal attempts: {total_attempts}"
            )
            print(f"Time elapsed: {time_elapsed:.1f}s")
    else:
        print(f"Unsupported hash algorithm: {hash_algorithm}")


if __name__ == "__main__":
    # Check Python version requirement
    if sys.version_info[:2] < (3, 6):
        print(
            "Error Code U-2: This script requires Python 3.6 or higher! You are running {}.{}".format(
                sys.version_info[0], sys.version_info[1]
            )
        )
        sys.exit()

    if 1 < len(sys.argv) < 6:
        try:
            commandline_args()
        except IndexError:
            print(
                "Usage: python3 main.py <hash_algo> '<hash_to_crack>' ['<wordlist_path>' --with-wordlist]"
            )
    else:
        print(
            "Usage: python3 main.py <hash_algo> '<hash_to_crack>' ['<wordlist_path>' --with-wordlist]"
        )
