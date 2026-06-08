from sqlalchemy import select, delete
from database import SessionLocal
from models import Film


def add_films():
    session = SessionLocal()
    try:
        films = [
            Film(title="Inception", director="Nolan", release_year=2010),
            Film(title="Matrix", director="Wachowski", release_year=1999),
            Film(title="Interstellar", director="Nolan", release_year=2014),
            Film(title="Ida", director="Pawlikowski", release_year=2013),
            Film(title="City of God", director="Meirelles", release_year=2002),
            Film(title="City of God", director="Meirelles", release_year=2002),
            Film(title="The Shawshank Redemption", director="Darabont", release_year=1994),
        ]

        for film in films:
            exists = session.query(Film).filter_by(title=film.title).first()
            if not exists:
                session.add(film)
                session.commit()

    except Exception as e:
        session.rollback()
        print(f"ERROR in adding films: {e}")

    finally:
        session.close()


def get_films():
    session = SessionLocal()
    try:
        stmt = select(Film)
        result = session.execute(stmt).scalars().all()
        return result

    except Exception as e:
        print(f"ERROR in getting films: {e}")
        return []

    finally:
        session.close()


def update_film(id: int, **kwargs):
    session = SessionLocal()

    try:
        stmt = select(Film).where(Film.id == id)
        film = session.execute(stmt).scalar_one_or_none()

        if not film:
            print(f"Film with ID {id} not found.")
            return

        for key, value in kwargs.items():
            if hasattr(film, key):
                setattr(film, key, value)

        session.commit()
        print(f"\n Film with ID {id} updated successfully.")

    except Exception as e:
        session.rollback()
        print(f"ERROR in updating film: {e}")

    finally:
        session.close()


def delete_all():
    session = SessionLocal()

    try:
        stmt = delete(Film)
        session.execute(stmt)
        session.commit()

        print("\n All films deleted successfully.")

    except Exception as e:
        session.rollback()
        print(f"ERROR in deleting films: {e}")

    finally:
        session.close()
