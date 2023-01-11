from rest_framework import serializers
from blog.models import Blog, Category


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ("updated_at", "author")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["count"] = instance.blogs.count()
        return representation
