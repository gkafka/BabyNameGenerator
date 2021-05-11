import csv
import os
import random

class BabyNameGenerator(object):
    """TODO Docstring
    """

    def __init__(self, use_weights):
        self._firsts = []
        self._middles = []
        self._lasts = []

        self._w_firsts = None
        self._w_middles = None
        self._w_lasts = None

        self._use_weights = use_weights

    @property
    def firsts(self):
        return self._firsts
    @firsts.setter
    def firsts(self, value):
        self._firsts = value

    @property
    def lasts(self):
        return self._lasts
    @lasts.setter
    def lasts(self, value):
        self._lasts = value

    @property
    def middles(self):
        return self._middles
    @middles.setter
    def middles(self, value):
        self._middles = value

    @property
    def use_weights(self):
        return self._use_weights

    @property
    def w_firsts(self):
        return self._w_firsts
    @w_firsts.setter
    def w_firsts(self, value):
        self._w_firsts = value

    @property
    def w_lasts(self):
        return self._w_lasts
    @w_lasts.setter
    def w_lasts(self, value):
        self._w_lasts = value

    @property
    def w_middles(self):
        return self._w_middles
    @w_middles.setter
    def w_middles(self, value):
        self._w_middles = value

    @staticmethod
    def load(path):
        """TODO Docstring
        """

        names = []
        weights = []

        try:
            with open(path) as f:
                cr = csv.reader(f)

                for row in cr:
                    tokens = row[0].split('/')
                    tokens = [t.strip() for t in tokens]

                    for t in tokens:
                        names.append(t)
                        weights.append(float(row[1])/len(tokens))
        except Exception as e:
            print('Error reading input {0}: {1}'.format(path, e))

        return names, weights

    def generateName(self):
        """TODO Docstring
        """

        weights = self.w_firsts if self.use_weights else None
        first = random.choices(self.firsts, weights)[0]

        weights = self.w_middles if self.use_weights else None
        middle = random.choices(self.middles, weights)[0]

        weights = self.w_lasts if self.use_weights else None
        last = random.choices(self.lasts, weights)[0]

        print('{0} {1} {2}\n{0} {2}'.format(first, middle, last))
        print('{0}{1}{2}'.format(first[0].upper(), middle[0].upper(), last[0].upper()))
        print()

    def loadFirsts(self, names):
        """TODO Docstring
        """

        if os.path.exists(names):
            self.firsts, self.w_firsts = self.load(names)
        else:
            self.firsts = [names]
            self.w_firsts = None

        return

    def loadMiddles(self, names):
        """TODO Docstring
        """

        if os.path.exists(names):
            self.middles, self.w_middles = self.load(names)
        else:
            self.middles = [names]
            self.w_middles = None

    def loadLasts(self, names):
        """TODO Docstring
        """

        if os.path.exists(names):
            self.lasts, self.w_lasts = self.load(names)
        else:
            self.lasts = [names]
            self.w_lasts = None
