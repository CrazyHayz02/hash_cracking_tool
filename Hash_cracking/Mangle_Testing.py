class mangles:

    def __init__(self, keyword):
        self.keyword = keyword

    def cap(self):
        return [(self.keyword).capitalize()]

    def up(self):
        return [(self.keyword).upper()]

    def append_num(self, start=0, end=11):
        return [(self.keyword) + str(num) for num in range(start,end)]

    def replace_a(self, A = ["@", "4"]):
        return [(self.keyword).replace("a", a) for a in A]

    def replace_s(self, S = ["$", "5"]):
        return [(self.keyword).replace("s", s) for s in S]

    def replace_i(self, I = ["!", "1"]):
        return [(self.keyword).replace("i", i) for i in I]

    def replace_g(self, G = ["6", "9"]):
        return [(self.keyword).replace("g", g) for g in G]

    def replace_t(self, T = ["7", "+"]):
        return [(self.keyword).replace("t", t) for t in T]

    def replace_b(self, B = ["8", "&"]):
        return [(self.keyword).replace("b", b) for b in B]

    def reverse(self):
        return [(self.keyword)[:: - 1]]

    def replace_h(self):
        return [(self.keyword).replace("h", "#")]

    def replace_o(self):
        return [(self.keyword).replace("o", "0")]

    def replace_e(self):
        return [(self.keyword).replace("e", "3")]

    def replace_l(self):
        return [(self.keyword).replace("l", "1")]

    def append_symbol(self, symbol = ["@", "_", "-", "%", "#", ">", "^"]):
        return [(self.keyword) + sym for sym in symbol]

    def append_123(self):
        return [(self.keyword)+"123"]

    def replace_z(self):
        return [(self.keyword).replace("z", "2")]

    

