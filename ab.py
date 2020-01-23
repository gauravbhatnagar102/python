class Base:
    @staticmethod
    def f1():
        print('Base class static func.')
class Derived(Base):
   # @staticmethod
    def f2(self):
        print('ilu')
        super().f1()
ch=Derived()
ch.f2()

