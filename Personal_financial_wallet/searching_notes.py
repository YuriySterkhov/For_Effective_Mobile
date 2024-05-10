class Search:
    @staticmethod
    def search_by_value(_strings_from_file, name, value):
        searching_result = []
        for string in _strings_from_file:
            if name in string and value in string:
                searching_result.append(string)
        if len(sorted(searching_result)) == 0:
            return 'Запись не найдена'
        else:
            return sorted(searching_result)
