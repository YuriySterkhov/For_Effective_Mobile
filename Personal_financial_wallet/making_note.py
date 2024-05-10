class Note:
    def __init__(self, date='', category='', amount='', description=''):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    @classmethod
    def create_object(cls, note_as_string):
        sliced_copy = note_as_string
        date = sliced_copy[:sliced_copy.find('\n')]
        sliced_copy = sliced_copy[sliced_copy.find('\n') + 1:]
        category = sliced_copy[:sliced_copy.find('\n')]
        sliced_copy = sliced_copy[sliced_copy.find('\n') + 1:]
        amount = sliced_copy[:sliced_copy.find('\n')]
        sliced_copy = sliced_copy[sliced_copy.find('\n') + 1:]
        description = sliced_copy[:sliced_copy.find('\n')]
        return f'{date}\n{category}\n{amount}\n{description}\n\n'
