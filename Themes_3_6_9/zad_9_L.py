from operator import itemgetter

class Car:
  ''' Автомобили '''
  def __init__(self, id, brand, model, year, color, price, owner_id):
    self.id = id
    self.brand = brand
    self.model = model
    self.year = year
    self.color = color
    self.price = price
    self.owner_id = owner_id


class Owner:
  ''' Автовладелец '''
  def __init__(self, id, fio):
    self.id = id
    self.fio = fio


class CarOwner:
  ''' Автомобили для реализации связи многие ко многим '''
  def __init__(self, owner_id, car_id):
    self.owner_id = owner_id
    self.car_id = car_id


def main():
  # Автовладельцы
  owners = [  
    Owner(1, 'Иванов И.И.'),
    Owner(2, 'Смирнов И.И.'),
    Owner(3, 'Анохив В.А.'),

    Owner(11, 'Пупкин И.И.'),
    Owner(22, 'Почкин И.И.'),
    Owner(33, 'Рогов В.А.'),
  ]    

  # Автомобили
  cars = [
    Car(1, 'BMW', 'X5', 2018, 'черный', 50000, 1),
    Car(2, 'Audi', 'A6', 2017, 'серебристый', 40000, 2),
    Car(3, 'Mercedes', 'E-class', 2019, 'белый', 60000, 3),
    Car(4, 'Toyota', 'Camry', 2016, 'синий', 30000, 11),
    Car(5, 'Honda', 'Accord', 2015, 'красный', 25000, 22),
    Car(6, 'Volkswagen', 'Golf', 2020, 'серый', 35000, 33),
  ]

  # Автомобили для реализации связи многие ко многим
  cars_owners = [
    CarOwner(1, 1),
    CarOwner(2, 2),
    CarOwner(3, 3),
    CarOwner(11, 4),
    CarOwner(22, 5),
    CarOwner(33, 6),
  ]

  # Соединение один ко многим
  one_to_many = [(c.brand, c.price, o.fio)
                 for o in owners
                 for c in cars
                 if c.owner_id == o.id]

  # Соединение многие ко многим
  many_to_many_temp = [(o.fio, co.owner_id, co.car_id)
                       for o in owners
                       for co in cars_owners
                       if o.id == co.owner_id]

  many_to_many = [(c.brand, c.price, fio)
                  for fio, owner_id, car_id in many_to_many_temp
                  for c in cars
                  if c.id == car_id]

  print('Задание 1:')
  print(sorted(one_to_many, key=itemgetter(0)))

  print('\nЗадание 2:')
  owners_cars = {}
  total_price = 0
  for o in owners:
    cars_price = sum([c.price for c in cars if c.owner_id == o.id])
    owners_cars[o.fio] = cars_price
    total_price += cars_price

  sorted_owners_cars = sorted(owners_cars.items(), key=itemgetter(1), reverse=True)
  for fio, price in sorted_owners_cars:
    print(f'Автовладелец: {fio}, Стоимость автомобилей: {price}')
  print(f'Суммарная стоимость автомобилей: {total_price}')

  print('\nЗадание 3:')
  owners_by_brand = {}
  for o in owners:
    brand = [c.brand for c in cars if c.owner_id == o.id][0]
    if brand in owners_by_brand:
      owners_by_brand[brand].append(o.fio)
    else:
      owners_by_brand[brand] = [o.fio]

  sorted_owners_by_brand = sorted(owners_by_brand.items(), key=itemgetter(0))
  for brand, fios in sorted_owners_by_brand:
    print(f'Бренд: {brand}, Автовладельцы: {", ".join(fios)}')


if __name__ == '__main__':
  main()
