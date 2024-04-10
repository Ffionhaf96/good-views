from models.models import User
from db.db import Session
from argon2 import PasswordHasher
from typing import Optional


def create_user(username: str, email: str, password: str) -> bool:
    # Create a new session
    session = Session()

    # Check if a user with the given username already exists
    existing_user = session.query(User).filter_by(username=username).first()

    if existing_user is not None:
        return False

    # Hash the password for security
    ph = PasswordHasher()
    hashed_pass = ph.hash(password)
    new_user = User(username=username, email=email, hashed_password=hashed_pass)

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


def verify_user(email: str, password: str) -> Optional[str]:
    """Verify a user based on email and password combination"""
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    ph = PasswordHasher()

    # verify user supplied password matches stored hash
    if user and ph.verify(user.hashed_password, password):
        return user.email

    # user did not pass verification
    return None
