from django.db import models

# Create your models here.


class User(models.Model):
    #id = models.IntegerField(label='ID', read_only=True)
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)
    
    __str__ = __repr__  # __str__にも同じ関数を適用


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, models.CASCADE, related_name='entries')

    def __repr__(self):
        return "{}: {}".format(self.pk, self.title)

    __str__ = __repr__
    
