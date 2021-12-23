
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

To change the interval of fetching videos, change it in CELERY_BEAT_SCHEDULE in settings.py

Developed on Windows 7, tested on Windows 7, 10 and Ubuntu 20.04
## Deployment

Please follow the following steps:
1. Clone the repository.
```bash
git clone https://github.com/Swanand01/externship.git
```
2. Go to the cloned repository
```bash
cd externship\
```
3. Create a virtual environment.
- Windows and Linux instructions [here](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
4. Activate the venv
- Windows and Linux instructions [here](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
5. Install the necessary dependencies
- Install [Redis](https://redis.io/download)
- Install necessary python packages:
    ```bash
     pip install -r requirements.txt
    ```
6. Start Redis server
7. Migrate changes and run the django server.
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
8. Open a new terminal in the cloned directory,
- Activate the virtual env
- Start the celery worker process
    - Windows: 
    ```bash
    celery -A backend_submission worker --pool=solo -l INFO
    ```
    - For Linux:
    ```bash
    celery -A backend_submission worker -l INFO
    ```
9. Open another terminal in the same directory,
- Activate the virtual env
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

