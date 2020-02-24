import graphene

import ingredients.schema as ing_schema

class Query(ing_schema.Query, graphene.ObjectType):
    #This Class wil inherit from multiple Queries
    #as we begin to add more apps to the project 
    pass
schema =graphene.Schema(query=Query)