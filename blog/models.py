import datetime

from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User


class PostBase(models.Model):
    CATEGORY_CHOICES = [
        ('Rowery miejskie', 'Rowery miejskie'),  # City Bikes
        ('Rowery górskie', 'Rowery górskie'),  # Mountain Bikes
        ('Rowery szosowe', 'Rowery szosowe'),  # Road Bikes
        ('Rowery trekkingowe', 'Rowery trekkingowe'),  # Trekking Bikes
        ('Akcesoria rowerowe', 'Akcesoria rowerowe'),
        ('Rowery torowe', 'Rowery torowe'),  # Track Bikes
        ('Wyprawy rowerowe', 'Wyprawy rowerowe'),  # Bike Trips
        ('Serwis i konserwacja', 'Serwis i konserwacja'),  # Service and Repair
        ('Porady dla początkujących', 'Porady dla początkujących'),  # Tips for Beginners
        ('Sprzęt rowerowy', 'Sprzęt rowerowy'),  # Bike Gear
        ('Zdrowie i kondycja', 'Zdrowie i kondycja'),  # Health and Fitness
        ('Inne', 'Inne'),  # Other
        ('Dieta i suplementy', 'Dieta i suplementy'),  # Diet and Supplements
        # Add more categories as needed
    ]
    title = models.CharField(max_length=127)
    # category = models.CharField(max_length=127, default='Ogólne')
    category = models.CharField(max_length=127, choices=CATEGORY_CHOICES, default='Inne')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True


class Post2(PostBase):
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', default='post_images/fixed.png')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title


class Topic(PostBase):
    description = models.TextField()

    def __str__(self):
        return self.title


class CommentBase(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class Comment(CommentBase):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, default=1)


class PostComment(CommentBase):
    post = models.ForeignKey('Post2', on_delete=models.CASCADE, default=1)
