import csv

class InputCvsFile():

    def __init__(self, config):
        self.file = config["file"]
        self.data = []

    def process(self):

        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.data.append(list(csv_reader))


