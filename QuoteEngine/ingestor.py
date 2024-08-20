from typing import List
from .ingestor_interface import IngestorInterface
from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .txt_ingestor import TXTIngestor
from .pdf_ingestor import PDFIngestor
from .quote_model import QuoteModel


class Ingestor(IngestorInterface):
    """
    Ingestor is a concrete implementation of the IngestorInterface that acts as a facade to handle multiple file types.

    Attributes:
        ingestors (list): A list of ingestor classes that this ingestor can delegate to.

    Methods:
        parse(path: str) -> List[QuoteModel]:
            Parses a file at the given path by delegating to the appropriate ingestor based on the file type.
    """

    ingestors = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
        except Exception as e:
            raise Exception('Some error has happened', e)
        return []
