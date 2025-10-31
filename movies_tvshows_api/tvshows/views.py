from rest_framework import viewsets, generics, mixins, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.db import models
from .models import TVShow
from .serializers import TVShowSerializer

class TVShowViewSet(viewsets.ModelViewSet):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'stars', 'year']


# 1) Function-Based Views (FBV)
def _tvshows_filtered_queryset(request):
    qs = TVShow.objects.all()
    query = request.query_params.get('search') or request.query_params.get('q')
    year = request.query_params.get('year')
    if query:
        qs = qs.filter(
            models.Q(title__icontains=query)
            | models.Q(genre__icontains=query)
            | models.Q(stars__icontains=query)
            | models.Q(short_story__icontains=query)
        )
    if year:
        qs = qs.filter(year__icontains=year)
    return qs
@api_view(['GET', 'POST'])
def tvshows_fbv_list(request):
    if request.method == 'GET':
        tvshows = _tvshows_filtered_queryset(request)
        serializer = TVShowSerializer(tvshows, many=True)
        return Response(serializer.data)
    serializer = TVShowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tvshows_fbv_detail(request, pk):
    try:
        tvshow = TVShow.objects.get(pk=pk)
    except TVShow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TVShowSerializer(tvshow)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TVShowSerializer(tvshow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    tvshow.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 2) Class-Based Views (APIView)
class TVShowsCBVList(APIView):
    def get(self, request):
        tvshows = _tvshows_filtered_queryset(request)
        serializer = TVShowSerializer(tvshows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TVShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TVShowsCBVDetail(APIView):
    def get_object(self, pk):
        try:
            return TVShow.objects.get(pk=pk)
        except TVShow.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tvshow = self.get_object(pk)
        serializer = TVShowSerializer(tvshow)
        return Response(serializer.data)

    def put(self, request, pk):
        tvshow = self.get_object(pk)
        serializer = TVShowSerializer(tvshow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tvshow = self.get_object(pk)
        tvshow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3) Mixins
class TVShowsMixinsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = TVShowSerializer

    def get_queryset(self):
        return _tvshows_filtered_queryset(self.request)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TVShowsMixinsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


# 4) Generics
class TVShowsGenericsList(generics.ListCreateAPIView):
    serializer_class = TVShowSerializer

    def get_queryset(self):
        return _tvshows_filtered_queryset(self.request)


class TVShowsGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
