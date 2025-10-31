from django.urls import path, include
from .views import (
    tvshows_fbv_list,
    tvshows_fbv_detail,
    TVShowsCBVList,
    TVShowsCBVDetail,
    TVShowsMixinsList,
    TVShowsMixinsDetail,
    TVShowsGenericsList,
    TVShowsGenericsDetail,
)

urlpatterns = [
    # FBV
    path('fbv/tvshows/', tvshows_fbv_list, name='tvshows-fbv-list'),
    path('fbv/tvshows/<int:pk>/', tvshows_fbv_detail, name='tvshows-fbv-detail'),

    # CBV (APIView)
    path('cbv/tvshows/', TVShowsCBVList.as_view(), name='tvshows-cbv-list'),
    path('cbv/tvshows/<int:pk>/', TVShowsCBVDetail.as_view(), name='tvshows-cbv-detail'),

    # Mixins
    path('mixins/tvshows/', TVShowsMixinsList.as_view(), name='tvshows-mixins-list'),
    path('mixins/tvshows/<int:pk>/', TVShowsMixinsDetail.as_view(), name='tvshows-mixins-detail'),

    # Generics
    path('generics/tvshows/', TVShowsGenericsList.as_view(), name='tvshows-generics-list'),
    path('generics/tvshows/<int:pk>/', TVShowsGenericsDetail.as_view(), name='tvshows-generics-detail'),
]
