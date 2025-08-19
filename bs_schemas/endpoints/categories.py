from ..base_schema import *
from ..product_type import ProductTypeDTO


class CategoriesRequest(BaseModel):
    categories: Optional[List[ProductTypeCategory]] = None


class CategoriesResponse(BaseModel):
    product_tupes: List[ProductTypeDTO]

