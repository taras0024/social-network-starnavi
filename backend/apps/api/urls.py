from django.urls import include, path

urlpatterns = [
    path('users/', include('api.users.urls')),
    path('articles/', include('api.articles.urls')),
    path('analytics/', include('api.analytics.urls')),
]
