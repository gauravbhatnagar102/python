class Base:
    def __init__(self):
        self.a=10
    @staticmethod
    def gaurav():
         print('I love you')
class Child(Base):
    @staticmethod
    def gaurav():
        print('ILU')
        super().gaurav()
Child.gaurav()