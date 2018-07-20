def mod(indx, base, prime):
    res = 1
    for i in range(indx):
        res *= base
        res %= prime
    #     print(res)
    #     print(i)
    # print(res)
    return res


class hash:
    def __init__(self, values, prime, base=4):
        self.prime = prime
        self.base = base
        self.values = values #{'A': 0, 'a': 0, 'C': 1, 'c': 1, 'G': 2, 'g': 2, 'T': 3, 't': 3}
        # self.residue_8 = mod(8, self.base, self.prime)
        self.residue_16 = mod(16, self.base, self.prime)
        self.residue_32 = (self.residue_16*self.residue_16) % prime
        self.residue_64 = (self.residue_32*self.residue_32) % prime

    def calc(self, str):
        res = 0
        for i in range(len(str)):
            res += (self.values.get(str[i]) * self.rec_mod(i)) % self.prime
            res %= self.prime
        # print(res)
        return res

    def rec_mod(self, i):
        res = 1
        if i < 0:
            print("Error: negetive indx")
            return res
        elif i == 0:
            return res
        elif i >= 64:
            res = self.residue_64*self.rec_mod(i-64)
        elif i >= 32:
            res = self.residue_32*self.rec_mod(i-32)
        elif i>= 16:
            res = self.residue_16*self.rec_mod(i-16)
        # elif i>= 8:
        #     res = self.residue_8*self.rec_mod(i-8)

        res = mod(i, self.base, self.prime)

        return res % self.prime
