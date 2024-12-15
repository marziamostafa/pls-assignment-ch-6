# Assignment
string = "Marzia Mostafa"
new_string = string   

print("1.Assignment:")
print(f"Original String: {string}")
print(f"Copied String: {new_string}")

# Concatenation
string1 = "Marzia"
string2 = "Mostafa"

c_string=string1+string2
print("\n2.Concatenation:")
print(f"Concatenated String: {c_string}")

joined_string = " ".join([string1, string2])
print(f"Joined String: {joined_string}")


# Substring Reference (Slicing)
substring = string[0:6]
print("\n3.Substring:")
print(f"Substring (from index 0 to 6): {substring}")


# Comparison
string_a = "car"
string_b = "cycle"
string_c = "rickshaw"

print("\n4.Comparison:")
print(f"Is '{string_a}' equal to '{string_b}'? {string_a == string_b}")
print(f"Is '{string_a}' less than '{string_b}'? {string_a < string_b}")
print(f"Is '{string_a}' equal to '{string_c}'? {string_a == string_c}")