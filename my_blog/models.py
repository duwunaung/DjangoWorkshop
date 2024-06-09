from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    nickname = models.CharField(max_length=50)
    createddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.nickname})"

class Blog(models.Model):

    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES_STATUS = (
        (ACTIVE, "Active"),
        (DRAFT, "Draft")
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, name="author", on_delete=models.CASCADE)
    preview = models.TextField()
    image = models.ImageField(upload_to="uploads/")
    content = models.TextField()
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    createddate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)

class About(models.Model):
    image = models.ImageField(upload_to="uploads/")
    content = models.TextField()

    def __str__(self):
        return self.content
    

    class Meta:
        verbose_name_plural = "About"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    createddate = models.DateTimeField(auto_now_add=True)

