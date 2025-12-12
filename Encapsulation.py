class Myclass:
    def __init__(self):
        self._protected_var = 10
        self.__private_var = 20

        
obj=Myclass()

print(obj.__private_var)   ## Output: 10 
print(obj._protected_var)  ## AttributeError: 'MyClass' object has no attribute '__private_var'