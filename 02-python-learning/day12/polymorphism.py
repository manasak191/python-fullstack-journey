class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Same method, different output!

# Output:
# Woof!
# Meow!