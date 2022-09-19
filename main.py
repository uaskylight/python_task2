
# first_name = "Olexsandr"
# last_name = "Tataryntsev"
# full_name = f"{first_name} {last_name}"
# message = (f"Hello, {full_name.title()}!")
# print(message)

# persons = ['alex', 'dima', 'vova']
# print(persons)
# persons.append('maxsim')
# print(persons)
# persons_second = persons
# print(persons)
# persons_second.append('sergey')
# print(persons)

#
# name = input("Enter your name:  ")
# print(name)
# number = int(input('Enter your age:'))
#
# print(number)
# kyiv = input("Enter your namber: ")
# kyiv = int(kyiv)
# if kyiv > 0:
#     print("Heloo")
# elif kyiv <0:
#     print ("Error")
# else:
#     print("zero")
def solve(coordinate):
    if (ord(coordinate [0]))%2 ==  int(coordinate[1])%2:
        return False
    else:
        return True
coordinate = "F5"
print(solve(coordinate))
