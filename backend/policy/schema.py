from datetime import date
from pydantic import BaseModel, Field, EmailStr, root_validator, validator
from typing import Literal, Union, Optional
from .utils import age_validator, policy_number_validator, phone_number_validator


class RequiredFields(BaseModel):
    application_number: str = Field(min_length=1, max_length=50)
    customer_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    phone_number: str
    date_of_birth: date
    policy_cover: int = Field(ge=2500000, le=50000000)
    policy_status: Literal[
        "Requirements Awaited",
        "Requirements Closed",
        "Underwriting",
        "Policy Issued",
        "Policy Rejected",
    ]
    policy_number: str = None

    @validator("date_of_birth", pre=False, always=True)
    def check_if_valid_age(cls, date_of_birth):
        return age_validator(date_of_birth)

    @root_validator(pre=True)
    def check_if_valid_policy_number(cls, values):
        policy_status = values.get("policy_status")
        policy_number = values.get("policy_number")
        policy_number_validator(policy_status, policy_number)
        return values

    @validator("phone_number", pre=True, always=True)
    def check_if_valid_number(cls, number):
        phone_number_validator(number)
        return number


class AdditionalRequiredFields(RequiredFields):
    medical_type: Literal["Tele Medicals", "Physical Medicals"]
    medical_status: Literal["Pending", "Scheduled", "Waiting for Report", "Done"]


class IciciLife(RequiredFields):
    policy_type: Literal["ICICI Life"]
    remarks: str = Field(min_length=1, max_length=200)


class MaxLife(AdditionalRequiredFields):
    policy_type: Literal["Max Life"]


class HdfcLife(AdditionalRequiredFields):
    policy_type: Literal["HDFC Life"]
    remarks: str = Field(min_length=1, max_length=200)


class PolicyOut(BaseModel):
    id: int
    application_number: str
    customer_name: str
    email: str
    phone_number: str
    date_of_birth: date
    policy_cover: int
    policy_status: str
    policy_number: str = None
    medical_type: str = None
    medical_status: str = None
    policy_type: str = None
    remarks: str = None


class FilterParams(BaseModel):
    policy_status: Optional[str] = None
    customer_name: Optional[str] = None
    created_at: Optional[date] = None


class PolicyUpdate(BaseModel):
    customer_name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    policy_cover: Optional[int] = None
    policy_status: Optional[str] = None
    policy_number: Optional[str] = None
    medical_type: Optional[str] = None
    medical_status: Optional[str] = None
    remarks: Optional[str] = None

    @validator("date_of_birth", pre=False, always=True)
    def check_if_valid_age(cls, date_of_birth):
        if date_of_birth is not None:
            return age_validator(date_of_birth)
        return date_of_birth

    @root_validator(pre=True)
    def check_if_valid_policy_number(cls, values):
        policy_status = values.get("policy_status")
        policy_number = values.get("policy_number")
        policy_number_validator(policy_status, policy_number)
        return values

    @validator("phone_number", pre=True, always=True)
    def check_if_valid_number(cls, number):
        if number is not None:
            phone_number_validator(number)
            return number
        return number


class Comment(BaseModel):
    comment: str = Field(min_length=1, max_length=255)
    policy_id: int
