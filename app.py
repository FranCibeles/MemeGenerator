import random
import os
from webbrowser import Error

import requests
from flask import Flask, render_template, abort, request
from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote_model import QuoteModel


app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))


    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    data_form = request.form
    path = data_form['image_url']
    body = data_form['body']
    author = data_form['author']
    try:
        if path and body and author  is not None:
            img_request = requests.get(path)
            tmp =  f"./img{random.randint(0, 10000)}.png"

            # Obtaining the Image from the URL of the Form and saving in a tmp file
            with open(tmp, 'wb') as img:
                img.write(img_request.content)

            # Obtaining the quote and the author and saving in a QuoteModel instance

            quote = QuoteModel(body=body, author=author)

            path = meme.make_meme(tmp, quote.body, quote.author)
            os.remove(tmp)
        else:
            raise Error("Every Form field is mandatory")
        return render_template("meme.html", path=path)
    except Exception:
        print("It seems that the path doesn't contain any image or you have not given a quote or an author")
        return "Every field is mandatory or probably the given URL doesn't contain a valid image"


if __name__ == "__main__":
    app.run()
