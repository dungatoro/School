import pickle
import cmd
import datetime as dt

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
        self.__notes[title] = text, dt.datetime.now()
        for tag in tags:
            if self.__tags.get(tag):
                self.__tags[tag].append(title)
            else:
                self.__tags[tag] = [title]

    def __getitem__(self, title):
        if self.__notes.get(title):
            return f"{self.__notes[title][0]}"
        else:
            return f"No note called {title}"

    def search_tags(self, *tags):
        matches = []
        for tag in tags:
            if titles := self.__tags.get(tag):
                matches += titles
        return list(set(matches)) # remove duplicates

    def titles(self):
        items = [(k, v) for k, (_, v) in self.__notes.items()]
        for title, date in sorted(items, key=lambda x: x[1], reverse=True):
            print(f"* {date.strftime('%d/%m/%y')}\t{title}")

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

class NotebookCli(cmd.Cmd):
    notebook = Notebook("notey.pickle")
    prompt = " >> "

    def __parse(self, line):
        return [s.strip() for s in line.split('"') if s.strip()]

    def postcmd(self, stop, line):
        self.notebook.save()
        return 

    def cmdloop(self, intro=None):
        print(intro)
        while True:
            try:
                super().cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")
                exit(0)

    def do_make_note(self, line):
        """
        Add or overwrite a note in the notebook.
         ~> make_note "title" "text" "tag1" tag2" ...
        """
        try:
            title, text, *tags = self.__parse(line)
        except:
            print("Invalid arguments")
        else:
            self.notebook.add_note(title, text, *tags)
            print(f"Note titled {title} added to notebook!")

    def do_search_title(self, line):
        """
        Print the contents of a .
         ~> search_title "title"
        """
        try: 
            title, *_ = self.__parse(line)
        except:
            print("Invalid arguments")
        else:
            print(self.notebook[title])

    def do_search_tags(self, line):
        """
        Search by tags.
         ~> search_tags "tag1" "tag2" ...
        """
        try:
            tags = self.__parse(line)
        except:
            print("Invalid arguments")
        else:
            matches = self.notebook.search_tags(*tags)
            if matches:
                for match in matches: print(f"* {match}")
            else:
                print("No matches found")

    def do_titles(self, _):
        """
        Print a list of all page titles.
        """
        self.notebook.titles()

if __name__ == "__main__":
    NotebookCli().cmdloop("Welcome to your notebook! Type 'help' if needed.")

