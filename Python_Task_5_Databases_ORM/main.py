from models import Base
from database import engine
import crud


def print_films(title):
    print(f"\n--- {title} ---")
    films = crud.get_films()

    for f in films:
        print(f"{f.id} | {f.title} | {f.director} | {f.release_year}")


def main():
    Base.metadata.create_all(engine)

    crud.add_films()
    print_films("AFTER INSERT")

    crud.update_film(3, title="Interstellar 2", release_year=2026)
    print_films("AFTER UPDATE")

    crud.delete_all()


if __name__ == "__main__":
    main()
