class T:
    def __init__(self, x):
        self.num = x


class F:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.t = T(x)
        self.f = F(y)

    def print_num(self):
        print(self.f.num, self.t.num)


if __name__ == "__main__":
    pool = Pool(1, 10)
    pool.print_num()
