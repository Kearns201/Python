class Hosterror(RuntimeError):
    def __init__(self, info):
        self.info = info


try:
    raise Hosterror("Bad hostname")
except Hosterror as e:
    print(e.info)
