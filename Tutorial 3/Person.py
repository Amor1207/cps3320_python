class Person:
    def __init__(self):
        self.name = None
        self.height = None
        self.weight = None
        self.age = None

    def input_person_data(self):
        self.name = input("please input your name: ")
        self.age = int(input("please input your age: "))
        self.weight = int(input("please input your weight: "))
        self.height = int(input("please input your height: "))

    def get_person_data(self):
        print("His/Her name is ", self.name)
        print("He/Her is ", self.age, "years old")
        print("His/Her weight is ", self.weight)
        print("His/Her height is ", self.height)


def main():
    person1 = Person()
    person2 = Person()
    person1.input_person_data()
    person2.input_person_data()
    person1.get_person_data()
    person2.get_person_data()


if __name__ == "__main__":
    main()
