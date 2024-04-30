from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='page_main_quality_control'),
    # path('', views.IndexView.as_view(), name='page_main_quality_control'),
    path('bugs/', include([
        path('', views.bug_list, name='page_bugs'),
        # path('<int:bug_id>/', views.BugDetailView.as_view(), name='page_bug_detail')
        path('<int:bug_id>', views.bug_detail, name='page_bug_detail')
    ])),
    path('features/', include([
        path('', views.feature_list, name='page_features'),
        # path('<int:feature_id>/', views.FeatureIdDetailView.as_view(), name='page_feature_detail')
        path('<int:feature_id>/', views.feature_id_detail, name='page_feature_detail')
    ])),
    # path('bugreport/new/', views.create_bugreport, name='create_bugreport'),
    # path('feature/new/', views.create_feature, name='create_feature'),
    # path('bugs/<int:bug_id>/update/', views.update_bugreport, name='update_bugreport'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bugreport, name='delete_bugreport'),
    # path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('bugreport/new/', views.BugReportCreateView.as_view(), name='create_bugreport'),
    path('feature/new/', views.FeatureCreateView.as_view(), name='create_feature'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bugreport'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bugreport'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
