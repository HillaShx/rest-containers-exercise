from pydantic import BaseModel


def fields_to_update(model: BaseModel):
    changed_fields = {k: v for k, v in model.__dict__.items() if v is not None}
    return changed_fields
