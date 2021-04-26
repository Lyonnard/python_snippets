    """
    The more pythonic way is not to use setter and getter but the attribute
    directly, if you still want to use them:
    """

class Obj:
    """property demo"""
    #
    @property            # first decorate the getter method
    def attribute(self): # This getter method name is *the* name
        return self._attribute
    #
    @attribute.setter    # the property decorates with `.setter` now
    def attribute(self, value):   # name, e.g. "attribute", is the same
        self._attribute = value   # the "value" name isn't special
    #
    @attribute.deleter     # decorate with `.deleter`
    def attribute(self):   # again, the method name is the same
        del self._attribute