from life import settings, validate


class DataManager:
    def __init__(self, sections):
        self.data = None
        self.sections = sections

    @staticmethod
    def display_entry(label, entry, section=None):
        entry_str = ''
        if section:
            entry_str = '\nSection: {section}\n'.format(section=section)
        entry_str += 'Label: {label} -> From: {from_} - To: {to}'.format(label=label, from_=entry['from'], to=entry['to'])
        print(entry_str)

    def list_section_entries(self, section, all_=False):
        print(settings.SEP)
        if self.data.get(section):
            print('\033[1m{}\033[0m\n'.format(section.upper()))
            for label in self.data[section].keys():
                self.display_entry(label, self.data[section][label])
        else:
            print('\033[1m{}\033[0m section is empty.'.format(section.upper()))
        if not all_:
            print(settings.SEP)

    def list_all_entries(self, sections):
        for section in sections:
            self.list_section_entries(section, all_=True)
        print(settings.SEP[:-2])

    def add_entry(self):
        print('\nAdd entry to which section?')
        section = validate.get_item_from_list('sections', self.sections)
        # print('What is the label name?')
        label = validate.set_label()
        print('Starting date?')
        starting_date = validate.set_date()
        print('Finishing date?')
        finishing_date = validate.set_date(to_present_available=True, not_less_than=starting_date)

        entry = {'from': starting_date, 'to': finishing_date}
        self.display_entry(label, entry, section=section)

        while True:
            confirm = input('\nConfirm to \033[1;32madd\033[0m this entry [y/n]:\n> ').lower()
            if confirm == 'y':
                if self.data.get(section):
                    self.data[section][label] = entry
                else:
                    self.data[section] = {label: entry}
                print('\nEntry successfully added.')
                break
            elif confirm == 'n':
                print('\nNew entry has been discarded.')
                break

    # def update_entry(self):
    #     print('Update entry of which section?')
    #     section = validate.get_item_from_list('sections', self.sections)
    #     self.list_entries(section)

    def delete_entry(self):
        print('\nDelete entry from which section?')
        section = validate.get_item_from_list('sections', self.sections)
        self.list_section_entries(section)
        if self.data.get(section):
            print('Delete which label?')
            label = validate.get_item_from_list('labels', [label for label in self.data[section]])
            self.display_entry(label, self.data[section][label], section=section)
            while True:
                confirm = input('\nConfirm to \033[1;31mdelete\033[0m this entry [y/n]:\n> ').lower()
                if confirm == 'y':
                    self.data[section].pop(label)
                    print('\nEntry successfully deleted.')
                    break
                elif confirm == 'n':
                    print('\nEntry has not been deleted.')
                    break
