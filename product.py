class Product:
    def __init__(self, title=None, price=None, seller=None, stars=None,
                 photos=None, characteristics=None, link=None, position=None, description=None):
        self.title = title
        self.price = price
        self.photos = photos
        self.characteristics = characteristics
        self.link = link
        self.position = position
        self.description = description
        self.stars = stars
