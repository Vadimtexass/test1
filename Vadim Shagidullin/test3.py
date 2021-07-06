
# Class & methods
class Person:

    def print_info(self):
        print(f"{self.name}, {self.surname}, {self.place_of_birth}")

    def get_age(self, current_year):
        print(f"Age: {current_year - self.year_of_birth}")

    def position(self):
        print(f"{self.work_place}")


p1 = Person()
p1.name = "Elon"
p1.surname = "Musk"
p1.place_of_birth = "SAR"
p1.year_of_birth = 1971
p1.work_place = "SpaceX"

p2 = Person()
p2.name = "Sergei"
p2.surname = "Korolev"
p2.place_of_birth = "Russia"
p2.year_of_birth = 1907
p2.work_place = "USSR"

p1.print_info()
p2.print_info()

p1.get_age(2021)
p2.get_age(2021)

p1.position()
p2.position()