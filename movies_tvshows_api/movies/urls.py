from django.urls import path, include
from .views import (
    movies_fbv_list,
    movies_fbv_detail,
    MoviesCBVList,
    MoviesCBVDetail,
    MoviesMixinsList,
    MoviesMixinsDetail,
    MoviesGenericsList,
    MoviesGenericsDetail,
)

urlpatterns = [
    # FBV
    path('fbv/movies/', movies_fbv_list, name='movies-fbv-list'),
    path('fbv/movies/<int:pk>/', movies_fbv_detail, name='movies-fbv-detail'),

    # CBV (APIView)
    path('cbv/movies/', MoviesCBVList.as_view(), name='movies-cbv-list'),
    path('cbv/movies/<int:pk>/', MoviesCBVDetail.as_view(), name='movies-cbv-detail'),

    # Mixins
    path('mixins/movies/', MoviesMixinsList.as_view(), name='movies-mixins-list'),
    path('mixins/movies/<int:pk>/', MoviesMixinsDetail.as_view(), name='movies-mixins-detail'),

    # Generics
    path('generics/movies/', MoviesGenericsList.as_view(), name='movies-generics-list'),
    path('generics/movies/<int:pk>/', MoviesGenericsDetail.as_view(), name='movies-generics-detail'),
]
