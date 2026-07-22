import sys
from pathlib import Path

import cv2
import face_recognition as fr

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from config.logger_config import logger

def face_scan():
    
    known_image_path = BASE_DIR / "tests" / "fixtures" / "known_face.jpg"
    test_image_path = BASE_DIR / "tests" / "fixtures" / "unknown_face6.jpg"

    if not known_image_path.exists() or not test_image_path.exists():
        logger.error("Erro: Uma ou ambas as imagens não foram encontradas na pasta!")
        return

    known_image = fr.load_image_file(known_image_path)
    known_encoding = fr.face_encodings(known_image)[0]

    test_image = fr.load_image_file(test_image_path)
    test_encodings = fr.face_encodings(test_image)

    if len(test_encodings) > 0:
        test_encoding = test_encodings[0]
    
        results = fr.compare_faces([known_encoding], test_encoding, tolerance=0.6)
    
        if results[0]:
            logger.info("Access granted: Face recognized!")
        else:
            logger.info("Alert: Unknown face.")
    else:
        logger.info("No faces found in the test image.")

if __name__ == "__main__":
    face_scan()