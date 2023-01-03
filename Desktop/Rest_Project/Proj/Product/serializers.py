from rest_framework import serializers

from Product.models import Product, Category, Likes, Favourite, Comments
from User.serializers import UserSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ("id", "elements",  "category", "user")
        # exclude = ("id",)

    # def to_internal_value(self, data):
    #     print("from internal value", data)
    #     return super().to_internal_value(data)
    #
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = data.pop("user")
        data["user"] = UserSerializer(user).data

        return data
#
# class ProductModelSerializer(serializers.ModelSeralizer):
#     class Meta:
#         model = Category
#         fields = "__all__"
#
#
# class LikesModelSerializer(serializers.ModelSeralizer):
#     pass
#
#
# class CommentsModelSerializer(serializers.ModelSeralizer):
#     pass
#