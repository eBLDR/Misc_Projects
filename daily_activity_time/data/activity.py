from data.constants import DAILY_MINUTES


class Activity:
    def __init__(self, label, minutes, category=None, flag=None):
        self.label = label
        self.minutes = minutes
        self.category = category
        self.flag = flag.lower() == 'true' if flag else None
        self.daily_percentage = round(minutes * 100 / DAILY_MINUTES, 1)

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            label=dict_data.get('label'),
            minutes=round(float(dict_data.get('minutes', 0)), 2),
            category=dict_data.get('category'),
            flag=dict_data.get('flag'),
        )


class ActivityList(list):
    def __init__(self):
        super().__init__()
        self.categories = set()

    def append(self, new_object):
        super().append(new_object)
        self.categories.add(new_object.category)

    def get_all_items_by_category(self, category):
        return [
            object_ for object_ in self if object_.category == category
        ]
