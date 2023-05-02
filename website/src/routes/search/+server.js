import {error, json} from '@sveltejs/kit';
import db from "$lib/server/db.js";


export function GET({url}) {
    const query = url.searchParams.get("q");
    if (! query) 
        throw error(400, "parameter query (q) is a required field that is missing.");
    

    const chapter = url.searchParams.get("ch");
    if (isNaN(chapter)) 
        throw error(400, "parameter chapter (ch) must be a valid number.");
    


    const results = search(query.trim(), chapter);
    return json(results)
}

function search(input, input_chapter) {
    // First, try to match the input string to a chapter and exercise pattern
    // For example, "45 35" should match
    const chapterExercisePattern = /^(\d+) (\d+)$/;
    const chapterExerciseMatch = input.match(chapterExercisePattern);
    if (chapterExerciseMatch) {
        const chapter_number = chapterExerciseMatch[1];
        const exercise_number = chapterExerciseMatch[2];

        let exercises = []
        exercises = exercises.concat(getExercise(chapter_number, exercise_number));
        if (exercise_number !== chapter_number) {
            exercises = exercises.concat(getExercise(exercise_number, chapter_number));
        }
        return {exercises: exercises, chapters: []};
    }

    // Next, try to match the input string to a chapter pattern
    // For example, "45" should match
    const chapterPattern = /^\d+$/;
    const chapterMatch = input.match(chapterPattern);
    if (chapterMatch) {
        const number = chapterMatch[0];

        const chapters = getChapter(number);

        let exercises;
        if (input_chapter === null) {
            exercises = getExercisesInChapter(number);
        } else {
            exercises = getExercise(input_chapter, number);
        }

        return {exercises: exercises, chapters: chapters};
    }

    // Next, try to match the input string to a chapter and search query pattern
    // For example, "abc 45 electric" should match
    const chapterSearchPattern = /^(\D*)(\d+)(\D*)$/;
    const chapterSearchMatch = input.match(chapterSearchPattern);
    if (chapterSearchMatch) {
        const query = (chapterSearchMatch[1].trim() + " " + chapterSearchMatch[3].trim()).trim()
        const number = chapterSearchMatch[2];
        let chapters = searchChapters(query);
        chapters = getChapter(number).concat(chapters);
        chapters = chapters.splice(0, 5)
        let exercises;
        if (input_chapter === null) {
            exercises = searchExercisesInChapter(number, query);
        } else {
            exercises = searchExercisesInChapter(input_chapter, query);
            exercises = getExercise(input_chapter, number).concat(exercises);
        }

        return {exercises: exercises, chapters: chapters};
    }

    // Finally, assume that the input is a search query
    const chapters = searchChapters(input);
    const exercises = searchExercises(input);
    return {exercises: exercises, chapters: chapters};
}

function getExercise(chapter, exercise) {
    const stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE chapter = ? AND number = ?
    ;`);
    return stmt.all(chapter, exercise);
}

function getChapter(chapter) {
    let stmt = db.prepare(`
    SELECT number, title, image_path
    FROM chapters
    WHERE number = ?
    `);
    return stmt.all(chapter);
}

function getExercisesInChapter(chapter) {
    const stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE chapter = ?
    ;`);
    return stmt.all(chapter);
}

function searchExercises(query) {
    const stmt = db.prepare(`
    SELECT chapter, number, exercises_fts.content AS content
    FROM exercises INNER JOIN exercises_fts ON exercises.id = exercises_fts.rowid
    WHERE exercises_fts MATCH ?
    ORDER BY rank LIMIT 100
    ;`);
    return stmt.all(query + "*");
}

function searchChapters(query) {
    const stmt = db.prepare(`
    SELECT number, title, image_path
    FROM chapters
    WHERE title LIKE ?
    LIMIT 5
    ;`);
    return stmt.all("%" + query + "%");
}

function searchExercisesInChapter(chapter, query) {
    const stmt = db.prepare(`
    SELECT chapter, number, exercises_fts.content AS content
    FROM exercises INNER JOIN exercises_fts ON exercises.id = exercises_fts.rowid
    WHERE chapter = ? AND exercises_fts MATCH ?
    ORDER BY rank LIMIT 100
    ;`);
    return stmt.all(chapter, query + "*");
}
