from django.urls import path

from . import views


# url patterns to include later in main urls module
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number), # if this path input can be converted to an int, then execute views.monthly...by_number, if not ignore
    path("<str:month>", views.monthly_challenge, name="month-challenge") # <> angles brackets create variable; ':' defines the data type
]
