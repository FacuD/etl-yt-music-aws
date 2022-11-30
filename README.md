# YT Music ETL AWS Lambda
This POC extract data from the YouTube Music API, transform the data filtering only the songs listened today and load it to a PostgreSQL database hosting service. All of this is done automatically by a AWS Lambda function created through a dockerfile.

## Inspired on
[Ejemplo de ETL con Spotify y Python](https://www.youtube.com/watch?v=eg8t2-E69ew&ab_channel=CodinEric)

## Extract
I used the [YouTube Music API](https://ytmusicapi.readthedocs.io/en/stable/) to extract the data. The API is not public, so you need to have a valid token to use it.

## Transform
I used the [Pandas](https://pandas.pydata.org/) library to transform the data. I filtered the data to get only the songs listened today.

## Load
I used the [Psycopg2](https://pypi.org/project/psycopg2/) library to load the data to a PostgreSQL database. I used a database hosting service called [ElephantSQL](https://www.elephantsql.com/).

### TODO

- [x] Use PostgreSQL hosting service
- [x] Make this to upload every day with lambda function using docker and cron
- [x] Fix docker image directory structure
- [ ] Fix inserted_at date (GMT -3)
- [ ] Implement Airflow (?)
