from peewee import (
    SqliteDatabase, PrimaryKeyField, CharField, BigIntegerField, Model
)

db = SqliteDatabase('rg.db')


class Form(Model):
    id = PrimaryKeyField()
    name = CharField()
    phone = BigIntegerField()
    age = CharField()
    category = CharField()
    job = CharField()
    motivation = CharField()
    sex = CharField()

    class Meta:
        database = db


db.create_tables([Form])
