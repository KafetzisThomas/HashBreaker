#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
from Scripts.gen_pass import generate_passwords


def crack_sha_hash(
    hash_type,
    hash_str,
    wordlist,
    custom_charset,
    password_length=1,
    with_wordlist=False,
    with_custom_charset=False,
):
    """Find & return a matching password for a given sha type of hash (sha1, sha224, etc.)."""
    hash_func = getattr(hashlib, hash_type)
    total_attempts = 0

    if not with_wordlist:
        while True:
            for guess in generate_passwords(
                password_length, custom_charset, with_custom_charset
            ):
                total_attempts += 1
                print(f"{hash_str}: {guess}")
                if hash_func(guess.encode("utf-8")).hexdigest() == hash_str:
                    return guess, total_attempts
            password_length += 1  # If no match is found, increase the password length
    else:
        total_attempts = 0
        wordlist_found = False
        try:
            with open(wordlist, "r") as file:
                for line in file.readlines():
                    total_attempts += 1
                    print(f"{hash_str}: {guess}")
                    if hash_func(line.strip().encode("utf-8")).hexdigest() == hash_str:
                        wordlist_found = True
                        return line.strip(), total_attempts
            if not wordlist_found:
                print(f"No matching password found in {wordlist}")
        except FileNotFoundError:
            print(f"Wordlist file not found: {wordlist}")
