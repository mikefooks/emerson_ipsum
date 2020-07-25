from random import shuffle

class StringGen:
    def __init__(self, path):
        with open(path, "r") as raw_data:
            self.strings = raw_data.read().split('\n')

        self.length = len(self.strings)
        self.idx = 0

        shuffle(self.strings)

    def sample(self):
        if self.idx >= self.length:
            shuffle(self.strings)
            self.idx = 0
            return self.sample()
        string = self.strings[self.idx]
        self.idx += 1
        return string

    def __repr__(self):
        return '<StringGen length={},idx={}>'.format(self.length, self.idx)

    def __call__(self, count=1, as_list=False, delim=" "):
        strings = [ self.sample()
                    for _ in range(count) ]

        return strings if as_list else delim.join(strings)


