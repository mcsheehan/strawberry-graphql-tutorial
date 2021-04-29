import pathlib

import shelve
from typing import List, Dict

class Database:

    def _get_database_file_location(self) -> str:
        return str(pathlib.Path.cwd() / ".." / "the_source_of_truth.db")

    def _open_database_connection(self, file_location: str):
        our_rubbish_db = shelve.open(file_location)
        return our_rubbish_db

    def __init__(self):
        """
        We store the database instance in self.db this is the shelf file and we open it on class instantiation
        """
        self.db = self._open_database_connection(self._get_database_file_location())

    def get_all_books(self)-> List[Dict]:
        self.db
        return []

    def store_book(self, item: Dict):
        pass


if __name__ == '__main__':
    # Lets play with shelve
    rubbish_db = shelve.open("../junk_db_file")

    rubbish_db["binday"] = "Tuesday"
    binday = rubbish_db["binday"]

    print(binday)
    rubbish_db.close()

    rubbish_db = shelve.open("junk_db_file")
    print(rubbish_db["binday"])
