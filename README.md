<div align="center">HashBreaker</div>

**What is this?**  
Allows you to crack hashes with or without wordlist.

## Features

- Operates entirely via command line arguments
- Supported hash algorithms: `Bcrypt`, `MD5`, `SHA1`, `SHA224`, `SHA256`, `SHA384`, `SHA512`
- Dictionary support
- Dynamic password generation:  
  - Generate all possible combinations of characters until a match is found
  - Customize the character set

## Usage

```bash
Usage: uv run main.py <hash_algo> '<hash_to_crack>' ['<wordlist_path>' --wordlist]
```

## Examples

Cracking a hash with a wordlist:

```bash
uv run main.py bcrypt '$2b$12$.pdcdWnjEA/2GOvHfEfMkupP/BXSsdJjLs5Sh63E0B/5JG/YeB9cu' 'common_passwords.txt' --wordlist

# Output:
# ...
# Password Found: [ a ]
# Total attempts: 4
# Time elapsed: 3.1s
```

Cracking a hash with dynamic password generation:

```bash
uv run main.py sha256 'e1608f75c5d7813f3d4031cb30bfb786507d98137538ff8e128a6ff74e84e643'

# Output:
# ...
# Password Found: [ tom ]
# Total attempts: 302523
# Time elapsed: 9.3s
```

Using different hash algorithms:

```bash
# cracking a sha512 hash
uv run main.py sha512 'example-sha512' 'example-wordlist' --wordlist

# cracking a sha1 hash
uv run main.py sha1 'example-sha1'

# cracking a md5 hash
uv run main.py md5 'example-md5' 'example-wordlist' --wordlist
```

Customizing the character set for dynamic generation:

```bash
uv run main.py sha256 'example-hash' 'atcdIQRsoTpUVZ01m5678' --charset

# Output:
# ...
# Password Found: [ pass1 ]
# Total attempts: 2152264
# Time elapsed: 67.6s
```

Handling errors and understanding the output:

```bash
# incorrect hash algorithm
uv run main.py md4 'example-hash'

# Output:
# Unsupported hash algorithm: md4
```

```bash
# invalid wordlist path
uv run main.py md5 'example-hash' 'invalid_wordlist.txt' --wordlist

# Output:
# Wordlist file not found: invalid_wordlist.txt
```

## Run Tests

```bash
uv run -m unittest discover tests
```

## Disclaimer

**HashBreaker** is designed for **educational purposes** and authorized testing only.
You must only use this tool on systems and files you own or have explicit permission to test.
The authors are **NOT** responsible for any misuse, damage, or legal consequences resulting from this tool.
