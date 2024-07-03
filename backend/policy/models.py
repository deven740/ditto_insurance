from sqlalchemy import Column, Integer, String, Date, Text, func, DateTime, ForeignKey
from database import Base


class PolicyModel(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    application_number = Column(String(50), nullable=False)
    customer_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(25), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    policy_cover = Column(Integer, nullable=False)
    policy_status = Column(String(25), nullable=False)
    policy_number = Column(String(50), nullable=True)
    medical_type = Column(String(25), nullable=True)
    medical_status = Column(String(25), nullable=True)
    policy_type = Column(String(25), nullable=False)
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())


class CommentModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text)
    policy_id = Column(
        Integer, ForeignKey("policies.id", ondelete="CASCADE"), nullable=False
    )
