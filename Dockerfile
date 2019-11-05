FROM django
ADD . /notes

RUN pip install pip --upgrade &&\
    pip install django --upgrade

RUN pip install -r /notes/notes/requirements.txt &&\
    python /notes/notes/manage.py migrate

CMD ["python", "notes/notes/manage.py", "runserver", "0.0.0.0:8000"]
