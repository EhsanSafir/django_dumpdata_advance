 Django Advance Dumpdata
===================
Django Manage Command like  ``dumpdata`` but with have more feature to  Output the contents of the database from given fields of a model
and filter that data using standard Django lookups for filtering.
data  can be export with divers format like json,xml,yaml.exported structure is compatible with Django ``dumpdata`` structure which
allows you to use standard ``loaddata`` command for import.

Installation
------------

To get the latest stable release from PyPi

    pip install django-advance-dumpdata


Add ``advance_dumpdata`` to your ``INSTALLED_APPS``

    INSTALLED_APPS = (
        ...,
        "django_dumpdata_one",
    )
Usage
-----

Export data:



    ./manage.py dumpdata_one app_name.model_name --fields=field1,field2 > dump_file.json


Import data:


   ` ./manage.py loaddata dump_file.json`