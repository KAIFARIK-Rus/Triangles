class TriangleTester:
    def __init__(self):
        self.case_count = 0
        self.bug_count = 0

    def check_triangle(self, a, b, c):
        # Проверка на существование треугольника
        if a + b > c and a + c > b and b + c > a:
            # Определение типа треугольника
            if a == b == c:
                return "Равносторонний треугольник"
            elif a == b or b == c or a == c:
                return "Равнобедренный треугольник"
            else:
                return "Разносторонний треугольник"
        else:
            return "Треугольник не существует"

    def check_cases(self, a, b, c):
        # Кейс 1: Пустые поля
        if a == '0' and b == '0' and c == '0':
            print("Кейс 1: Пустые поля пройден.")
            self.case_count += 1

        # Кейс 2: Частично заполненные поля
        if (a != '0' and b != '0' and c == '0') or (a != '0' and b == '0' and c != '0') or (
                a == '0' and b != '0' and c != '0'):
            print("Кейс 2: Частично заполненные поля пройден.")
            self.case_count += 1

        # Кейсы 3-7: Позитивные кейсы
        if (a == '3' and b == '4' and c == '5') or (a == '2' and b == '3' and c == '4') or (
                a == '66' and b == '67' and c == '68') or (a == '3' and b == '3' and c == '5') or (
                a == '6' and b == '6' and c == '6'):
            print("Кейсы 3-7: Позитивные кейсы пройдены.")
            self.case_count += 5

        # Кейс 8: Не треугольник
        try:
            if float(a) + float(b) <= float(c) or float(a) + float(c) <= float(b) or float(b) + float(c) <= float(a):
                print("Кейс 8: Не треугольник пройден.")
                self.case_count += 1
        except ValueError:
            pass

        # Кейс 9: Не числовой ввод
        try:
            float(a)
            float(b)
            float(c)
        except ValueError:
            print("Кейс 9: Не числовой ввод пройден.")
            self.case_count += 1

        # Кейс 10: Большие числа
        try:
            if float(a) > 4294967295 or float(b) > 4294967295 or float(c) > 4294967295:
                print("Кейс 10: Большие числа пройден.")
                self.case_count += 1
        except ValueError:
            pass

        # Кейс 11: SQL-инъекция
        if 'select' in str(a) or 'or' in str(b) or 'where' in str(c):
            print("Кейс 11: SQL-инъекция пройден.")
            self.case_count += 1

        # Кейс 12: XSS-уязвимость
        if '<script>' in str(a) or '<script>' in str(b) or '<script>' in str(c):
            print("Кейс 12: XSS-уязвимость пройден.")
            self.case_count += 1

    def check_bugs(self, a, b, c):
        # Баг 1: Поле C не проверяется
        if c == '0' and (a != '0' or b != '0'):
            print("Баг 1: Поле C не проверяется найден.")
            self.bug_count += 1

        # Баг 2: Равносторонний треугольник с нулевыми сторонами
        if a == '0' and b == '0' and c == '0':
            print("Баг 2: Равносторонний треугольник с нулевыми сторонами найден.")
            self.bug_count += 1

        # Баг 3: Не целые числа
        try:
            float(a)
            float(b)
            float(c)
            if '.' in str(a) or '.' in str(b) or '.' in str(c):
                print("Баг 3: Не целые числа найден.")
                self.bug_count += 1
        except ValueError:
            pass

        # Баг 4: XSS с регистрозависимостью
        if '<SCRIPT>' in str(a) or '<SCRIPT>' in str(b) or '<SCRIPT>' in str(c):
            print("Баг 4: XSS с регистрозависимостью найден.")
            self.bug_count += 1

    def run_tests(self, a, b, c):
        self.check_cases(a, b, c)
        self.check_bugs(a, b, c)

        print(f"\nВсего кейсов пройдено: {self.case_count}")
        print(f"Всего багов найдено: {self.bug_count}")
        self.case_count = 0
        self.bug_count = 0


def main():
    tester = TriangleTester()

    while True:
        print("напишите stop для выхода")
        # Ввод данных от пользователя
        a = input("Введите длину первой стороны: ")
        if a.lower() == 'stop':
            break

        b = input("Введите длину второй стороны: ")
        c = input("Введите длину третьей стороны: ")

        # Проверка кейсов и багов
        tester.run_tests(a, b, c)


if __name__ == "__main__":
    main()
