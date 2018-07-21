from django.urls import path, re_path
from todoapp.auth import *
from todoapp.classbasedviews import *
from todoapp.apiviews import *

app_name = "todoapp"

urlpatterns = [
    path("list/", Todolistview.as_view(), name="list"),
    path("list/add/", CreateList.as_view(), name="create_list"),
    path("list/<int:pk>/edit", Editlist.as_view(), name="edit_list"),
    path("list/<int:pk>/delete", DeleteList.as_view(), name="delete_list"),
    path("apilist/", dislay),
    path("apilistmodify/<int:pk>/", modification_detail),
    path("signup/", Signupclass.as_view(), name="signup"),
    path("login/", LoginClass.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
