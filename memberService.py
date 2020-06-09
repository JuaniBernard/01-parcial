from repository import Repository


class MemberService:
    def add_member(self, member):
        key = len(Repository.membersList)
        while key in Repository.membersList:
            key = key + 1
        Repository.membersList[key] = member.__dict__
        return key

    def update_member(self, key, member):
        if key in Repository.membersList:
            Repository.membersList[key]['_name'] = member._name
            Repository.membersList[key]['_surname'] = member._surname
            Repository.membersList[key]['_age'] = member._age
            Repository.membersList[key]['_phone'] = member._phone
        else:
            raise ValueError("ID de member incorrecta.")

    def delete_member(self, key):
        if key in Repository.membersList:
            del Repository.membersList[key]
        else:
            raise ValueError("ID de member incorrecta.")
