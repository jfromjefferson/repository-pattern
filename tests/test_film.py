from mocks.film_mock import MockFilmRepository


def test_get_film():
    film_repository = MockFilmRepository()
    film_dict = {
        "film_id": 3,
        "title": "Adaptation Holes",
        "description": "A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory",
        "release_year": 2006,
        "language_id": 1,
        "rental_duration": 7,
        "rental_rate": 2.99,
        "length": 50,
        "replacement_cost": 18.99,
        "rating": "NC-17",
        "last_update": "2013-05-26T14:50:58.951000",
        "special_features": [
            "Trailers",
            "Deleted Scenes"
        ],
        "fulltext": "'adapt':1 'astound':4 'baloon':19 'car':11 'factori':20 'hole':2 'lumberjack':8,16 'must':13 'reflect':5 'sink':14"
    }
    film_repository.add(**film_dict)

    assert film_repository.get(0) is not None
    assert film_repository.get(1) is None


def test_get_all():
    film_repository = MockFilmRepository()
    film_dict = {
        "film_id": 3,
        "title": "Adaptation Holes",
        "description": "A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory",
        "release_year": 2006,
        "language_id": 1,
        "rental_duration": 7,
        "rental_rate": 2.99,
        "length": 50,
        "replacement_cost": 18.99,
        "rating": "NC-17",
        "last_update": "2013-05-26T14:50:58.951000",
        "special_features": [
            "Trailers",
            "Deleted Scenes"
        ],
        "fulltext": "'adapt':1 'astound':4 'baloon':19 'car':11 'factori':20 'hole':2 'lumberjack':8,16 'must':13 'reflect':5 'sink':14"
    }

    film_repository.add(**film_dict)
    film_repository.add(**film_dict)
    film_repository.add(**film_dict)

    assert len(film_repository.get_all()) == 3


def test_delete():
    film_repository = MockFilmRepository()
    film_dict = {
        "film_id": 3,
        "title": "Adaptation Holes",
        "description": "A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory",
        "release_year": 2006,
        "language_id": 1,
        "rental_duration": 7,
        "rental_rate": 2.99,
        "length": 50,
        "replacement_cost": 18.99,
        "rating": "NC-17",
        "last_update": "2013-05-26T14:50:58.951000",
        "special_features": [
            "Trailers",
            "Deleted Scenes"
        ],
        "fulltext": "'adapt':1 'astound':4 'baloon':19 'car':11 'factori':20 'hole':2 'lumberjack':8,16 'must':13 'reflect':5 'sink':14"
    }

    film_repository.add(**film_dict)
    film_repository.add(**film_dict)

    film_repository.delete(1)

    assert len(film_repository.get_all()) == 1
