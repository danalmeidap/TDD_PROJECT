import uuid
from datetime import UTC, datetime

from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixim(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    class Config:
        validate_assignment = True
