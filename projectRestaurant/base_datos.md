>pip install mysqlclient

-----------------------------------------------------
configuramos el DataBases del projecto <settings.py>:

            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME':'misterrestaurant',
                    'USER': 'root',
                    'PASSWORD': '',
                    'HOST':'127.0.0.1',
                    'PORT':'3306',
                }
            }
------------------------------------------------------------
lo que hacemos ahora es añadir mas tablas en mi <models.py>.
