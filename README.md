# Running the app

Clone this repo and enter the root dir.
For the app to peoperly work, you first have to place the `.env` file (sent separately) in the root dir of this repo.
Then, inside the root dir, run

```bash
docker-compose build
docker-compose up
```

When the console shows uvicorn's message that the server is running, you can enter [the graphic interface](http://0.0.0.0:8000/docs) of the server where you will find all 5 routes:
* Create book record
* Get book record by ID
* Get all book records
* Update book record
* Delete book record by ID

This interface is interactive and will let you test out the different routes with your own data.
