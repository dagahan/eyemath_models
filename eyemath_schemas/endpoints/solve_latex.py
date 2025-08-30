from ..base_schema import *


class SolveRequest(BaseModel):
    latex_expression: str = Field(..., min_length=1, max_length=10_000)
    show_solving_steps: bool = False
    render_latex_expressions: bool = False


class SolveResponse(BaseModel):
    results: List[str] = []
    renders: List[str] = []
    solving_steps: List[str] = []


