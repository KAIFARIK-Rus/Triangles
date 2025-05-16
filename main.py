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
