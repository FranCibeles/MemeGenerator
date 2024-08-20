import os
import random

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
        Function which creates a meme given a path to find a foto and the quotes attributes
        @param img_path: Path of the foto used for the meme
        @param text: Body of the quote to be introduced in the meme
        @param author: Author of the quote introduced in the meme
        @param width: Width of the meme - Following the rubric 500px
        """

        # Loading the image using Pillow
        img = Image.open(img_path)

        # Resizing the image to the given size by the project rubric
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), 0)

        # Writing the quote in the image
        if text and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("./data/fonts/LoveDays.ttf", size=20)
            draw.text((10, 30), f'"{text}" - {author}', font=font, fill="white")

        # Save the image in the output dir given on the insantiation of the MemeEngine class
        output_path = os.path.join(self.output_dir, f"{random.randint(1, 100000)}.png")
        img.save(output_path)
        return output_path
