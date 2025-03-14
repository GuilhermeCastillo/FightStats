from rest_framework import generics
from .models import Organizer, Event, Fighter, Fight, Statistics
from .serializers import (
    OrganizerSerializer,
    EventSerializer,
    FighterSerializer,
    FightSerializer,
    StatisticsSerializer,
)


# Views para Organizer
class OrganizerListCreateView(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class OrganizerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


# Views para Event
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Views para Fighter
class FighterListCreateView(generics.ListCreateAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class FighterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


# Views para Fight
class FightListCreateView(generics.ListCreateAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer


class FightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer


# Views para Statistics
class StatisticsListCreateView(generics.ListCreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


class StatisticsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
