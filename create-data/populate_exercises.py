from get_text import get_ex_text
from progress import progress


def populate_exercises(connection, index, chapters_path):
    print("Populating exercises metadata...")
    progress(0, len(index))
    data = []
    for chapter, exercises in index.items():
        for exercise in exercises.keys():
            content = get_ex_text(int(chapter), int(exercise), index, chapters_path)
            data.append((chapter, exercise, content))
        progress(int(chapter), len(index))

    cursor = connection.cursor()
    cursor.executemany("INSERT INTO exercises (chapter, number, content) VALUES (?, ?, ?)", data)
    connection.commit()
    print("Done!")
