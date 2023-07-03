from rest_framework import serializers
from .models import BookModel, AuthorModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id','name', 'fname', 'date_of_birth')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'author', 'name', 'page', 'price')


