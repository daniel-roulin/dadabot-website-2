CREATE TABLE exercises (
    id INTEGER PRIMARY KEY,
    chapter INTEGER NOT NULL,
    number INTEGER NOT NULL,
    content TEXT NOT NULL,
    last_consulted TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (chapter) REFERENCES chapters(id)
);

/* exercises_fts(content) */
CREATE VIRTUAL TABLE exercises_fts USING fts5(content);

CREATE TABLE IF NOT EXISTS 'exercises_fts_data'(id INTEGER PRIMARY KEY, block BLOB);

CREATE TABLE IF NOT EXISTS 'exercises_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS 'exercises_fts_content'(id INTEGER PRIMARY KEY, c0);

CREATE TABLE IF NOT EXISTS 'exercises_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);

CREATE TABLE IF NOT EXISTS 'exercises_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;

CREATE TRIGGER exercises_fts_update
AFTER
UPDATE
    ON exercises BEGIN
DELETE FROM
    exercises_fts
WHERE
    rowid = new.id;

INSERT INTO
    exercises_fts(rowid, content)
VALUES
    (new.id, new.content);

END;

CREATE TRIGGER exercises_fts_insert
AFTER
INSERT
    ON exercises BEGIN
DELETE FROM
    exercises_fts
WHERE
    rowid = new.id;

INSERT INTO
    exercises_fts(rowid, content)
VALUES
    (new.id, new.content);

END;

CREATE TRIGGER exercises_fts_delete
AFTER
    DELETE ON exercises BEGIN
DELETE FROM
    exercises_fts
WHERE
    rowid = old.id;

END;

CREATE TABLE chapters (
    id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    title TEXT NOT NULL,
    image_path TEXT,
    last_consulted TIMESTAMP DEFAULT NULL
);