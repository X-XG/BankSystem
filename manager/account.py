import checker


class account:
    def __init__(self) -> None:
        pass

    def aa(self):
        checker.name('3')
        # raise Exception("no aa")


b = account()
try:
    b.aa()
except Exception as e:
    print(e)
