from random import shuffle

class SentenceGen:
    def __init__(self, path):
        raw_data = open(path, 'r').read()
        
        self.sentences = raw_data.split('\n')
        self.length = len(self.sentences)
        self.idx = 0

        shuffle(self.sentences)

    def _get_sentence (self):
        sentence = self.sentences[self.idx]
        self.idx += 1
        return sentence

    def __call__(self, count=1, as_list=False):
        if self.idx >= self.length:
            shuffle(self.sentences)
            self.idx = 0
            return self(*args, **kwargs)
        else:
            sentences = [ self._get_sentence()
                          for _ in range(count) ]
            if as_list:
                return sentences
            else:
                return " ".join(sentences)


