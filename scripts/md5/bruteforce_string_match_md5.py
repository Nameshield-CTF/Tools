import hashlib
import random
import string
import sys


# This script finds a string which hash start the specified argument
# High CPU load

def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


target = sys.argv[1]
found = False
while not found:
    mystring = random_string()
    md5gen = hashlib.md5(str.encode(mystring)).hexdigest()
    if target == md5gen[:len(target)]:
        print("FOUND : " + str(mystring) + " - HASH : " + md5gen)
        found = True
