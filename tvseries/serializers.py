from tvseries.models import Serie,Fseires
from rest_framework import serializers


class AddFollow(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fseires
        fields = ('url','seriesname', 'followuser' )

class Serieslizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ('url','title', 'language', 'imdblink','raiting', 'owner' )



class Addserialize(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)