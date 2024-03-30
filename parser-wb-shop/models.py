from pydantic import BaseModel, field_validator


class Price(BaseModel):
    product: int

    @field_validator('product')
    def convert_sale_price(cls, sale_price: int) -> float:
        if sale_price is not None:
            return sale_price / 100


class Sizes(BaseModel):
    price: Price


class Products(BaseModel):
    id: int
    name: str
    brand: str
    sizes: list[Sizes]
    reviewRating: float


class Items(BaseModel):
    products: list[Products]
