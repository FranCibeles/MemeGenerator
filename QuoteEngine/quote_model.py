class QuoteModel:
    """
    QuoteModel represents a quote with a body and an author.

    Attributes:
        body (str): The text of the quote.
        author (str): The author of the quote.

    Methods:
        __str__() -> str:
            Returns a string representation of the QuoteModel instance.
    """

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f"Quote model of autor: {self.author} who said {self.body}"
