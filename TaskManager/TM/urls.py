from django.conf.urls import url
from django.urls import path
from TM.views import LoginView, RegisterView, DashboardView, CreateTeamView, logout_view, TeamView, ProfileView, SpecificTeamView, CreateTaskView, TasksView, DeleteTeam, MembersView, TeamSettingsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name="register"),
    path('', DashboardView.as_view(), name="dashboard"),
    path('create-team/', CreateTeamView.as_view(), name="create-team"),
    path('logout/', logout_view, name="logout"),
    path('teams/', TeamView.as_view(), name="team"),
    url(r'^profile\/.*$', ProfileView.as_view(), name="profile"),
    url(r'^team\/[a-zA-z0-9]+\/dashboard\/$', SpecificTeamView.as_view(), name="team"),    
    url(r'^team\/[a-zA-z0-9]+\/create-task\/$', CreateTaskView.as_view(), name="create-tasks"),    
    url(r'^team\/[a-zA-z0-9]+\/tasks\/$', TasksView.as_view(), name="tasks"),
    url(r'^team\/[a-zA-z0-9]+\/members\/$', MembersView.as_view(), name="members"),
    url(r'^team\/[a-zA-z0-9]+\/settings\/$', TeamSettingsView.as_view(), name="settings"),
    url(r'^team\/[a-zA-z0-9]+\/delete\/$', DeleteTeam.as_view(), name="delete"),
]