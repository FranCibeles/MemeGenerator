from typing import List
import subprocess
import os
import random

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .utils.txt_parser import parse_txt_files


class PDFIngestor(IngestorInterface):
    """
    PDFIngestor is a concrete implementation of the IngestorInterface for parsing PDF files.

    Attributes:
        file_types (list): A list of file types that this ingestor can handle.

    Methods:
        parse(path: str) -> List[QuoteModel]:
            Parses a PDF file at the given path and returns a list of QuoteModel instances.
    """

    files_types = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Edge case for incorrect path
        if not cls.can_ingest(path):
            raise Exception("Cannot be ingested")

        tmp = f"./tmp/{random.randint(0, 10000)}.txt"
        call = subprocess.call(["pdftoprocess"], path, tmp)

        quotes = []
        parse_txt_files(quotes, tmp)
        os.remove(tmp)

        return quotes
