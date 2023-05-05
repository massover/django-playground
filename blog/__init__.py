import os


def init():
    import django
    from django.core.management import call_command
    from django.conf import settings
    from django.utils.crypto import get_random_string

    settings.configure(
        DEBUG=True,
        ALLOWED_HOSTS=["*"],
        ROOT_URLCONF=__name__,
        SECRET_KEY=get_random_string(50),
        INSTALLED_APPS=["blog"],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
    )

    django.setup()

    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    call_command("migrate", run_syncdb=True, verbosity=0)
