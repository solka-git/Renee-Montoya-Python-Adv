"""
клієнт - це рітейлер автомобілів.
Є завод, яикй випускає авто марки Рейні, конkретні моделі види і тд;
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
    Menu().run()
