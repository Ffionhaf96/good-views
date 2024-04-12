from models.models import User
from db.db import Session
from argon2 import PasswordHasher
from typing import Optional


def create(username: str, email: str, password: str) -> bool:
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


def get_by_id(id: int) -> Optional[User]:
    """Retrieve a user based on the ID or Email"""
    session = Session()
    return session.get(User, id)


def get_by_email(email: str) -> Optional[User]:
    session = Session()
    return session.query(User).filter_by(email=email).first()


def verify(email: str, password: str) -> Optional[str]:
    """Verify a user based on email and password combination"""
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    ph = PasswordHasher()

    # verify user supplied password matches stored hash
    if user and ph.verify(user.hashed_password, password):
        return user.email

    # user did not pass verification
    return None


def delete(email: str) -> bool:
    """Delete a user based on their email"""
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return None
    try:
        # delete the user
        session.delete(user)
        return True
    except Exception as e:
        print(f"Could not delete user - {e}")
        session.rollback()
        return False
    finally:
        session.close()


def update(
    email: str, username: Optional[str], name: Optional[str], avatar_path: Optional[str]
) -> bool:
    session = Session()
    user = session.query(User).filter_by(email=email)

    if username:
        user.username = username

    if name:
        user.name = name

    if avatar_path:
        user.avatar_path = avatar_path

    try:
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Couldn't update user {email} - {e}")
        return False


def follow(follower_email: str, followed_email: str):
    session = Session()
    follower = session.query(User).filter_by(email=follower_email)
    followed = session.query(User).filter_by(email=followed_email)

    try:
        follower.followed.append(followed)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't follow user {followed.email} - {e}")
        return False


def unfollow(follower_email: str, followed_email: str):
    session = Session()
    follower = session.query(User).filter_by(email=follower_email)
    followed = session.query(User).filter_by(email=followed_email)

    try:
        follower.followed.remove(followed)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't unfollow user {followed.email} - {e}")
        return False
