import csv
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    CSVIngestor is a concrete implementation of the IngestorInterface for parsing CSV files.

    Attributes:
        file_types (list): A list of file types that this ingestor can handle.

    Methods:
        parse(path: str) -> List[QuoteModel]:
            Parses a CSV file at the given path and returns a list of QuoteModel instances.
    """

    file_types = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Edge case for incorrect path
        if not cls.can_ingest(path):
            raise Exception("Cannot be ingested")

        quotes = []
        with open(path, "r") as f:
            d = csv.DictReader(f)
            for row in d:
                quotes.append(QuoteModel(row['body'],
                                         row['author']))
        return quotes
