import os
import random
from argparse import ArgumentParser

from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote_model import QuoteModel
from MemeGenerator.meme_generator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = ArgumentParser(
        description="Pass your image path, selected quote and its author to create a meme - OPTIONAL")
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        help="Image file path")
    parser.add_argument("--body", type=str, default=None, help="Quote text")
    parser.add_argument(
        "--author",
        type=str,
        default=None,
        help="author of quote")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
