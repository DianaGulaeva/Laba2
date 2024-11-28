import re
class PhoneValidation:
    country_phone_codes = [
        # Все коды северной Америки
        "+1","+1242","+1246", "+1264","+1268","+1284","+1340",
        "+1345","+1441","+1473","+1649","+1664","+1670",
        "+1671","+1684","+1721","+1758","+1767","+1784","+1787",
        "+1809","+1829","+1849","+1868","+1869","+1876","+1939",

        # Вся Африка
        "+20","+211","+212","+213","+216","+218","+220","+221",
        "+222","+223","+224","+225","+226","+227","+228","+229",
        "+230","+231","+232","+233","+234","+235","+236","+237",
        "+238","+239","+240","+241","+242","+243","+244","+245",
        "+246","+247","+248","+249","+250","+251","+252","+253",
        "+254","+255","+256","+257","+258","+260","+261","+262",
        "+262","+263","+264","+265","+266","+267","+268","+269",
        "+27","+290","+291","+297","+298","+299",

        # Вся Европа
        "+30","+31","+32","+33","+34","+350","+351","+352","+353",
        "+354","+355","+356","+357","+358","+35818","+359","+36",
        "+370","+371","+372","+373","+374","+37447","+375","+376",
        "+377","+378","+380","+381","+382","+385","+386","+387","+389",
        "+39","+3906698","+40","+41","+420","+421","+423","+43","+44",
        "+441481","+441534","+441624","+4428","+45","+46","+47","+48","+49",

        # Южная Америка + чуть-чуть северной
        "+500","+501","+502","+503","+504","+505","+506","+507",
        "+508","+509","+51","+52","+53","+54","+55","+56","+57",
        "+58","+590","+591","+592","+593","+594","+595","+596",
        "+597","+598","+599",

        # Океания
        "+60","+61","+6189162","+6189164","+62","+63","+64","+65",
        "+66","+670","+6721","+6723","+673","+674","+675","+676",
        "+677","+678","+679","+680","+681","+682","+683","+685",
        "+686","+687","+688","+689","+690","+691","+692",

        # Россия, Казахстан, Абхазия
        "+7", "+7840",

        # Азия и Арабы
        "+81","+82","+84","+850","+852","+853","+855","+856","+86",
        "+880","+886","+90","+90392","+91","+92","+93","+94","+95",
        "+960","+961","+962","+963","+964","+965","+966","+967","+968",
        "+970","+971","+972","+973","+974","+975","+976","+977","+98",
        "+992","+993","+994","+995","+996","+9971","+998"
    ]

    def validate_phone_numbers(self, file_path):
        valid_numbers = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if re.match(r'^\+?\d+$', line):
                    for code in sorted(self.country_phone_codes, key=len, reverse=True):
                        if code in line:
                            digits = line[len(code):]
                            if len(digits) == 10 and re.match(r'^\d+$', digits):
                                valid_numbers.append(line)
                                break
                    else:
                        continue

        return valid_numbers

    def add_by_user(self, filepath):
        with open(filepath, 'a') as file:
            phone_number = input("Введите номер телефона (например, +7XXXXXXXXXX или +1242XXXXXXXXXX): ")

            # Проверяем, начинается ли номер с одной из подстрок из country_phone_codes
            if any(phone_number.startswith(code) for code in self.country_phone_codes):
                # Проверяем, состоит ли строка только из цифр и может ли начинаться с '+'
                if re.match(r'^\+?\d+$', phone_number):
                    for code in sorted(self.country_phone_codes, key=len, reverse=True):
                        if code in phone_number:
                            digits = phone_number[len(code):]
                            if len(digits) == 10 and re.match(r'^\d+$', digits):
                                print("Валидный номер успешно добавлен в список.")
                                file.write(phone_number + '\n')
                                return True  # Возвращаем True, если номер был успешно добавлен
                                break
                            else:
                                print("Неверный формат. Номер должен содержать ровно 10 цифр после кода страны.")
                                return False  # Возвращаем False, если номер не соответствует ожидаемому формату
                    else:
                        print("Неверный формат. Код страны не найден или номер не соответствует ожидаемому формату.")
                        return False
                else:
                    print("Неверный формат. Пожалуйста, используйте только цифры и может начинаться с '+'.")
                    return False
            else:
                print("Неверный формат. Пожалуйсьа, используйте один из поддерживаемых форматов.")
                return False

    def main_menu(self):
        while True:
            print("\nВыберите действие:")
            print("1. Добавить номер телефона в файл")
            print("2. Просмотреть содержимое файла")
            print("3. Валидация номеров")
            print("4. Выйти из программы")

            choice = input("Введите число от 1 до 4: ")

            if choice == '1':
                self.add_by_user('numbers.txt')
            elif choice == '2':
                try:
                    with open('numbers.txt', 'r') as file:
                        print(file.read())
                except FileNotFoundError:
                    print("Файл numbers.txt не существует.")
            elif choice == '3':
                valid_numbers = self.validate_phone_numbers('numbers.txt')

                print(f"Обнаружено {len(valid_numbers)} валидных номеров:")
                for number in valid_numbers:
                    print(number)
            elif choice == '4':
                print("Конец работы")
                break
            else:
                print("Неверный выбор. Пожалуйся, выберите число от 1 до 4.")

# стартуем
phone_validator = PhoneValidation()

if __name__ == '__main__':
    phone_validator.main_menu()