python3 manage.py dumpdata > datadump.json
python manage.py makemigrations
python manage.py migrate

Run this on Django shell to exclude contentype data

python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
Finally:

python3 manage.py loaddata datadump.json
