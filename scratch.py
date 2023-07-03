string_one = "aaaaaabbbcccccddbbbbb"
next_str = "this one is the next one"


def generate_hash_map(string):
    hash_map = {}
    for char in string:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    return hash_map

hash_map_one = generate_hash_map(string_one)
hash_map_two = generate_hash_map(next_str)

print(hash_map_one)
print(hash_map_two)