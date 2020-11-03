#! /usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import os


class FileFinder:
    def __init__(self, path_origin, match_word, ignore_case=False):
        """
        :param path_origin: str, directory path where to recursively search for files
        :param match_word: str, word to match in file name
        :param ignore_case: bool, True to perform case insensitive search
        """
        self.path_origin = path_origin
        self.match_word = match_word
        self.files_matched = []
        self.ignore_case = ignore_case

    def run(self):
        self.search_files()
        self.display_matches()

    def search_files(self):
        print('\nSearching...')
        for path, directories, files in os.walk(self.path_origin):
            for file in files:
                file_path = os.path.join(path, file)
                if self.is_match(file_path):
                    self.files_matched.append(file_path)

    def is_match(self, file_path):
        if not self.ignore_case:
            return self.match_word in file_path.split(os.sep)[-1]
        else:
            return self.match_word.lower() in file_path.split(os.sep)[-1].lower()

    def display_matches(self):
        if self.files_matched:
            print('\nMatches found:')
            for file_path in self.files_matched:
                print(file_path)
        else:
            print('\nNo matches found.')


if __name__ == '__main__':
    # Parsing args
    parser = argparse.ArgumentParser(description='File finder.')
    parser.add_argument('directory_path', help='Absolute path of directory where to run the search.')
    parser.add_argument('match_word', help='Word to be matched in file name.')
    parser.add_argument('--ignorecase', help='Activate mode to ignore case sensitive.', default=False, action='store_true')

    args = parser.parse_args()

    file_finder = FileFinder(args.directory_path, args.match_word, ignore_case=args.ignorecase)
    file_finder.run()
