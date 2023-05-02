import json
import math
import os
import re
import fitz
import multiprocessing as mp


def segfault_guard(f):
    """
    The decorated function will be called with its input arguments in another process.
    If the execution fails, we try again and hope for the best.
    """
    def wrapper(*args, **kwargs):
        q = mp.Queue()
        p = mp.Process(target=lambda q: q.put(f(*args, **kwargs)), args=(q, ))
        p.start()
        p.join()
        exit_code = p.exitcode

        if exit_code == 0:
            return q.get()

        print('Segfault! Exit code: {}'.format(exit_code))
        # wrapper()

    return wrapper


def find_ex_rect(page, exercise, exercise_page_num, chapter, pdf):
    """Returns the rectangle around a given exercise"""
    matches = page.search_for(f"{exercise}. ")
    rects = []
    for n in range(len(matches)):
        if matches[n].x0 < 110:
            rects.append(matches[n])

    if len(rects) > 1:
        rects.sort(key=lambda r: r.x0)
        return rects[0]

    elif len(rects) < 1:
        print(f"Error: No match for exercise {exercise} on page {exercise_page_num} in chap {chapter}")
        exit()
    return rects[0]


@segfault_guard
def get_ex_text(chapter_int, exercise_int, index, chapters_path):
    """Takes a chapter and exercise number and creates a PDF of the exercise"""

    chapter = str(chapter_int)
    exercise = str(exercise_int)
    next_exercise = str(exercise_int + 1)

    exercise_page_num = index[chapter][exercise]

    if next_exercise in index[chapter]:
        next_exercise_page_num = index[chapter][next_exercise]
        page_range = 1 + (next_exercise_page_num-exercise_page_num)
    else:
        page_range = 1

    pdf = fitz.open(os.path.join(chapters_path, f"chapter{chapter}.pdf"))
    output = fitz.open()

    x, y, width, height = pdf.load_page(exercise_page_num).rect

    crop = fitz.Rect(0, 35, width, height - 115)
    page = output.new_page(-1, crop.width, crop.height*page_range)
    for i in range(page_range):
        page.show_pdf_page(crop + (0, crop.height*i, 0, crop.height*i), pdf, exercise_page_num + i, clip=crop)
    pdf.close()

    page = output.load_page(0)

    ex_rect = find_ex_rect(page, exercise, exercise_page_num, chapter, output)
    if next_exercise in index[chapter]:
        next_ex_rect = find_ex_rect(page, next_exercise, exercise_page_num, chapter, output)
        bottom = next_ex_rect.y0 - 8
    else:
        bottom = height

    top = ex_rect.y0 - 8
    width = page.cropbox.width

    text = page.get_text(clip=fitz.Rect(0, top, width, bottom))

    output.close()

    return clean_text(text)


def clean_text(text):
    if len(text) == 0:
        return ""

    # Remove rare occurences of CHAPTERS appearing in the string
    pattern = r'\d+CHAPTER \d+\.'
    text = re.sub(pattern, '', text)

    # Remove char 65533 (invalid character)
    text = text.replace(chr(65533), "")

    # Remove new lines and tabs
    mapping = dict.fromkeys(range(32))
    text = text.translate(mapping)

    # Remove exercise number
    text = text.split(".", 1)[1]

    return text.strip()