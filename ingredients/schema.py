import graphene 
from graphene_django.types import DjangoObjectType
from .models import Category , Ingredients

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
    
class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredients

class Query(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientsType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_all_ingredients(self, info, **kwargs):
        #We can easily optimize query count in the resolve Method
        return Ingredients.objects.select_related('category').all()