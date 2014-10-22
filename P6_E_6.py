class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (self.__class__.__name__, # My class's name
                                                          self.__listSuper(),
                                                          id(self), # My address
                                                          self.__attrnames()) # name=value list
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__): # Instance attr dict
            result += '\tname %s=%s\n' % (attr, self.__dict__ [attr])
        return result
    
    def __listSuper(self):
        result = []
        for cls in self.__class__.__bases__:
            result.append(cls.__name__)
        result = ', '.join(result)
        return result
 
 
        