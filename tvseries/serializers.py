from tvseries.models import Serie
from rest_framework import serializers


#class Serieslizers(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Serie
#        fields = ('url','title', 'language', 'imdblink','raiting' )

class Serieslizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ('url','title', 'language', 'imdblink','raiting', 'owner' )



class Addserialize(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)