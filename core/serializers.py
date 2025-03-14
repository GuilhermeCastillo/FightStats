from rest_framework import serializers
from .models import Organizer, Event, Fighter, Fight, Statistics


# Serializer para Organizer
class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ["id", "name", "email"]


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(queryset=Organizer.objects.all())

    class Meta:
        model = Event
        fields = ["id", "name", "date", "location", "organizer"]


# Serializer para Fighter
class FighterSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = Fighter
        fields = ["id", "name", "nickname", "weight_class", "event"]


# Serializer para Fight
class FightSerializer(serializers.ModelSerializer):
    fighter1 = FighterSerializer()
    fighter2 = FighterSerializer()
    winner = FighterSerializer()

    class Meta:
        model = Fight
        fields = [
            "id",
            "fighter1",
            "fighter2",
            "event",
            "winner",
            "method",
            "round",
            "time",
        ]


# Serializer para Statistics
class StatisticsSerializer(serializers.ModelSerializer):
    fighter = FighterSerializer()
    event = EventSerializer()

    class Meta:
        model = Statistics
        fields = [
            "id",
            "fighter",
            "event",
            "wins",
            "losses",
            "draws",
            "ko_wins",
            "sub_wins",
            "fight_time_avg",
        ]
