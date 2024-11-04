import runner_and_tournament
import unittest

# Напишите класс TournamentTest, наследованный от TestCase.
class TournamentTest(unittest.TestCase):
# setUpClass - метод, где создаётся атрибут класса all_results.
#       Это словарь в который будут сохраняться результаты всех тестов.
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

# setUp - метод, где создаются 3 объекта:
#
#     Бегун по имени Усэйн, со скоростью 10.
#     Бегун по имени Андрей, со скоростью 9.
#     Бегун по имени Ник, со скоростью 3.
    def setUp(self):
        self.run_Yce = runner_and_tournament.Runner('Усэйн', 10)
        self.run_And = runner_and_tournament.Runner('Андрей', 9)
        self.run_Nik = runner_and_tournament.Runner('Ник', 3)
# Так же методы тестирования забегов, в которых создаётся объект Tournament
# на дистанцию 90. У объекта класса Tournament запускается метод start,
# который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект
# из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют
# (порядок передачи в объект Tournament соблюсти):
#
#     Усэйн и Ник
#     Андрей и Ник
#     Усэйн, Андрей и Ник.
#
# Как можно понять: Ник всегда должен быть последним.

    def test_run_1(self):
        tournament = runner_and_tournament.Tournament(90, self.run_Yce, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_run_2(self):
        tournament = runner_and_tournament.Tournament(90, self.run_And, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')


    def test_run_3(self):
        tournament = runner_and_tournament.Tournament(90, self.run_Yce, self.run_And, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')

# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
# В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее,
# чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.

    def test_run_4(self):
        tournament = runner_and_tournament.Tournament(90,  self.run_Nik, self.run_And, self.run_Yce)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[min(result.keys())] == 'Усэйн')

   #tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            #преобразуем dict к читабельному виду, т.к. Runner поменять не можем
            result_print = {k: str(v) for k, v in result.items()}
            print(result_print)

if __name__ == '__main__':
    unittest.main()