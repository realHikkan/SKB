class Certificate:
    def __init__(self, name, date, valid):
        self.common_name = name
        self.date = date
        self.valid = valid

    def get_common_name(self):
        return self.common_name

    def get_date(self):
        return self.date

    def get_valid(self):
        return self.valid
