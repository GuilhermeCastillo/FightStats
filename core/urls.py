from django.urls import path
from .views import (
    OrganizerListCreateView,
    OrganizerRetrieveUpdateDestroyView,
    EventListCreateView,
    EventRetrieveUpdateDestroyView,
    FighterListCreateView,
    FighterRetrieveUpdateDestroyView,
    FightListCreateView,
    FightRetrieveUpdateDestroyView,
    StatisticsListCreateView,
    StatisticsRetrieveUpdateDestroyView,
)

urlpatterns = [
    # URLs para Organizer
    path(
        "organizers/", OrganizerListCreateView.as_view(), name="organizer-list-create"
    ),
    path(
        "organizers/<int:pk>/",
        OrganizerRetrieveUpdateDestroyView.as_view(),
        name="organizer-retrieve-update-destroy",
    ),
    # URLs para Event
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path(
        "events/<int:pk>/",
        EventRetrieveUpdateDestroyView.as_view(),
        name="event-retrieve-update-destroy",
    ),
    # URLs para Fighter
    path("fighters/", FighterListCreateView.as_view(), name="fighter-list-create"),
    path(
        "fighters/<int:pk>/",
        FighterRetrieveUpdateDestroyView.as_view(),
        name="fighter-retrieve-update-destroy",
    ),
    # URLs para Fight
    path("fights/", FightListCreateView.as_view(), name="fight-list-create"),
    path(
        "fights/<int:pk>/",
        FightRetrieveUpdateDestroyView.as_view(),
        name="fight-retrieve-update-destroy",
    ),
    # URLs para Statistics
    path(
        "statistics/", StatisticsListCreateView.as_view(), name="statistics-list-create"
    ),
    path(
        "statistics/<int:pk>/",
        StatisticsRetrieveUpdateDestroyView.as_view(),
        name="statistics-retrieve-update-destroy",
    ),
]
