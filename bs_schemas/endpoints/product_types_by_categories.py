from ..base_schema import *
from ..product_type import ProductTypeDTO


class ProductTypesByCategoriesRequest(BaseModel):
    categories: Optional[List[ProductTypeCategory]] = None


class ProductTypesByCategoriesResponse(BaseModel):
    product_types: List[ProductTypeDTO]

