import json
import os

from django.core.management.base import BaseCommand

from ... import utils


class Command(BaseCommand):
    help = 'Get current vat rates in european country and saves to database'

    def handle(self, *args, **options):
        commands_dir = os.path.dirname(__file__)
        rates_list_path = os.path.join(commands_dir, "rates_list.json")
        types_path = os.path.join(commands_dir, "types.json")

        with open(rates_list_path, "r") as read_file:
            json_response_rates = json.load(read_file)

        utils.create_objects_from_json(json_response_rates)

        with open(types_path, "r") as read_file:
            json_response_types = json.load(read_file)

        utils.save_vat_rate_types(json_response_types)
