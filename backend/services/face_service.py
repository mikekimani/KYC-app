from deepface import DeepFace

def compare_faces(id_path: str, selfie_path: str) -> bool:
    try:
        result = DeepFace.verify(img1_path=id_path, img2_path=selfie_path, enforce_detection=False)
        return result["verified"]
    except Exception:
        return False
