"""
Наш клієнт - це рітейлер автомобілів.
Є завод, яикй випускає авто марки Рейні, конвретні моделі види і тд;
декілька салонів, які займаються продажем машин;
машини які продаються кінцевому клієнту;
Власники автомобілів

Фреймворк - архітектура MVC - Model-View-Controller:
За збереження даних відповідає модель
За обробку даних, будь-яку бізнес логіку відповідає контролер
за відображення даних відповідає вю

"""
from framework.menu import Menu

if __name__ == '__main__':
    # first_plant = Plant(1, "Kovel", "Renee", 1)
    # first_plant.save()
    # first_plant = Plant.get_by_id(2)
    # print(first_plant)
    # first_employee = Employee(1, "Liubomyr", "liub@gmail.com", "plant", 1)
    # first_employee.save()
    # print(Employee.get_by_id(1))
    # print(Plant.get_by_id(1))
    # while True:
    #     print(
    #         "Choose a menu item by number: \n" +
    #         "1. Add new Plant \n" +
    #         "2. Add new Employee \n" +
    #         "3. Get plant by id \n" +
    #         "4. Get employee by id \n"
    #     )
    #     menu_flag = int(input("Your choose: "))
    #
    #     if menu_flag == 1:
    #         id = int(input("ID: "))
    #         location = input("Location: ")
    #         name = input("Name: ")
    #         director_id = int(input("Director ID: "))
    #         plant = Plant(id, location, name, director_id)
    #         plant.save()
    #
    #     elif menu_flag == 2:
    #         id = int(input("ID: "))
    #         name = input("Name: ")
    #         email = input("Email: ")
    #         department_type = input("Department Type: ")
    #         department_id = input("Department ID: ")
    #         employee = Employee(id, name, email, department_type, department_id)
    #         employee.save()
    #
    #     elif menu_flag == 3:
    #         id = int(input("ID: "))
    #         plant = Plant.get_by_id(id)
    #         print(plant)
    #
    #     elif menu_flag == 4:
    #         id = int(input("ID: "))
    #         employee = Employee.get_by_id(id)
    #         print(employee)
    Menu().run()
