Django-MySQL-Example
=========

A simple example, based on Python3 and MySQL, upload and show multimedia, like musics, pictures or videos.

Getting started
----------------
1.Change the default DATABASES in setting.py:
```python
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'Schema name in DataBase',
    'USER':'root',
    'PASSWORD':'Database password',
    'HOST':'127.0.0.1',
    'PORT':'3306'
    }
}
```
2.Start Django Server:
```python
python manage.py runserver
```
3.View the webside:
```bash
http://127.0.0.1:8000/upload
http://127.0.0.1:8000/artupload
http://127.0.0.1:8000/musupload
http://127.0.0.1:8000/vidupload
```
These three URLs are upload multimedia.

```bash
http://127.0.0.1:8000/show/
```
This URL can show every thing which you upload.
