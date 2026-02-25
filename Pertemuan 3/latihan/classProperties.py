class Person:
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name

  @name.deleter
  def name(self):
    del self._name

p1 = Person("Emil")
print(p1.name)

p1.name = "Tobias"
print(p1.name)

del p1.name