import json


def populate_chapters(connection, chapter_names_path):
    print("Populating chapters metadata...")
    with open(chapter_names_path) as f:
        chapter_to_title = json.load(f)

    data = []
    for index, title in chapter_to_title.items():
        data.append((index, index, title, ""))

    cursor = connection.cursor()
    cursor.executemany("INSERT INTO chapters (id, number, title, image_path) VALUES (?, ?, ?, ?)", data)
    connection.commit()
