#__init__()
class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = person("John", 36)

print(p1.name)
print(p1.age)

p2 = person("John", 36)

print(p2.name, p2.age)
