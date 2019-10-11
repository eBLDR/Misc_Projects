import os
import sys

from notebook import Notebook


class Menu:
    """
    Display a menu and respond to choices when run.
    """

    def __init__(self):
        """
        Initializes a menu with a Notebook with its corresponding choices.
        """
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_by_text,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.delete_note,
            'Q': self.quit_,
        }

    @staticmethod
    def quit_():
        """
        Stop process.
        """
        print('Thanks for using Notebook.')
        sys.exit(0)

    @staticmethod
    def display_menu():
        """
        Displays menu in terminal.
        """
        print(
"""
- Notebook Menu -

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Delete Note
Q. Quit
"""
        )

    def run(self):
        """
        Main manager, displays menu and takes action based on user's choice.
        """
        while True:
            os.system('clear')
            self.display_menu()
            choice = self.get_user_choice()
            os.system('clear')
            self.choices[choice]()
            self.continue_()

    def add_note(self):
        """
        Creates a new note.
        """
        memo, tags = self.get_memo_and_tags()
        new_id = self.notebook.new_note(memo, tags=tags)

        print('Note with id "{0}" added.'.format(new_id))

    def show_notes(self, notes=None):
        """
        Displays passed notes, or all notes.
        :param notes: <list[Note]> notes to be displayed
        """
        if not notes:
            notes = self.notebook.notes

        if not notes:
            print('Notebook is empty!')

        for note in notes:
            print('Id: {0}\tDate: {1}\nTags: [{2}]\nMemo: "{3}"\n'.format(
                note.id, note.created_date, note.tags, note.memo)
            )

    def search_by_text(self):
        """
        Ask a text filter to user, searches and displays notes.
        """
        while True:
            text = input('Search for: ')
            if text:
                break

        notes = self.notebook.search_by_text(text)

        if not notes:
            print('No notes found matching "{0}".'.format(text))

        self.show_notes(notes=notes)

    def modify_note(self):
        """
        Modifie memo and tags form a note.
        """
        note_id = self.get_note_id()
        if not note_id:
            return

        new_memo, new_tags = self.get_memo_and_tags()

        self.notebook.modify_memo(note_id, new_memo)

        if new_tags:
            self.notebook.modify_tags(note_id, new_tags)

        print('Note with id "{0}" modified.'.format(note_id))

    def delete_note(self):
        """
        Delete completely a note.
        """
        note_id = self.get_note_id()
        if not note_id:
            return

        self.notebook.delete_note(note_id)

        print('Note with id "{0}" deleted.'.format(note_id))

    # Utils
    @staticmethod
    def continue_():
        print('\n' + '=' * 30 + '\n')
        input('Enter when done... ')

    def get_user_choice(self):
        """
        Validates user choice.
        :return: <str> valid choice
        """
        while True:
            choice = input('Option: ').upper()
            if choice in self.choices:
                return choice

            print('"{0}" is not a valid choice.'.format(choice))

    @staticmethod
    def get_memo_and_tags():
        """
        Asks to user memo and tags information.
        :return: (<str>, <str>) memo, tags
        """
        while True:
            memo = input('Memo: ')
            if memo:
                break

        tags = input('Tags (or Enter for blank): ')

        return memo, tags

    def get_note_id(self):
        """
        Ask user input for a note id.
        :return: <str> note id False otherwise
        """
        note_id = input('Note id: ')

        if not self.notebook.search_by_id(note_id):
            print('Note with id "{0}" not found.'.format(note_id))
            return False

        return note_id
