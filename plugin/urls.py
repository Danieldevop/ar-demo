from django.urls import path
from plugin.views import ShowScenarioView

urlpatterns = [
    path('', ShowScenarioView.as_view(), name='show-plugin-scenario'),

]
