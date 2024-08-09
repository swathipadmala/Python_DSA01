def hash_function(key):
    hash = 0
    for char in key:
        hash = hash+ord(char)
    return hash % 10
value = hash_function("swathi")
value2 = hash_function("sandi")
print(value)
print(value2)

