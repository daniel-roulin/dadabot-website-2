import os
import tempfile
from split_chapters import split_chapters
from create_index import create_index
from generate_image import generate_image
from populate_chapters import populate_chapters
from populate_exercises import populate_exercises
from progress import progress
import warnings
import json
import sqlite3

warnings.filterwarnings("ignore")

DATA_PATH = "../dadabot-data"
CHAPTER_NAMES_PATH = os.path.join(DATA_PATH, "chapter_names.json")
STATIC_PATH = os.path.join(DATA_PATH, "static")
DB_PATH = os.path.join(DATA_PATH, "database", "database.db")
ANSWERS_PATH = os.path.join(STATIC_PATH, "answers")
PDFS_PATH = os.path.join(STATIC_PATH, "pdfs")
PDF_PATH = os.path.join(PDFS_PATH, "answers.pdf")


def generate_images():
    print("Generating images...")
    progress(0, len(index))
    with tempfile.TemporaryDirectory() as temp_dir:
        for chapter_num, exercises in index.items():
            chapter_dir = os.path.join(ANSWERS_PATH, f"chapter{chapter_num}")
            os.makedirs(chapter_dir, exist_ok=True)
            for exercise_num, page_num in exercises.items():
                destination_path = os.path.join(chapter_dir, f"exercise{exercise_num}.png")
                generate_image(int(chapter_num), int(exercise_num), destination_path, index, ANSWERS_PATH, temp_dir)
            progress(int(chapter_num), len(index))
    print("Done!")


def setup_database():
    print("Setting up database...")
    connection = sqlite3.connect(DB_PATH)

    with open('schema.sql') as f:
        schema = f.read()
        connection.executescript(schema)

    connection.commit()
    return connection


# split_chapters(PDF_PATH, PDFS_PATH)
# index = create_index(ANSWERS_PATH)

with open(f"index.json", 'r') as f:
    index = json.load(f)
    index = dict(sorted(index.items(), key=lambda s: int(s[0])))

# generate_images()

connection = setup_database()
populate_chapters(connection, CHAPTER_NAMES_PATH)
populate_exercises(connection, index, ANSWERS_PATH)