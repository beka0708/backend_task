from django.db import models


class User(models.Model):
    """
    Абстрактно аутентифицированные пользователи
    """

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Добавить пользователя"

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    Профиль пользователя
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Добавить профиль"

    def __str__(self):
        return self.user.name


class HashTag(models.Model):
    """
    Хэштеги для всех постов
    """

    name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Хэштеги"
        verbose_name_plural = "Добавить хештег"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Пост от пользователей
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(HashTag, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Добавить пост"

    def __str__(self):
        return f'Пользователь: "{self.user}", Пост - "{self.title}"'


STARS = (
    ("*", "*"),
    ("**", "**"),
    ("***", "***"),
    ("****", "****"),
    ("*****", "*****"),
)


class Review(models.Model):
    """
    Отзывы от пользователей
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_user"
    )
    text = models.TextField()
    stars = models.CharField(max_length=100, choices=STARS)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Добавить отзыв"

    def __str__(self):
        return f'Пользователь - "{self.user}", оставил отзыв под постом - "{self.post}'
