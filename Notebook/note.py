import datetime


class Note:
    """
    Represent a note in the notebook.
    """

    note_id = 1

    def __init__(self, memo, tags=''):
        """
        Initialize a note automatically setting unique id and creation date.
        :param memo: <str> text for the note
        :param tags: <str> tags for quick search
        """
        self.id = Note.note_id
        self.memo = memo
        self.tags = tags
        self.created_date = datetime.date.today()

        Note.note_id += 1

    def match(self, text):
        """
        Determine if note matches the filter.
        :param text: <str> text to be searched for
        :return: <bool> True if matches, False otherwise
        """
        return text in self.memo or text in self.tags
