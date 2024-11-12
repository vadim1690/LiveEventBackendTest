# app/utils/face_encoding_utils.py
import face_recognition

def encode_face(file) -> list:
    """Encodes a face from the uploaded file. Returns the encoding as a list."""
    image = face_recognition.load_image_file(file)
    encodings = face_recognition.face_encodings(image)
    return encodings[0] if encodings else None
