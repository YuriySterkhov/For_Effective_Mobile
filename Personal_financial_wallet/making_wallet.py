from making_note import Note

class Wallet:
    def __init__(self, new_note='', list_of_notes='', wallet_as_set=''):
        self.new_note = new_note
        self.list_of_notes = list_of_notes
        self.wallet_as_object = wallet_as_set

    @classmethod
    def create_set(cls, _strings_from_file):
        new_note = ''
        list_of_notes = []
        wallet_as_set = set()
        for string in _strings_from_file:
            if string != '\n':
                new_note += string
            else:
                list_of_notes.append(new_note)
                new_note = ''
            if string is _strings_from_file[len(_strings_from_file) - 2]:
                list_of_notes.append(new_note)
                break
        for string in list_of_notes:
            note = Note.create_object(string)
            wallet_as_set.add(note)
        return wallet_as_set
