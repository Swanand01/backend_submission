
# Backend Assignment

## Project goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.


## Features

- Periodic task to constantly fetch data in the background every minute
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- Dashboard to access the videos with options to filter and search


## How it works

A periodic task is run in the background at an interval, which can be changed from the Django admin panel.
This task fetches videos with the keyword "cricket" using the YouTube Data V3 API. New videos are saved in the database, in the Video model.



##

You will need a YouTube Data API key in order to run this app. Follow the instructions on this page to get one.

In case of multiple API keys, provide them as
```python
api_keys = [key_1, key_2,...]
```
in core\tasks.py
## Deployment

Please follow the following steps:
1. Clone the repository.
```bash
git clone https://github.com/Swanand01/externship.git
```
2. Create a virtual environment. 
```bash
py -m venv venv
```
3. Activate the venv
```bash
venv\Scripts\activate.bat
```
4. Install the necessary dependencies
- Install Redis
- Install python packages:
    ```bash
    pip install django djangorestframework redis celery django-celery-beat
    ```
    ```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
5. Start Redis server and Redis client
6. Go to the cloned repository
```bash
cd externship\
```
7. Run the django server.
```bash
python manage.py runserver
```
8. In a new terminal,
- Activate the virtual env
- Go inside the repo directory
    ```bash
    cd externship\
- Start the celery worker process
    ```bash
    celery -A backend_submission worker --pool=solo -l INFO
    ```
9. In another terminal,
- Activate the virtual env
- Go inside the repo directory
    ```bash
    cd externship\
    ```
- Start the celery beat scheduler
    ```bash
    celery -A backend_submission beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```

The project should now be running at localhost:8000.\
To access the dashboard visit localhost:8000/dashboard\
To access the API visit localhost:8000/api/videos

## Tech Stack

Django,\
Django Rest Framework (For the API endpoint),\
Celery (Task queue),\
Celery-Beat (Periodic Task Scheduler),\
Redis (As the message broker and celery result backend),



## API Reference

```http
  GET /api/videos
```
#### Returns the stored video data in a paginated response sorted in descending order of published datetime.

## Authors

- [@Swanand01](https://www.github.com/Swanand01)

