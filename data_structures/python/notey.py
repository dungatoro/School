import pickle

class Notebook(object):
    def __init__(self, file=""):
        self.__file = file
        try:
            f = open(file, 'rb')
        except:
            self.__notes = {}
            self.__tags  = {}
        else:
            self.__notes = pickle.load(f)
            self.__tags = pickle.load(f)
            f.close()

    def add_note(self, title, text, *tags):
        self.__notes[title] = text
        for tag in tags:
            if self.__tags.get(tag):
                self.__tags[tag].append(title)
            else:
                self.__tags[tag] = [title]

    def __getitem__(self, title):
        return self.__notes[title]

    def search_tags(self, *tags):
        matches = []
        for tag in tags:
            notes = self.__tags.get(tag)
            if notes:
                matches.append(notes)
        return matches

    def __pickle(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.__notes, f)
            pickle.dump(self.__tags, f)

    def save(self, target_file=""):
        if target_file: 
            self.__pickle(target_file)
        elif self.__file:
            self.__pickle(self.__file)
        else:
            raise FileNotFoundError("No file set for this notebook.")

if __name__ == "__main__":
    n = Notebook("notey.pickle")
    n.add_note("shopping list", "cheese, tomato, shoe", "shopping", "todos")
    print(n.search_tags("todos", "shopping"))
    n.save()

