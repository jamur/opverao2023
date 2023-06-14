from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index),
    path('cadestagiarios', views.index),
    path('valores/', views.valores),
    path('nomes/', views.nomes),
    path('telefones/', views.telefones),
    path('falta_pagamento/', views.falta_pagamento),
    path('falta_pagamento_texto/', views.falta_pagamento_texto),
    path('falta_pagamento_texto_so_valor/', views.falta_pagamento_texto_so_valor),
    path('avaliacao/',views.avaliacao),
]
