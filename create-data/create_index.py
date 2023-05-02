import os
import pdftotext
from progress import progress


def create_index(chapter_folder_path):
    print("Indexing chapters...")
    index = {}
    chapters = os.listdir(chapter_folder_path)
    chapters.sort(key=lambda path: int(path[len("chapter"):-len(".pdf")]))
    for chapter_path in chapters:
        chapter_num = int(chapter_path[len("chapter"):-len(".pdf")])
        with open(os.path.join(chapter_folder_path, chapter_path), "rb") as f:
            pdf_text = pdftotext.PDF(f)

        ex_num = 1
        ex_to_pg = {}
        for page_num in range(len(pdf_text)):
            page = pdf_text[page_num]

            if chapter_num == 30 and page_num == 21:
                with open("test.txt", "w") as f:
                    f.write(page)

            for line in page.splitlines():
                if line.lstrip().startswith(str(ex_num) + ". ") or line.strip() == str(ex_num) + ".":
                    ex_to_pg[ex_num] = page_num
                    ex_num += 1

                    # Pdftotext fails to correctly indentify these 2
                    if ex_num == 66 and chapter_num == 36:
                        ex_to_pg[ex_num] = 16
                        ex_num += 1
                    if ex_num == 71 and chapter_num == 30:
                        ex_to_pg[ex_num] = 21
                        ex_num += 1

        index[chapter_num] = ex_to_pg
        index = dict(sorted(index.items(), key=lambda s: int(s[0])))

        progress(chapter_num, len(chapters))

    print("Done!")
    return index