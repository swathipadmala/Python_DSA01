hash_table = [[]]*10
def hash_function(key):
    hash = 0
    for char in key:
        hash = hash+ord(char)
    return hash % 10
def insert_data(key,data):
    h = hash_function(key)
    hash_table[h] = data
def get_data(key):
    h = hash_function(key)
    return hash_table[h] 
insert_data('123',"flower")
insert_data("234","fruits")
insert_data("567","animals")

result = get_data("567")
print(result)