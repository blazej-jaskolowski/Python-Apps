import hashlib

# Get input from user
word = input("Enter a word to hash: ")

print("\nGenerating different hash values:")

# Calculate different hash types
md5 = hashlib.md5(word.encode()).hexdigest()
sha1 = hashlib.sha1(word.encode()).hexdigest()
sha256 = hashlib.sha256(word.encode()).hexdigest()

print(f"\nOriginal word: {word}")
print(f"MD5: {md5}")
print(f"SHA1: {sha1}")
print(f"SHA256: {sha256}")
