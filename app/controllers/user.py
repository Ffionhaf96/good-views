from models.models import User
from db.db import Session
from argon2 import PasswordHasher
from typing import Optional


def create(name: str, username: str, email: str, password: str) -> bool:
    """Create a user and save it to the database"""
    # Create a new session
    session = Session()

    # Check if a user with the given username already exists
    existing_user = session.query(User).filter_by(username=username).first()

    if existing_user is not None:
        return False

    # Hash the password for security
    ph = PasswordHasher()
    hashed_pass = ph.hash(password)
    new_user = User(
        name=name, username=username, email=email, hashed_password=hashed_pass
    )

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
    """Retrieve a user based on the ID"""
    session = Session()
    return session.get(User, id)


def get_by_email(email: str) -> Optional[User]:
    """Retrieve a user based on the email"""
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


def follow(follower_id: str, followed_id: str) -> Optional[int]:
    """Follower a user based on the id"""
    session = Session()
    follower = session.get(User, follower_id)
    followed = session.get(User, followed_id)

    try:
        follower.followed.append(followed)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't follow user {followed.id} - {e}")
        return None

    return followed.id


def unfollow(follower_id: int, followed_id: int) -> Optional[int]:
    """Unfollow a user based on the id"""
    session = Session()

    unfollower = session.get(User, follower_id)
    unfollowed = session.get(User, followed_id)

    try:
        unfollower.followed.remove(unfollowed)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't unfollow user {unfollowed.id} - {e}")
        return None

    return unfollowed.id


def is_following(follower_id: int, followee_id: int) -> bool:
    """Check if a user is following another user"""
    session = Session()

    follower = session.get(User, follower_id)
    followee = session.get(User, followee_id)

    if not follower or not followee:
        return False

    return followee in follower.followed
