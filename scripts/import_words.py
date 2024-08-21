import re
import sys
import os

from requests import Session


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.api.v1.models.models import Entry
from app.db.database import SessionLocal


def read_file_as_bytes(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        content = file.read()
    return content.decode('latin-1', errors='ignore')

def import_words_from_file(file_path: str, db: Session):
    try:

        content = read_file_as_bytes(file_path)
        words = [line.strip() for line in content.splitlines() if line.strip()]
        for word in words:
            sanitized_word = sanitize_word(word)
            result = db.query(Entry).filter(Entry.word == sanitized_word).first()
           
            print(f"Sanitized word: '{sanitized_word}'")
            print(db.query(Entry).filter(Entry.word == sanitized_word).first()) 
            if sanitized_word and not db.query(Entry).filter(Entry.word == sanitized_word).first():
                db.add(Entry(word=sanitized_word))
               
        db.commit()
        
        print(f"Successfully imported {len(words)} words.")
    except Exception as e:
        print(f"Error occurred: {e}")
        print({result})
        db.rollback()

def sanitize_word(word: str) -> str:
    word = word.strip()
    word = word.strip('—“”\'`–.''')
    word = re.sub(r'[^\w\s]', '', word)
    word = ' '.join(word.split())
    return word


def main():
    db = SessionLocal()
    file_path = os.path.join('data', 'english.txt')
    import_words_from_file(file_path, db)
    db.close()

if __name__ == "__main__":
    main()
