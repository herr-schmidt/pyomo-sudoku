from select import select


class DataMaker:
    def __init__(self):
        self.dataDictionary = {None: {
            'I': {None: 9},
            'J': {None: 9},
            'N': {None: 9},
            'R': {None: 3},
            'C': {None: 3},
        }
        }

    def make_example_data(self):
        exampleData = self.dataDictionary
        exampleData[None]['f'] = {
            (1, 1): 5, (1, 2): 3, (1, 5): 7,
            (2, 1): 6, (2, 4): 1, (2, 5): 9, (2, 6): 5,
            (3, 2): 9, (3, 3): 8, (3, 8): 6,
            (4, 1): 8, (4, 5): 6, (4, 9): 3,
            (5, 1): 4, (5, 4): 8, (5, 6): 3, (5, 9): 1,
            (6, 1): 7, (6, 5): 2, (6, 9): 6,
            (7, 2): 6, (7, 7): 2, (7, 8): 8,
            (8, 4): 4, (8, 5): 1, (8, 6): 9, (8, 9): 5,
            (9, 5): 8, (9, 8): 7, (9, 9): 9,
        }
        return exampleData

    def make_indices(self):
        return self.dataDictionary