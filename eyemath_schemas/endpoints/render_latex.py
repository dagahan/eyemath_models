from ..base_schema import *


class RenderLatexRequest(BaseModel):
    latex_expression: str = Field(min_length=1)
    dpi: int | None = Field(default=None, ge=72, le=1200)


class RenderLatexResponse(BaseModel):
    render_image: str


