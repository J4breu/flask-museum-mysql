class Artwork():
  def __init__(self, id, clientId, title, image, price) -> None:
    self.id = id
    self.clientId = clientId
    self.title = title
    self.image = image
    self.price = price

class Ceramic(Artwork):
  def __init__(self, artworkId, color, composition) -> None:
    self.artworkId = artworkId
    self.color = color
    self.composition = composition

class Photography(Artwork):
  def __init__(self, artworkId, dimensions, resolution) -> None:
    self.artworkId = artworkId
    self.dimensions = dimensions
    self.resolution = resolution

class Painting(Artwork):
  def __init__(self, artworkId, dimensions, gender, technique, stream) -> None:
    self.artworkId = artworkId
    self.dimensions = dimensions
    self.gender = gender
    self.technique = technique
    self.stream = stream

class Goldsmith(Artwork):
  def __init__(self, artworkId, materials, technique, appearance) -> None:
    self.artworkId = artworkId
    self.materials = materials
    self.technique = technique
    self.appearance = appearance

class Sculpture(Artwork):
  def __init__(self, artworkId, description, materials) -> None:
    self.artworkId = artworkId
    self.description = description
    self.materials = materials