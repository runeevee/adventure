import entity

class Player(entity.Entity):
  def __init__(self, name):
    super().__init__(name, 100)
  