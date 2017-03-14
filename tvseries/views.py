from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from tvseries.models import Serie,Fseires
from tvseries.serializers import Serieslizer,Addserialize,AddFollow
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class SerieViewSet(viewsets.ModelViewSet):
	queryset = Serie.objects.all().order_by('-raiting')
	serializer_class = Serieslizer

	#def update(self, request, pk=None):
	#	author = request.user.pk
	#	print(pk)
	#	requser = User.objects.get(pk=author)
	#	reqseri = Serie.objects.get(pk=int(pk))
	#	reqseri.owner.add(requser)
	#	reqseri.save()
	#	return Response(status=status.HTTP_201_CREATED)

class FollowSeries(viewsets.ModelViewSet):
	queryset = Fseires.objects.all().order_by('-id')
	serializer_class = AddFollow

	
#
#@api_view(['GET','PUT'])
#def series(request):
#	if request.method == 'GET':
#		querysets = Serie.objects.all().order_by('-raiting')
#		serializer = Serieslizer(querysets, many=True,context={'request': request})
#		return JsonResponse(serializer.data, safe=False)

#@api_view(['PUT','GET'])
#def Addseries(request,pk):
#	if request.method == 'GET':
#		querysets = Serie.objects.get(id=pk)
#		serializer = Serieslizer(querysets, many=True,context={'request': request})
#		return JsonResponse(serializer.data, safe=False)

#	if request.method == 'PUT':
#		print(request)
#		datas = {'text': request.DATA.get('seriesid'), 'author': request.user.pk}
#		requser = User.objects.get(datas.author)
#		for data in datas['text']:
#			reqseri = Serie.objects.get(data.text)
#			reqseri.owner.add(requser)
#			reqseri.save()
#		return Response(status=status.HTTP_201_CREATED)
#	return Response(status=status.HTTP_400_BAD_REQUEST)
