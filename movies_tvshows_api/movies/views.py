from rest_framework import viewsets, generics, mixins, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.db import models
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'director', 'genre', 'year']


# 1) Function-Based Views (FBV)
def _movies_filtered_queryset(request):
    qs = Movie.objects.all()
    query = request.query_params.get('search') or request.query_params.get('q')
    year = request.query_params.get('year')
    if query:
        qs = qs.filter(
            models.Q(title__icontains=query)
            | models.Q(genre__icontains=query)
            | models.Q(director__icontains=query)
            | models.Q(actors__icontains=query)
            | models.Q(plot__icontains=query)
        )
    if year:
        qs = qs.filter(year=year)
    return qs
    
@api_view(['GET', 'POST'])
def movies_fbv_list(request):
    if request.method == 'GET':
        movies = _movies_filtered_queryset(request)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_fbv_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 2) Class-Based Views (APIView)
class MoviesCBVList(APIView):
    def get(self, request):
        movies = _movies_filtered_queryset(request)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesCBVDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3) Mixins
class MoviesMixinsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return _movies_filtered_queryset(self.request)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class MoviesMixinsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


# 4) Generics
class MoviesGenericsList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return _movies_filtered_queryset(self.request)


class MoviesGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
