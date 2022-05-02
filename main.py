class Person:
  def __init__(self, name, city):
    self.name = name
    self.city = city

  def get_name(self):
    return self.name
  
  def get_city(self):
    return self.city

  def set_name(self, new_name):
    self.name = new_name
    return self
