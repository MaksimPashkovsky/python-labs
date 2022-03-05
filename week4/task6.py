"""
Get
"""


class Entity:

    def __init__(self, par1: int, par2: str, values: list):
        self.par1 = par1
        self.par2 = par2
        self.values = values

    def __getattr__(self, item):
        """
        Getting invoked only if object has no attribute 'item',
        otherwise uses built-it __getattr__.
        """
        return f"Object has no attribute '{item}'"

    def __getattribute__(self, item):
        """
        Getting invoked every time the attribute 'item' being looked for,
        no matter whether the object has it
        NOTE: if class contains both methods __getattr__ and __getattribute__
        then __getattribute__ is called first. But if __getattribute__ raises
        AttributeError exception then the exception will be ignored and __getattr__
        method will be invoked.
        """
        if item.startswith('xyz'):
            raise AttributeError
        if item.startswith('abc'):
            raise Exception
        return object.__getattribute__(self, item)

    def __getitem__(self, item):
        """
        Getting a value by key.
        """
        if not isinstance(item, int):
            raise KeyError
        return self.values[item]

    def __get__(self, instance, owner):
        """
        Defines the dynamic return value when accessing a specific instance and
        class attribute.
        Getting invoked when accessing the attribute through the owner class.
        """
        return self.par1


class SecondEntity:

    entity = Entity(777, "ooo", [3, 1, 7, 9, 0])


if __name__ == '__main__':
    e = Entity(123, "321", [0, 2, 4, 6, 8])

    # __getattr__ example
    # getting an existing attribute (built-in __getattr__ used)
    res1 = getattr(e, 'par1')
    # getting non-existing attribute (redefined method used)
    res2 = getattr(e, 'qwerty')
    # Results:
    # res1 == 123
    # res2 == "Object has no attribute 'qwerty'"

    # __getattribute__ example
    # getting an existing attribute (redefined method used)
    res3 = getattr(e, 'par1')
    # getting non-existing attribute (__getattr__ used because AttributeError is raised)
    res4 = getattr(e, 'xyzqwe')
    # getting non-existing attribute (we'll get an Exception)
    # res5 = getattr(g, 'abcqwe')
    # Results:
    # res3 == "123"
    # res4 == "Object has no attribute 'xyzqwe'"
    # res5 - Exception

    # __getitem__ example
    # getting value by key 2
    res6 = e[2]
    # getting value by key 100 - we'll get an IndexError (index 100 is out of range)
    # res7 = e[100]
    # getting value by key 'asd' - we'll get a KeyError (only int keys are allowed in redefined method)
    # res8 = e['asd']
    # Results:
    # res6 == 4
    # res7 - IndexError
    # res8 - KeyError

    # __get__ example
    # creating new SecondEntity object
    se = SecondEntity()
    # getting an attribute (through __get__ method of Entity class)
    res9 = se.entity
    # Result:
    # res9 == 777
