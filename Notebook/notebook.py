from note import Note


class Notebook:
    """
    Represent a collection of notes that can be tagged, modified and searched.
    """

    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        :param memo: <str> text for the note
        :param tags: <str> reference tags
        :return: <id> new note's id
        """
        new_note = Note(memo, tags=tags)
        self.notes.append(new_note)

        return new_note.id

    def search_by_text(self, text):
        """
        Find all notes that match filter.
        :param text: <str> text to be used for filter
        :return: <list[Note]>
        """
        return [
            note for note in self.notes if note.match(text)
        ]

    def search_by_id(self, note_id):
        """
        Searches one note by it's id.
        :param note_id: <str,int,float> note's id
        :return: <Note> if match, False otherwise
        """
        if (isinstance(note_id, str) and note_id.isdigit()) \
                or isinstance(note_id, float):
            note_id = int(note_id)

        if not type(note_id) == int:
            return False

        for note in self.notes:
            if note.id == note_id:
                return note

        return False

    def modify_memo(self, note_id, new_memo):
        """
        Find the note with the given id and change its memo value.
        :param note_id: <str,int,float> note's id
        :param new_memo: <str> new memo value
        :return: <bool> True if successfully updated, False otherwise
        """
        note = self.search_by_id(note_id)
        if note:
            note.memo = new_memo

    def modify_tags(self, note_id, new_tags):
        """
        Find the note with the given id and change its tags value.
        :param note_id: <str,int,float> note's id
        :param new_tags: <str> new tags value
        :return: <bool> True if successfully updated, False otherwise
        """
        note = self.search_by_id(note_id)
        if note:
            note.tags = new_tags

    def delete_note(self, note_id):
        """
        Deletes the note with given id.
        :param note_id: <str,int,float> note's id
        :return: <bool> True if successfully updated, False otherwise
        """
        note = self.search_by_id(note_id)
        if note:
            self.notes.remove(note)
