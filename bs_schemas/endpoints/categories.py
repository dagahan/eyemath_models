from ..base_schema import *


class CategoriesRequest(BaseModel):
    pass


class CategoriesResponse(BaseModel):
    categories: List[ProductTypeCategory]

