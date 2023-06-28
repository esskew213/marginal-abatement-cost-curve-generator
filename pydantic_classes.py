from enum import Enum
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, condecimal, validator


class MACCOutputFormat(Enum):
    PNG = 'png'
    SVG = 'svg'


class AbatementMeasure(BaseModel):
    name: str
    net_econ_cost: condecimal(decimal_places=2)
    abatement: condecimal(decimal_places=2, gt=Decimal(0))
    category: Optional[str]

    @property
    def marginal_cost(self) -> Decimal:
        return self.net_econ_cost / self.abatement

    @classmethod
    def strip_space_and_convert_to_lowercase(cls, some_string: str) -> str:
        return some_string.lower().strip()

    @validator('category')
    def validate_category(cls, category: str) -> str:
        return cls.strip_space_and_convert_to_lowercase(category)

    @validator('name')
    def validate_name(cls, name: str) -> str:
        return cls.strip_space_and_convert_to_lowercase(name)