from making_wallet import Wallet
from calculation import Calculation
from searching_notes import Search

with open('data_file.txt', encoding='UTF-8') as data:
    strings_from_file = data.readlines()
strings_from_file.append('\n')
print()
wallet = Wallet.create_set(strings_from_file)
print()
print('Приложение "Личный финансовый кошелёк" готово к работе.')
print()
print('ЭТО ГЛАВНОЕ МЕНЮ ПРОГРАММЫ:\n')
while True:
    choice_action = input('Введите целое число в отрезке от 1 до 5:\n\n'
                          '1 - узнать доходы, расходы и текущий баланс,\n'
                          '2 - добавить новую запись,\n'
                          '3 - изменить существующую запись,\n'
                          '4 - выполнить поиск записей по категории, дате или сумме,\n'
                          '5 - выйти из программы.\n\n')
    match choice_action:
        case '1':
            print()
            showing_balance = Calculation.create_object(wallet).object_to_string()
            print(showing_balance)
        case '2':
            print()
            if not data.closed:
                data.close()
            string_to_file = ''
            string_to_file += f'Дата: {input('Введите дату в формате ГГГГ-ММ-ДД\n\n')}\n'
            print()
            while True:
                choice_category = input('Введите целое число в отрезке от 1 до 2:\n\n'
                                        '1 - указать расход,\n'
                                        '2 - указать доход.\n\n')
                match choice_category:
                    case '1':
                        print()
                        string_to_file += 'Категория: Расход\n'
                        break
                    case '2':
                        print()
                        string_to_file += 'Категория: Доход\n'
                        break
                    case _:
                        print()
                        print('Введено некорректное число')
                        print()
            string_to_file += f'Сумма: {input('Введите сумму в формате целого числа\n\n')}\n'
            print()
            string_to_file += f'Описание: {input('Введите описание\n\n')}\n\n'
            if string_to_file in wallet:
                print()
                print('Такая запись уже существует и не может быть добавлена')
                print()
            else:
                print()
                wallet.add(string_to_file)
                set_to_list = sorted(wallet)
                set_to_list[-1] = set_to_list[-1].replace('\n\n', '\n')
                with open('data_file.txt', 'w', encoding='UTF-8') as data:
                    data.writelines(sorted(set_to_list))
                    data.flush()
                print('Запись добавлена в файл')
                print()
        case '3':
            print()
            print('Функционал не реализован')
            print()
        case '4':
            print()
            while True:
                choice_searching_way = input('Введите целое число в отрезке от 1 до 3:\n\n'
                                             '1 - поиск по дате,\n'
                                             '2 - поиск по категории,\n'
                                             '3 - поиск по сумме.\n\n')
                match choice_searching_way:
                    case '1':
                        print()
                        print('\nРезультаты поиска по дате:\n\n' +
                              ''.join(Search.search_by_value(sorted(wallet),
                                                             name='Дата',
                                                             value=input(
                                                                 'Введите дату в формате ГГГГ-ММ-ДД\n\n'
                                                             ))).strip())
                        break
                    case '2':
                        print()
                        while True:
                            choice_category = input('Введите целое число в отрезке от 1 до 2:\n\n'
                                                    '1 - указать расход,\n'
                                                    '2 - указать доход.\n\n')
                            match choice_category:
                                case '1':
                                    print()
                                    print('Результаты поиска по категории:')
                                    print()
                                    print(''.join(Search.search_by_value(sorted(wallet),
                                                                         name='Категория',
                                                                         value='Расход'
                                                                         )).strip())
                                    break
                                case '2':
                                    print()
                                    print('Результаты поиска по категории:')
                                    print()
                                    print(''.join(Search.search_by_value(sorted(wallet),
                                                                         name='Категория',
                                                                         value='Доход'
                                                                         )).strip())
                                    break
                                case _:
                                    print()
                                    print('Такой категории не существует')
                                    print()
                        break
                    case '3':
                        print()
                        print('\nРезультаты поиска по сумме:\n\n' +
                              ''.join(Search.search_by_value(sorted(wallet),
                                                             name='Сумма',
                                                             value=input(
                                                                 'Введите сумму в формате целого числа\n\n'
                                                             ))).strip())
                        print()
                        break
                    case _:
                        print()
                        print('Введено некорректное число')
                        print()
            print()
        case '5':
            print()
            print('Программа завершила свою работу.\n')
            print('Чтобы вернуться к работе с программой, введите команду:\npython interface.py')
            break
        case _:
            print()
            print('Введено некорректное число')
            print()
