from dataclasses import dataclass


@dataclass
class Product:
    title:str
    ownerId:str
    category:str
    price:float
    description:str

