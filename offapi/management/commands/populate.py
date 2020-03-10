from django.core.management.base import BaseCommand, CommandError
from sentry_sdk import capture_message
from ...models import Category
import offapi.management.commands._api as offapi
import offapi.management.commands._updatedb as update


class Command(BaseCommand):
    help = 'call the OFF api and populate the DB'

    def handle(self, *args, **options):
        api = offapi.ApiRetriever()
        data = api.get_data('Produits à tartiner sucrés')
        capture_message("Début de la mise à jour hebdomadaire", level="info")
        for it in data:
            db = update.Storedb()
            stores = db.insert_store(it)
            categories = db.insert_category(it)
            db.insert_product(it, stores, categories)
        capture_message("Fin de la mise à jour hebdomadaire", level="info")
