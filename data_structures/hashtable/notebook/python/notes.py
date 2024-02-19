import json

class Notebook(object):
    def __init__(self, json_file=""):
        self.__notes = {}
        self.__tags  = {}
        self.__file  = json_file

    def __setitem__(self, title, text, tags=[]):
        self.__notes[title] = text
        for tag in tags:
            if self.__tags.get(tag):
                self.__tags.append(title)
            else:
                self.__tags = [title]

    def __getitem__(self, title):
        return self.__notes[title]
    
    def tag_search(self, tags):
        matches = []
        for tag in tags:
            notes = self.__tags.get(tag)
            if note:
                matches.append(notes)

        return matches

    def save(self, target_file=""):
        if target_file:
            # write to given file
            pass
        elif self.__file:
            # write to init file
            pass
        else:
            raise FileNotFoundError("No file set for this notebook.")

