from django.core.management.base import BaseCommand
from main.utils import fetch_exchange_rates


class Command(BaseCommand):
    help = "Оновлює курси валют з API Монобанку"

    def handle(self, *args, **kwargs):
        fetch_exchange_rates()
        self.stdout.write(self.style.SUCCESS("Курси валют успішно оновлено"))
