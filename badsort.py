class Solution:
    def FindTheGuest(self, liste: list, target: str):
        for i in range(len(liste)):
            if liste[i] == target:
                # find first var of the list and then do until target
                first = liste.index(0)
                stored = []
                while True:
                    if first != target:
                        stored.append(first)
                        first += 1
                    else:
                        return stored
