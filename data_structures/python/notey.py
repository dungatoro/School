import pickle

class Notebook(object):
    def __init__(self, file=""):
        try:
            with open(file, 'rb') as f:
                self = pickle.load(f)
        except:
            self.__file  = file
            self.__notes = {}
            self.__tags  = {}

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

    def save(self, target_file=""):
        if target_file:
            with open(target_file, 'wb') as f:
                pickle.dump(self, f)
        elif self.__file:
            with open(self.__file, 'wb') as f:
                pickle.dump(self, f)
        else:
            raise FileNotFoundError("No file set for this notebook.")

if __name__ == "__main__":
    n = Notebook("notes.pickle")
    # n.add_note("shopping list", "cheese, tomato, shoe", "shopping", "todos")
    print(n.search_tags("todos", "shopping"))
    n.save()

