from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """
    IngestorInterface is an abstract base class that defines a common interface for different types of file ingestors.

    Attributes:
        file_types (list): A list of file types that this ingestor can handle. This should be overridden by subclasses.

    Methods:
        can_ingest(path: str) -> bool:
            Determines if the given file path can be ingested based on its file type. This method should be implemented by subclasses.

        parse(path: str) -> List[QuoteModel]:
            Parses a file at the given path and returns a list of QuoteModel instances. This is an abstract method and must be implemented by subclasses.
    """

    file_types = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
