from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from backend.auth.auth_utils import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from backend.kyc.schemas import KYCResponse
from backend.services.ocr_service import extract_text
from backend.services.face_service import compare_faces
from backend.services.liveness import check_liveness
import shutil, uuid, os

router = APIRouter(prefix="/kyc", tags=["kyc"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def save_temp_file(upload_file: UploadFile) -> str:
    filename = f"temp_{uuid.uuid4()}.jpg"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return filename

@router.post("/verify", response_model=KYCResponse)
async def verify_kyc(
    id_image: UploadFile = File(...),
    selfie_image: UploadFile = File(...),
    token: str = Depends(oauth2_scheme)
):
    user = decode_access_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Save files locally (or use S3 if needed)
    id_path = save_temp_file(id_image)
    selfie_path = save_temp_file(selfie_image)

    try:
        # Step 1: OCR on ID
        ocr_data = extract_text(id_path)

        # Step 2: Face match
        face_match = compare_faces(id_path, selfie_path)

        # Step 3: Liveness
        liveness_passed = check_liveness(selfie_path)

        # Status
        status = "approved" if face_match and liveness_passed else "rejected"

        return KYCResponse(
            ocr_data=ocr_data,
            face_match=face_match,
            liveness_passed=liveness_passed,
            status=status
        )

    finally:
        os.remove(id_path)
        os.remove(selfie_path)
        