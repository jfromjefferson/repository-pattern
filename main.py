from fastapi import FastAPI, Query, Path, HTTPException

from repositories.film_repository import FilmRepository

app = FastAPI()

film_repository = FilmRepository()

@app.get('/films')
async def get_films(page: int = Query(gt=0, default=1), limit: int = Query(lt=101, default=100)):
    offset = (page - 1) * limit
    film_list = film_repository.get_all(limit=limit, offset=offset)

    return {
        'data': film_list
    }

@app.get('/films/{film_id}')
async def get_film(film_id: int = Path(gt=0)):
    film = film_repository.get(id=film_id)

    if not film:
        raise HTTPException(status_code=404)

    return {
        'data': film
    }

@app.delete('/films/{film_id}')
async def delete_film(film_id: int = Path(gt=0)):
    success = film_repository.delete(id=film_id)

    if success:
        return {
            'data': 'Film deleted successfully'
        }

    raise HTTPException(status_code=404)
