#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bcrypt
from Scripts.gen_pass import generate_passwords


def crack_bcrypt_hash(
    hash_str,
    wordlist,
    custom_charset,
    password_length=1,
    with_wordlist=False,
    with_custom_charset=False,
):
    total_attempts = 0
    """Find & return a matching password for a given bcrypt hash"""
    if not with_wordlist:
        while True:
            for guess in generate_passwords(
                password_length, custom_charset, with_custom_charset
            ):
                total_attempts += 1
                print(f"{hash_str}: {guess}")
                # Check if the generated password matches the hash
                if bcrypt.checkpw(guess.encode("utf-8"), hash_str.encode("utf-8")):
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
                    if bcrypt.checkpw(
                        line.strip().encode("utf-8"), hash_str.encode("utf-8")
                    ):
                        wordlist_found = True
                        return line.strip(), total_attempts

            if not wordlist_found:
                print(f"No matching password found in {wordlist}")
        except FileNotFoundError:
            print(f"Wordlist file not found: {wordlist}")
