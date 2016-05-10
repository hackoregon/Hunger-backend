from django.db import models


class Foo(models.Model):
    class Meta:
        db_table = "foo"
