from typing import List

from QuoteEngine.quote_model import QuoteModel


def parse_txt_files(quotes: List, path: str) -> List:
    with open(path, "r") as file:
        for line in file.readlines():
            line = line.strip("\n\r").strip()
            if len(line) > 0:
                parsed = line.split()
                new_quote = QuoteModel(body=parsed[0], author=parsed[1])
                quotes.append(new_quote)
    return quotes
