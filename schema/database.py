import pathlib

import shelve
from typing import List, Dict

class Database:

    def _get_database_file_location(self) -> str:
        return str(pathlib.Path.home() / "the_source_of_truth.db")

    def __init__(self):
        """
        We store the database instance in self.db this is the shelf file and we open it on class instantiation
        """
        self.db = shelve.open(self._get_database_file_location())

    def get_all_books(self)-> List[Dict]:
        # Lets write the code to get all the values from our database
        # return list(self.db.values())
        return []

    def store_book(self, item: Dict):
        key = item["title"]
        self.db[key] = item


if __name__ == '__main__':
    # Lets play with shelve
    rubbish_db = shelve.open("../junk_db_file")

    rubbish_db["binday"] = "Tuesday"
    binday = rubbish_db["binday"]

    print(binday)
    rubbish_db.close()

    rubbish_db = shelve.open("../junk_db_file")
    print(rubbish_db["binday"])
