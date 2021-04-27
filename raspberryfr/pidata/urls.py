from django.urls import path

# from raspberryfr.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

from raspberryfr.pidata.views import (
    receber_dados,
    visualizar_dados
)

app_name = "pidata"
urlpatterns = [
    path("receber-dados/", view=receber_dados, name="receber_dados"),
    path("visualizar-dados/", view=visualizar_dados, name="visualizar_dados"),
]
