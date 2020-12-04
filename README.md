# Djano-Anti-Crawler
A light weight anti crawler Django app which blocks the IP addresses which sends too many hits to your application.
You can decide the number of hits that are allowed per IP address in defined time.

Quick start
-----------

1. Add `django_anti_crawler` to your INSTALLED_APPS setting like this::
    
    ```
    INSTALLED_APPS = [
        ...
        'django_anti_crawler',
    ]
    ```

2. Add `'DjangoAntiCrawlerMiddleware'` to your middleware classes in `settings.py` file::

    ```
    MIDDLEWARE = [
        'django_anti_crawler.middlewares.DjangoAntiCrawlerMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```

    `DjangoAntiCrawlerMiddleware` can be and should be first middleware as we need to make sure IP check is the very first
    thing in processing request.


3. If cache settings are not defined in your settings.py file, then you need to add below lines to your settings.py file::

    ```
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table',
        }
    }
    ```

   Make sure you have database settings configured. Run the below command to create cache_table in database::
    
    ```
    python manage.py createcachetable
    ```

   You may choose whatever cache backend you want to use.


4. (optional) Set variables in MAX_ALLOWED_HITS_PER_IP and IP_HITS_TIMEOUT in settings.py file::

    MAX_ALLOWED_HITS_PER_IP = 2000  # max allowed hits per IP_TIMEOUT time from an IP. Default 2000.
    IP_HITS_TIMEOUT = 60  # timeout in seconds for IP in cache. Default 60.

   To test on local system, set these values to very low, e.g. IP_HITS_TIMEOUT = 30 and MAX_ALLOWED_HITS_PER_IP = 2.
   Restart the server and send requests frequently. After two requests you will start receiving 403 error.
   If not defined in settings file, default values will be used.

## Authors

* **Muhammad Haseeb** - *Initial work* - [Muhammad Haseeb](https://github.com/iam-mhaseeb)

## Licensing
The project is [MIT Licenced](LICENSE).

