# -*- coding: utf 8 -*-
from django.db import models
from django.conf import settings
from django_extensions.db.fields import RandomCharField


REGION = (
    ('0', " "),
    ('1', "Sao Paulo"),
    ('2', "Rio de Janeiro"),
)

COUNTRY= (
    ('0', " "),
    ('1', "Brasil"),
)