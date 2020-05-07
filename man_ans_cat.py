from random import randint


class Man:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я {}, живу в доме'.format(self.name)

    def work(self):
        if self.house.money < 50:
            self.house.money += 100
            print('Сходил на работу. Денег стало в доме: {}'.format(self.house.money))
            self.house.mud -= 20
            self.house.food -= 30

    def buy_eat_to_cat(self):
        self.house.food += 100
        print('Купил в магазине еды: {}'.format(self.house.food))
        self.house.money -= 50

    def cleen(self):
        self.house.mud += 100
        print('Почистил дом, грязи: {} '.format(self.house.mud))
        self.house.food -= 30

    def go_into_the_home(self, house):
        self.house = house
        self.house.food -= 20
        self.house.mud -= 20
        print('Въехал в дом: {}'.format(self.name))


    def act(self):
        dice = randint(1, 6)
        if dice == 1:
            self.work()
        elif dice == 2:
            self.cleen()
        elif 2 < dice < 4:
            self.buy_eat_to_cat()
        else:
            print('Cидит дома смотрит ТВ. В доме еды: {} , денег: {}, грязи: {}'.format(self.house.food, self.house.money, self.house.mud))
            self.house.mud -= 20
            self.house.food -= 20


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я кот - {}, сытость: {}'.format(self.name, self.fullness)

    def go_into_the_home(self, house):
        self.house = house
        self.house.food -= 20
        self.house.mud -= 20
        print('Въехал в дом: {}'.format(self.name))

    def sleep(self):
        print('{} лег спать'.format(self.name))
        self.fullness -= 10


    def eat(self):
        print('{} ест'.format(self.name))
        self.house.food -= 10
        self.fullness += 20

    def tears_wallpaper(self):
        print('{} рвет обои'.format(self.name))
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness < 0:
            print('Кот умер ...')
        dice = randint(1, 6)
        if dice == 1 or dice == 3:
            self.eat()
        elif dice == 2 or dice == 4:
            self.tears_wallpaper()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 0
        self.mud = 0
        self.money = 0

    def __str__(self):
        return 'В доме еды: {} , денег: {}, грязи: {}'.format(self.food, self.money, self.mud)






c = Man(name='Вася')
home = House()
c.go_into_the_home(house=home)

for day in range(1, 365):
    print('================ {} день ================'.format(day))
    c.act()
    print(c)
