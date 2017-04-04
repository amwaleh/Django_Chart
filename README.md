## Django_Charts
![](https://cdn.scotch.io/15775/OQk6534nTPCqvZOaJg1I_Screen%20Shot%202017-03-20%20at%2012.42.55%20AM.png)
This Django app uses a combination of chartJS and Ajax to generate Charts.



clone this repo
```bash
 git clone git@github.com:andela-amwaleh/Django_Chart.git

```

**Create a virtualenv**
### Install dependencies
```bash
    pip install -r requirements.txt

```
### Load data into database
use fixture to load the data
- run migrations
```bash
 cd Django-Chart
 python manage.py makemigrations
 python manage.py migrate
```
- Next, load sample data by running.
```bash

$ python manage.py loaddata app_sample_data.json

```
- Start the server

```bash

$ python manage.py runserver

```

- Navigate to http://localhost:8000 in your browser
