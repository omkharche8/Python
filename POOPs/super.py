class A:
    def __init__(self):
        print("A's __init__")
        super().__init__()


class B:
    def __init__(self):
        print("B's __init__")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C's __init__")
        super().__init__()


c = C()



