import os

from setuptools import find_packages, setup

setup(
    name="django-advance-dumpdata",
    zip_safe=False,
    version="0.0.1",
    description="Django Manage Command; Output the contents of the database"
                " as a fixture of the given format,filter and more features ",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    long_description_content_type="text/markdown",
    author="Ehsan Safir , Sayed Farid Qattali",
    author_email="EhsanSafir@outlook.com , eng.faridqattali@gmail.com ",
    url="https://github.com/EhsanSafir/django_dumpdata_advance",
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=["Django>=2.2"]
)
