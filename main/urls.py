from django.urls import path
from main.views import (
    show_main,
    show_xml,
    show_json,
    create_product,
    edit_product,
    delete_product,
    show_xml_by_id,
    show_json_by_id,
    login_user,
    logout_user,
    register,
    create_product_ajax,
    create_mood_flutter,

)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("create/", create_product, name="create_product"),
    path('create-ajax/', create_product_ajax, name='create_ajax'),
    path("edit/<uuid:id>/", edit_product, name="edit_product"),
    path("delete/<uuid:id>/", delete_product, name="delete_product"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register, name="register"),
    path("xml/<uuid:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", show_json_by_id, name="show_json_by_id"),
    path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),
    
]
