from django.db import models

class User(models.Model):
    username = models.CharField(verbose_name='имя пользователя', max_length=50, unique=True)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    password_hash = models.CharField(verbose_name='хэш пароля', max_length=255)
    avatar = models.URLField(verbose_name='аватар', blank=True, null=True)
    registration_date = models.DateField(verbose_name='дата регистрации', auto_now_add=True)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["email"])
        ]

    def __str__(self):
        return self.username

class Artist(models.Model):
    name = models.CharField(verbose_name='имя артиста', max_length=100)
    bio = models.TextField(verbose_name='биография', blank=True, null=True)
    verified = models.BooleanField(verbose_name='верифицирован', default=False)
    photo_url = models.URLField(verbose_name='фото', blank=True, null=True)
    total_listens = models.IntegerField(verbose_name='всего прослушиваний', default=0)
    
    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name

class Album(models.Model):
    ALBUM_TYPES = [
        ('album', 'Альбом'),
        ('ep', 'EP'),
        ('single', 'Сингл')
    ]
    
    title = models.CharField(verbose_name='название альбома', max_length=200)
    artist = models.ForeignKey(Artist, verbose_name='артист', on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name='дата выпуска')
    cover_url = models.URLField(verbose_name='обложка', blank=True, null=True)
    album_type = models.CharField(verbose_name='тип альбома', max_length=10, choices=ALBUM_TYPES)
    genre = models.CharField(verbose_name='жанр', max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ["-release_date", "title"]
        indexes = [
            models.Index(fields=["artist", "release_date"])
        ]

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(verbose_name='название трека', max_length=200)
    main_artist = models.ForeignKey(Artist, verbose_name='основной артист', on_delete=models.CASCADE)
    featured_artists = models.ManyToManyField(Artist, verbose_name='участвующие артисты',related_name='featured_tracks', blank=True)
    album = models.ForeignKey(Album, verbose_name='альбом', on_delete=models.SET_NULL, blank=True, null=True)
    duration = models.IntegerField(verbose_name='длительность (секунды)')
    listens_count = models.IntegerField(verbose_name='количество прослушиваний', default=0)
    created_at = models.DateField(verbose_name='дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
        ordering = ["album"]
        indexes = [
            models.Index(fields=["main_artist", "listens_count"]),
            models.Index(fields=["album"])
        ]

    def __str__(self):
        return self.title

class ListeningHistory(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, verbose_name='трек', on_delete=models.CASCADE)
    listened_at = models.DateField(verbose_name='время прослушивания', auto_now_add=True)
    playback_duration = models.IntegerField(verbose_name='длительность прослушивания')
    
    class Meta:
        verbose_name = "История прослушиваний"
        verbose_name_plural = "История прослушиваний"
        ordering = ["-listened_at"]
        indexes = [
            models.Index(fields=["user", "listened_at"])
        ]

class UserFavorite(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, verbose_name='трек', on_delete=models.CASCADE, blank=True, null=True)
    artist = models.ForeignKey(Artist, verbose_name='артист', on_delete=models.CASCADE, blank=True, null=True)
    added_at = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        ordering = ["user"]


def __str__(self):
    if self.track:
        return f"{self.user.username} - {self.track.title}"
    else:
        return f"{self.user.username} - {self.artist.name}"