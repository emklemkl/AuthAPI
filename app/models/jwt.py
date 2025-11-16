from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app import db

class Jwt(db.Model):
    __tablename__ = "jwt"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    token: Mapped[str] = mapped_column(nullable=False)
    is_refresh_token: Mapped[bool] = mapped_column(nullable=True)
    expires_at: Mapped[datetime] = mapped_column(nullable=True)
    issued_at: Mapped[datetime] = mapped_column(default=datetime.now())

    user: Mapped["User"] = relationship("User", back_populates="tokens")


    