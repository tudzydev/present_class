class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price   # ใครก็แก้ได้!

p = Product(1, 'สมุดโน้ต', 45.00)
p.price = -500   # ไม่มีอะไรทักท้วงเลย
print(p.price)