# For_Effective_Mobile
Сontains the results of the test task

Создано приложение "Личный финансовый кошелёк" для учета личных доходов и расходов.

Основные возможности:
1. Вывод баланса: реализовано.
2. Добавление записи: реализовано.
3. Редактирование записи: НЕ РЕАЛИЗОВАНО (цейтнот).
4. Поиск по записям: реализовано.

Требоания к программе:
1. Интерфейс: выполнено.
2. Хранение данных: выполнено.
3. Информация в записях: выполнено.

Дополнительно:
1. Аннотации: НЕ РЕАЛИЗОВАНО (цейтнот).
2. Документация: НЕ РЕАЛИЗОВАНО (цейтнот).
3. Описание функционала: представлено ниже.
4. GitHub: реализовано.
5. Тестирование: выполнено ручное тестирование.
6. Объектно-ориентированный подход программирования: реализовано частично.

Описание приложения:
1. Приложение создано и протестировано в системе: Windows 10 Домашняя для одного языка версии 22H2.
2. Personal_financial_wallet - директория проекта.
3. venv - виртуальное окружение, здесь удалены папки Include, Lib, Scripts и оставлен файл pyvenv.cfg, в нём описание конфигурации окружения.
4. Установка приложения:
    4.1. Скопировать папку Personal_financial_wallet в нужную директорию.
    4.2. Открыть папку Personal_financial_wallet.
    4.3. Удалить папку venv.
    4.4. Создать в папке Personal_financial_wallet виртуальное окружение.
5. Запуск приложения:
    5.1. Запустить командную строку.
    5.2. Запустить команду <путь>cd Personal_financial_wallet && venv\Scripts\activate && python interface.py
         в командной строке, <путь> - путь к директории, куда скопирована папка Personal_financial_wallet.
7. Файлы:
    6.1. data_file.txt - файл для хранения записей.
    6.2. __init__.py - пустой файл, создан для удобства импорта.
    6.3. interface.py - основной файл приложения, взаимодействующий с пользователем:
         читает файл data_file.txt, создаёт список строк этого файла и передаёт его making_wallet.py
    6.4. making_wallet.py создаёт список записей (здесь запись - строка сложенная из элементов среза списка             строк из файла) и передаёт его making_note.py.
    6.5. Планировалось, что making_note.py будет преобразовывать каждую запись в экземпляр класса Note (не
         реализовано). making_note.py получает значения полей date, category, amount, description каждого
         элемента полученного списка записей и передаёт их в f-строку.
    6.6. f-строки, возвращённые из making_note.py, добавляются в множество, создаваемое making_wallet.py.
    6.7. Множество возвращается в interface.py, таким образом, после запуска приложения мы имеем прочитанный и          закрытый файл и доступное множество записей. Пользователь видит сообщение: 'Приложение "Личный                 финансовый кошелёк" готово к работе.' и главное меню программы.
    6.8. 
    6
