#enumerate()
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
#zip()
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
#list comprehension
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
#list comprehension with if
print(even_numbers)

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
#list comprehension with if-else
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
#filter()
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)
#map()
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
#sum()
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50
#lambda functions
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Dictionary Methods
pizza ={
    'name': 'Margherita Pizza', 
    'price': 15, 
    'calories_per_slice': 250, 
    'toppings': ['mozzarella', 'basil'], 
    'total_time': 25
}

#dict()
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

#get()
pizza.get('toppings', []) # ['mozzarella', 'basil']

# keys() and values()
pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])
pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])

#items()
pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

#clear()
pizza.clear()

#pop()
pizza.pop('price', 10)

#popitem()
pizza.popitem()

#update()
pizza.update({ 'price': 15, 'total_time': 25 })
# Example usage of dictionary methods
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)
# Using enumerate to get  product
for product in enumerate(products):
    print(product)
# Set Methods
my_set = {1, 2, 3, 4, 5} 
#add()
my_set.add(6)
#remove() or discard()
my_set.remove(3)  # Raises KeyError if 3 is not found
my_set.discard(10)  # Does not raise an error if 10 is not
#clear()
my_set.clear()
#issubset() and issuperset()
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False
#isdisjoint()
print(my_set.isdisjoint(your_set)) # False
#union()
my_set | your_set # {1, 2, 3, 4, 5, 6}
#intersection()
my_set & your_set # {2, 3, 4}
#difference()
my_set - your_set # {1, 5}
#symmetric_difference()
my_set ^ your_set # {1, 5, 6}

