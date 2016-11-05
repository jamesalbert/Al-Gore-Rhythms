

from .paths import AllPairs


class FloydWarshall(AllPairs):
    def find_path(self):
        return self.D[-1]
