from models.models import User, List
from db.db import Session


def create_list(name: str, user: User) -> bool:
    session = Session()
    new_list = List(name=name, user=user.id)

    try:
        # Add the new list to the session and commit
        session.add(new_list)
        session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def delete_list(list_id: str, user: User) -> bool:
    session = Session()
    content_list = session.get(List, list_id)

    try:
        # Remove the list and commit the session
        session.delete(content_list)
        session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
        return False
    finally:
        session.close()
