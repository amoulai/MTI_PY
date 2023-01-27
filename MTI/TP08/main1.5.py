class Data:
    """Data Class"""
    d_id = 10


class SubData(Data):
    """SubData Class"""
    sd_id = 20


print(Data.__class__)
print(Data.__bases__)
print(Data.__dict__)
print(Data.__doc__)
print(SubData.__class__)
print(SubData.__bases__)
print(SubData.__dict__)
print(SubData.__doc__)
