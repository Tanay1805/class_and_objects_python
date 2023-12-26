class Animal:
    def __init__(self):
        self.pet = []
        self.user_input = str(input("Enter if you want a dog or cat: "))

        if self.user_input == 'dog':
            self.attributes_dog()
        elif self.user_input == 'cat':
            self.attributes_cat()

    def attributes_dog(self):
        breed = input('Enter the breed of the dog: ')
        gender = input('Enter the gender of the dog required: ')
        age = int(input('Enter the age of the dog: '))
        self.pet = [breed, gender, age]

    def attributes_cat(self):
        breed = input('Enter the breed of the cat: ')
        gender = input('Enter the gender of the cat required: ')
        age = int(input('Enter the age of the cat: '))
        self.pet = [breed, gender, age]


class Dog(Animal):
    pass


class Cat(Animal):
    pass

animal_instance = Animal()
print(animal_instance.pet)
