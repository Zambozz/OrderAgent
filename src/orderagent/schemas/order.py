from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class OrderStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    BLOCKED = "blocked"
    COMPLETED = "completed"


class Order(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_id: str = Field(min_length=1)
    customer_id: str = Field(min_length=1)
    status: OrderStatus
    reason: str | None = None
    created_at: datetime


class OrderInvestigationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str = Field(min_length=5, max_length=2000)
    order_id: str = Field(min_length=1)
