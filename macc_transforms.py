from pydantic_classes import AbatementMeasure


def macc_transforms(validated_data: list[AbatementMeasure]) -> list[AbatementMeasure]:
    validated_data.sort(key=lambda row: row.marginal_cost)
    return validated_data
