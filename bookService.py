from repository import Repository


class BookService:
    def add_book(self, book):
        key = len(Repository.booksList)
        while key in Repository.booksList:
            key = key + 1
        Repository.booksList[key] = book.__dict__
        return key

    def update_book(self, key, book):
        if key in Repository.booksList:
            Repository.booksList[key]['_name'] = book._name
            Repository.booksList[key]['_authorName'] = book._authorName
            Repository.booksList[key]['_memberLegajo'] = book._memberLegajo
        else:
            raise ValueError("ID de book incorrecta.")

    def assign_book(self, book_key, member_key):
        if book_key in Repository.booksList:
            if member_key in Repository.membersList:
                Repository.booksList[book_key]['_memberLegajo'] = member_key
            else:
                raise ValueError("ID de member incorrecta.")
        else:
            raise ValueError("ID de book incorrecta.")
