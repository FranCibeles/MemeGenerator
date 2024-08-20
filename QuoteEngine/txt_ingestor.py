from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List
from .utils.txt_parser import parse_txt_files


class TXTIngestor(IngestorInterface):
    """
    TXTIngestor is a concrete implementation of the IngestorInterface for parsing TXT files.

    Attributes:
        file_types (list): A list of file types that this ingestor can handle.

    Methods:
        parse(path: str) -> List[QuoteModel]:
            Parses a TXT file at the given path and returns a list of QuoteModel instances.
    """

    file_types = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Edge case for incorrect path
        if not cls.can_ingest(path):
            raise Exception("Cannot be ingested")

        quotes = []
        parse_txt_files(quotes, path)

        return quotes
