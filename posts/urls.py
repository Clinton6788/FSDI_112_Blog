from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("my_posts/", views.UserPostListView.as_view(), name = "user_post"),
    path("published/", views.PublishedPostListView.as_view(), name = "published"),
    path("archived/", views.ArchivedPostListView.as_view(), name = "archived"),
    path("my_archived/", views.UserArchivedPostListView.as_view(), name = "user_archived"),
    path("drafts/", views.DraftPostListView.as_view(), name="draft"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete"),
]