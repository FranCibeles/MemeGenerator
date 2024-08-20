
# Meme Generator

This project is part of the Udacity Nanodegree Intermediate Python course. It consists of two main components: the `MemeGenerator` and the `QuoteEngine`. The `MemeGenerator` is responsible for creating memes by overlaying quotes on images, while the `QuoteEngine` handles the ingestion and parsing of quotes from various file formats.

## Project Structure

The project is organized into the following directories and files:

```
.
├── MemeGenerator
│   ├── __init__.py
│   ├── meme_engine.py
├── QuoteEngine
│   ├── __init__.py
│   ├── ingestor_interface.py
│   ├── csv_ingestor.py
��   ├── docx_ingestor.py
│   ├── pdf_ingestor.py
│   ├── txt_ingestor.py
│   ├── quote_model.py
│   ├── utils
│       ├── __init__.py
│       ├── txt_parser.py
├── _data
│   ├── DogQuotes
│   │   ├── DogQuotesTXT.txt
│   │   ├── DogQuotesDOCX.docx
│   │   ├── DogQuotesPDF.pdf
│   │   ├── DogQuotesCSV.csv
│   ├── photos
│       ├── dog
│           ├── xander_1.jpg
│           ├── xander_2.jpg
│           ├── ...
├── app.py
├── meme.py
├── requirements.txt
├── README.md
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/meme-generator.git
    cd meme-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Generating Memes

To generate a meme, run the `app.py` script. You can specify an image path, a quote body, and an author as command-line arguments:

```sh
python app.py --path <image_path> --body <quote_body> --author <quote_author>
```

If no arguments are provided, a random image and quote will be used.

### Web Interface

You can also run the web interface to generate memes through a web browser. Start the web server by running:

```sh
python meme.py
```

Then, open your browser and navigate to `http://localhost:5000`.

## Quote Ingestion

The `QuoteEngine` module supports ingestion from various file formats including TXT, CSV, DOCX, and PDF. Each ingestor class implements the `IngestorInterface` and provides a `parse` method to read quotes from files.

### Example

To parse quotes from a CSV file:

```python
from QuoteEngine.csv_ingestor import CSVIngestor

quotes = CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
for quote in quotes:
    print(quote)
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

This project is part of the Udacity Nanodegree Intermediate Python course.
This Readme Document was generated using the Copilot Plugin for PyCharm.
