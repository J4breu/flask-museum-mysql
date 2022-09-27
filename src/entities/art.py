
from email.mime import image


class Art():
  def __init__(self, id, title = None, imageLink = None, gender = None, status = None, author = None, price = None, commision = None) -> None:
    self.id = id
    self.title = title
    self.imageLink = imageLink
    self.gender = gender
    self.status = status
    self.author = author
    self.price = price
    self.commision = commision

class Escultura(Art):
	def __init__(self, id, title, imageLink, gender, status, author, price, commision, dimensions, material) -> None:
		super().__init__(id, title, imageLink, gender, status, author, price, commision)
		self.dimensions = dimensions
		self.material = material

class Pintura(Art):
	def __init__(self, id, title, imageLink, gender, status, author, price, commision, dimensions, tecnic, corriente) -> None:
		super().__init__(id, title, imageLink, gender, status, author, price, commision)
		self.dimensions = dimensions
		self.tecnic = tecnic
		self.corriente = corriente

class Orfebreria(Art):
	def __init__(self, id, title, imageLink, gender, status, author, price, commision, tecnic, form) -> None:
		super().__init__(id, title, imageLink, gender, status, author, price, commision)
		self.title = title
		self.tecnic = tecnic
		self.form = form

class Fotografia(Art):
	def __init__(self, id, title, imageLink, gender, status, author, price, commision, resolution, dimensiones) -> None:
		super(Fotografia, self).__init__(id, title, imageLink, gender, status, author, price, commision)
		self.resolution = resolution
		self.dimensiones = dimensiones

class Ceramica(Art):
	def __init__(self, id, title, imageLink, gender, status, author, price, commision, material, color) -> None:
		super().__init__(id, title, imageLink, gender, status, author, price, commision)
		self.material = material;
		self.color = color;