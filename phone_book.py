from datetime import datetime
from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def iterator(self, n):
        data_list = list(self.data.items())
        while data_list:
            for i in data_list[:n]:
                yield i
            data_list = data_list[n:]


class Record:
    def __init__(self, name, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday

    def add_field(self, phone):
        self.phones.append(phone)

    def change_field(self, phone, new_phone):
        try:
            self.phones[self.phones.index(phone)] = new_phone
        except ValueError as e:
            print(e)

    def delete_field(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            print(f'{phone} is not in list')

    def days_to_birthday(self):
        now = datetime.today()
        try:
            if datetime(self.birthday.value.year, self.birthday.value.month, self.birthday.value.day) < now:
                birthday_date = datetime(now.year, self.birthday.value.month, self.birthday.value.day)
                if birthday_date > now:
                    return (birthday_date - now).days + 1
                else:
                    birthday_date = datetime(now.year + 1, self.birthday.value.month, self.birthday.value.day)
                    return (birthday_date - now).days + 1
            else:
                print('The date cannot be in the future!')
        except AttributeError:
            print('Wrong date format!')

    def __repr__(self):
        return f"{self.birthday} {self.phones}"


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __repr__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if value.isdigit():
            if len(value) == 10:
                self.value = value
            else:
                print('There should be 10 numbers!')
        else:
            print('There should be only numbers!')


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            s = datetime.strptime(value, '%Y-%m-%d').date()
            self.value = s
        except ValueError as e:
            print(e)


name = Name('Sasha')
phone = Phone('0236537890')
birthday = Birthday('2020-11-30')
name1 = Name('Masha')
phone1 = Phone('0948763456')
phone2 = Phone('0000000000')
birthday1 = Birthday('2020-10-30')
r = Record(name, birthday)
r.change_field(phone, phone2)
r.add_field(phone1)
r1 = Record(name1)
r.add_field(phone)
r1.add_field(phone1)
print(r.days_to_birthday())
print(r1.days_to_birthday())
ab = AddressBook()
ab.add_record(r)
ab.add_record(r1)
it = ab.iterator(3)
for i in it:
    print(i)

