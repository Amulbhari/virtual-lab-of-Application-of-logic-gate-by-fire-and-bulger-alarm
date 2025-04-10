from django.db import models

class TruthTableEntry(models.Model):
    input_a = models.BooleanField()
    input_b = models.BooleanField()
    input_c = models.BooleanField()
    output = models.BooleanField()

    def __str__(self):
        return f"A:{self.input_a}, B:{self.input_b}, C:{self.input_c} => Output:{self.output}"


class AlarmLog(models.Model):
    alarm_type = models.CharField(max_length=100)
    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alarm_type} triggered at {self.triggered_at}"
