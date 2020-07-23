from random import shuffle

class SentenceGen:
    def __init__(self, path):
        raw_data = open(path, 'r').read()

        self.sentences = raw_data.split('\n')
        self.length = len(self.sentences)
        self.idx = 0

        shuffle(self.sentences)

    def _get_sentence (self):
        if self.idx >= self.length:
            shuffle(self.sentences)
            print(self)
            self.idx = 0
            return self._get_sentence()
        sentence = self.sentences[self.idx]
        self.idx += 1
        return sentence

    def __repr__(self):
        return '<SentenceGen length={},idx={}>'.format(self.length, self.idx)

    def __call__(self, count=1):
        sentences = [ self._get_sentence()
                      for _ in range(count) ]

        return " ".join(sentences)


