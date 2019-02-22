class ShippingContainer:
    # for our class variables
    next_serial = 1337

    # staticmethod decorator means it doesn't get the 'self' arg
    #@staticmethod
    #def _get_next_serial():
    #
    # classmethod decorator means it gets a class (cls) arg
    #@classmethod
    #def _get_next_serial(cls):
    @classmethod
    def _get_next_serial(cls):
        # underscore, by convention, makes it 'non-public'
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # can use classmethod to make named constructors, also known
    # as factory methods
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents = None)

    def __init__(self, owner_code, contents):
        # instance variables, associated with instances of the class
        self.owner_code = owner_code
        self.contents = contents
        self.celsius = 0
        
        # next_serial isn't in any of the searched scopes (local, 
        # enclosing function, global, built-in) and -- this is important --
        # classes do NOT introduce new scope
        #
        # so we must expressly state the scope/namespace:
        # self.serial = next_serial
        #
        # we could have used self, as with instance variables, but
        # then it's confusing and not obvious
        # self.serial = self.next_serial
        # self.next_serial += 1 # this, however, will *create* an instance var!
        #
        # these are 'most correct'
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        #
        # though, in practice, it makes sense to have a method
        # that does this sort of thing:
        self.serial = ShippingContainer._get_next_serial()

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32
    
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return ShippingContainer._c_to_f(self.celsius)
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = ShippingContainer._f_to_c(value)
    