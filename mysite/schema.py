import graphene
from mysite.blog import schema


class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
