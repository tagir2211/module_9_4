first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda i, j: i == j, first, second)))

def get_advanced_writer(file_name):
  def write_everything(*data_set):
    with open(file_name, 'w', encoding='utf-8') as file:
      for data in data_set:
        file.write(f'{data} \n')
  return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
  def __init__(self, *words):
    self.words = [word for word in words]
  def __call__(self):
    from random import choice
    return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())