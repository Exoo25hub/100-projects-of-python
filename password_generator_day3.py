import random

length = int(input("Password length: "))  # Convert input to an integer

all_chars = (
	"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
)

password = ""
for i in range(length):
	password += random.choice(all_chars)
print(password)
