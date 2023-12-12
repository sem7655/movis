from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
# Абстрактные модели
class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):#Жанры
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)


    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.name

class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=150)

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _("Person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return self.full_name



class Filmwork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    creation_date = models.DateField(_('creation_date'), blank=True, null=True)
    rating = models.FloatField(_('rating'), blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    #certificate = models.CharField(_('certificate'), max_length=512, blank=True)
    #file_path = models.FileField(_('file'), blank=True, null=True, upload_to='movies/')
    class FilmWorkType(models.TextChoices):
        MOVIE = _('movie')
        TV_SHOW = _('tv_show')
    type = models.CharField(_('type'), choices=FilmWorkType.choices, blank=True)
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    persons = models.ManyToManyField(Person, through='PersonFilmwork')



    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _("Film")
        verbose_name_plural = _("Films")

    def __str__(self):
        return self.title
class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(_('role'), null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _("Person Filmwork")
        verbose_name_plural = _("PersonFilmWork_verbose_name_plural")
class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _("GenreFilmwork")
        verbose_name_plural = _("GenreFilmwork_verbose_name_plural")