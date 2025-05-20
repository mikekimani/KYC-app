from pydantic import BaseModel

class KYCResponse(BaseModel):
    ocr_data: dict
    face_match: bool
    liveness_passed: bool
    status: str
