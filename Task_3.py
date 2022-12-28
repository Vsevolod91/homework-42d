import json

class Operations():
    __slots__ = ("__date", "__state", "__amount", "__description", "__from_", "__to", "__cur",
                 "__date_print", "__from_print", "__to_print")
    __all_operations = []

    def __init__(self, date, state, amount, description, from_, to, currency):
        self.__all_operations.append(self)
        self.__date = date
        date_to_print = date.split("T")[0].split("-")
        date_to_print.reverse()
        self.__date_print = ".".join(date_to_print)
        self.__state = state
        self.__amount = amount
        self.__description = description
        self.__from_ = from_
        self.__from_print = self.hide(from_)
        self.__to = to
        self.__to_print = self.hide(to)
        self.__cur = currency

    @classmethod
    def all(cls):
        return cls.__all_operations

    @staticmethod
    def hide(string):
        if not string:
            return ""
        str_split = string.split(" ")
        if len(str_split) == 2:
            if str_split[0] == "Счет":
                return str_split[0] + " " + "**" + str_split[1][-4:]
            else:
                return str_split[0] + " " + str_split[1][:4] + " " + str_split[1][4:6] + "** " + "**** " + str_split[1][-4:]
        else:
            return str_split[0] + " " + str_split[1] + " " + str_split[2][:4] + " " + \
                   str_split[2][4:6] + "** " + "**** " + str_split[2][-4:]

    def __gt__(self, other):
        return self.__date > other

    def __lt__(self, other):
        return self.__date < other

    def __str__(self):
        return f"{self.__date_print} {self.__description} \n" \
               f"{self.__from_print} -> {self.__to_print} \n" \
               f"{self.__amount} {self.__cur} \n"

    def state(self):
        return self.__state

with open("operations.json", "r", encoding="utf-8") as f:
    operations = json.load(f)

    for i in operations:
        try:
            from_ = i["from"]
        except KeyError:
            from_ = ""

        try:
            date = i["date"]
            state = i["state"]
            amount = i["operationAmount"]["amount"]
            description = i["description"]
            to = i["to"]
            currency = i["operationAmount"]["currency"]["name"]
        except KeyError:
            continue

        Operations(date=date, state=state, amount=amount, description=description,
                   from_=from_, to=to, currency=currency)

    count = 0
    Operations.all().sort(reverse=True)
    for inst in Operations.all():
        if inst.state() == "EXECUTED":
            print(inst)
            count += 1
            if count == 5:
                break
        else:
            continue

