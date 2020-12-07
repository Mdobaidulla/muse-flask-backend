from peewee import *
import datetime
DATABASE = PostgresqlDatabase('flask_music_app', host='localhost', port=5432)
class Song(Model):
    title = CharField()
    artist = CharField()
    album = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("The TABLE IS Created!!!!")
    DATABASE.close()