from .ingestor_interface import IngestorInterface
import docx
from .quote_model import QuoteModel
from typing import List


class DocxIngestor(IngestorInterface):
    """
    DocxIngestor is a concrete implementation of the IngestorInterface for parsing DOCX files.

    Attributes:
        file_types (list): A list of file types that this ingestor can handle.

    Methods:
        parse(path: str) -> List[QuoteModel]:
            Parses a DOCX file at the given path and returns a list of QuoteModel instances.
    """

    file_types = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Edge case for incorrect path
        if not cls.can_ingest(path):
            raise Exception("Cannot be ingested")

        quotes = []
        document = docx.Document(path)

        for para in document.paragraphs:
            if para.text != "":
                body, author = para.text.split(" - ")
                new_quote = QuoteModel(body.strip(), author.strip())
                quotes.append(new_quote)

            return quotes
