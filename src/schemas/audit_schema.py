from pydantic import (
    BaseModel,
    ConfigDict,
)


class AuditLogResponse(BaseModel):
    """
    Representação pública de um registro
    permanente de auditoria.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    user_id: int

    action: str
    module: str

    entity_type: str
    entity_id: int

    description: str | None

    old_values: str | None
    new_values: str | None

    justification: str | None

    created_at: str