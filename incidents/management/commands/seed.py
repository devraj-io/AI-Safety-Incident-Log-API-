from django.core.management.base import BaseCommand
from incidents.models import Incident

class Command(BaseCommand):
    help = 'Seed the database with sample incidents'

    def handle(self, *args, **kwargs):
        Incident.objects.create(title="AI system misidentification", description="An AI facial recognition misidentified a person.", severity="High")
        Incident.objects.create(title="Autonomous vehicle malfunction", description="A self-driving car ignored traffic signs.", severity="Medium")
        print("Sample incidents added.")
