from pydantic import BaseModel, StrictFloat, StrictStr, field_validator

class CreateUserRequest(BaseModel):
    name: StrictStr
    phone_number: StrictStr
    height: StrictFloat
    bio: StrictStr | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        import re

        if re.fullmatch(r"010-\d{4}-\d{4}", phone_number) is None:
            raise ValueError("phone_number must be in 010-XXXX-XXXX format")
        return phone_number

    @field_validator("bio")
    @classmethod
    def validate_bio(cls, bio: str | None) -> str | None:
        if bio is not None and len(bio) > 500:
            raise ValueError("bio must be 500 characters or fewer")
        return bio

class UserResponse(BaseModel):
    user_id: int
    name: str
    phone_number: str
    height: float
    bio: str | None = None