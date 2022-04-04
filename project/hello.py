# acesta este un comm pe o linie
print("hello world")
for i in range(2):
    print(f"hello world! {i}")  #ceva


def new_function(a, b):
    """
        aduna 2 numere
    """
    return a + b


l = []

if not l:
    print('lista vida')

print("coco \n"
      """   ceva""")

print(r"ceva\n")

nume = 'popescu'
prenume = 'ion'

body_text = f"""
Buna ziua!
Ma numesc {nume} {prenume}
Bine ati venit pe websiteul nostru"""

print(body_text)

l = [1, 2, 3]
print(l)
l[1] = 0
print(l)

name = 'david'
print(name[1])


l = [1, 3, 3, 4, 5, 6, 7, 8, 9]
print(l)
g = l
l[0] = 'a'
print(l)
print(g)

sliced = l[-2]
print(sliced)

my_tupple = (1, 7, "abc", 18.5)
print(my_tupple)

my_dictionary = {
    "key_1": 12,
    "key_2": 4+5j,
    3: True,
    4: None,
    5 + 2j: '',
    ("key_6", 7): [1, 2, 3]
}

print(my_dictionary)
print(my_dictionary["key_1"])

for key, value in my_dictionary.items():
    print(f'{key} -> {value}')
print(my_dictionary.get(8, 5))

s = {1, 2, 3}
print(set(l))
