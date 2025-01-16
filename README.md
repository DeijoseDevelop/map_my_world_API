# Map My World API

## Description

Map My World is a REST API built with FastAPI that allows users to explore and review different locations and categories around the world. The application offers an interactive map where users can discover new locations and receive recommendations based on specific categories such as restaurants, parks and museums.

## Main features

- Geographic location management with coordinates (latitude/longitude)
- Location categorization system
- Review system for locations and categories
- Intelligent recommender that suggests places not recently reviewed

## Technologies Used

- Python 3.10+
- FastAPI
- SQLModel (ORM)
- Poetry
- SQL Lite
- Pydantic for data validation
- Uvicorn as ASGI server

## API Endpoints

### Location

- `GET /locations`: Get list of locations
- `POST /locations`: Create new location

### Category

- `GET /categories`: Get list of categories
- `POST /categories`: Create new category

### Recommendations

- `GET /recommendations`: Get 10 recommendations of locations-categories not reviewed in the last 30 days

## Installation and Configuration

1. Clone repository:

```bash
git clone https://github.com/DeijoseDevelop/map-my-world.git
cd map-my-world
```

2. Create and activate virtual environment:

```bash
pip install -r requirements.txt
```

3. Execute application:

```bash
uvicorn app.main:app --reload
```

## Documentation API

Once the server is running, you can access:

- Swagger UI Documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Using the Recommender

The recommender system prioritizes:

1. locations that have never been reviewed 2.
2. Locations that have not been reviewed in the last 30 days.
3. Returns maximum 10 recommendations per query.

Sample response:

```json
{
  "recommendations": [
    {
      "location_id": 10,
      "category_id": 30,
      "last_reviewed": null,
      "location": {
        "latitude": 40.7128,
        "longitude": -74.006
      },
      "category": {
        "name": "Restaurante",
        "description": "Establecimiento gastronómico"
      }
    }
  ]
}
```