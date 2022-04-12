class MyFirstClass:
    pass

my_first_python_object = MyFirstClass()

class Dog:
    legs_no = 4

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{type(self)} - {self.name}'

    def change_name(self, name):
        self.name = name

    @staticmethod
    def speak():
        print('ham ham')


my_dog = Dog('Rex')
print(my_dog)

my_dog.speak()
my_dog.change_name('Pufi')
print(my_dog)
Dog.speak()
print(my_dog.legs_no)
