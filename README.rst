 Django Advance Dumpdata
========================

Django Manage Command like  ``dumpdata`` but with have more feature to  Output the contents of the database from given fields of a model
and filter that data using standard Django lookups for filtering.
data  can be export with divers format like json,xml,yaml.exported structure is compatible with Django ``dumpdata`` structure which
allows you to use standard ``loaddata`` command for import.
xx

Installation
------------

To get the latest stable release from PyPi


    pip install django-dumpdata-advance


Add ``dumpdata_advance`` to your ``INSTALLED_APPS``


    INSTALLED_APPS = (
        ...,
        "django_dumpdata_advance",
    )

Usage
-----

Export data:



    ./manage.py dumpdata_one app_name.model_name --fields=field1,field2 > dump_file.json


Import data:



    ./manage.py loaddata dump_file.json


How to use filters? If you not familiar take a look at Django Field
lookups - https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups



    ./manage.py dumpdata_one app_name.model_name --fields=field1 --filter=name__icontains=django

    ./manage.py dumpdata_one app_name.model_name --fields=field1 --filter=name__icontains=django,pk__gt=300

Set order by:



    ./manage.py dumpdata_advance app_name.model_name --fields=field1,field2 --order=field2,field2

Export all fields:



    ./manage.py dumpdata_advance app_name.model_name --fields=*


Exclude custom fields:



    ./manage.py dumpdata_advance app_name.model_name --exclude_fields=name



Limit number of exported records:



    ./manage.py dumpdata_advance app_name.model_name --fields=* --limit=10


Export full file URL:



    ./manage.py dumpdata_advance app_name.model_name --fields=image --full_url=image


Export from another database than 'default':



    ./manage.py dumpdata_advance app_name.model_name --database=other_database