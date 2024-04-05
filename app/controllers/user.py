from models.models import User
from db.db import Session

def create_user(username: str, email: str, password: str) -> bool:
    # Create a new session
    session = Session()

    # Check if a user with the given username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    
    if existing_user is not None:
        return False
    
    # TODO: actually hash password

    new_user = User(username=username, email=email, hashed_password=password)

    try:
    # Add the new user to the session and commit
        session.add(new_user)
        session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
        return False
    finally:
        session.close()