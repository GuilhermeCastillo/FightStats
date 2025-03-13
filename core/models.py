from django.db import models


# Organizador de evento
class Organizer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Evento de Luta
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Lutador
class Fighter(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    weight_class = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Luta
class Fight(models.Model):
    fighter1 = models.ForeignKey(
        Fighter, related_name="fighter1", on_delete=models.CASCADE
    )
    fighter2 = models.ForeignKey(
        Fighter, related_name="fighter2", on_delete=models.CASCADE
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    winner = models.ForeignKey(Fighter, related_name="winner", on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    round = models.IntegerField()
    time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fighter1.name} vs {self.fighter2.name} - {self.method}"


# Estatísticas do Lutador
class Statistics(models.Model):
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    ko_wins = models.IntegerField(default=0)
    sub_wins = models.IntegerField(default=0)
    fight_time_avg = models.FloatField(default=0)

    def __str__(self):
        return f"Stats for {self.fighter.name} in {self.event.name}"
