from django.urls import path
from plugin.views import ShowScenarioView

urlpatterns = [
    path('plugin/demo', ShowScenarioView.as_view(), name='show-plugin-scenario'),

]
