from django.contrib import admin
from .models import TruthTableEntry, AlarmLog  # Make sure both models are imported

admin.site.register(TruthTableEntry)
admin.site.register(AlarmLog)
