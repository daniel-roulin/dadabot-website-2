import {error} from '@sveltejs/kit';
import db from "$lib/server/db.js";

export function load({params}) {
    let stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE chapter = ?
    `);
    const all_exercises = stmt.all(params.chapter);

    if (all_exercises.length === 0) 
        throw error(404);
    


    stmt = db.prepare(`
    SELECT chapter, number, content
    FROM exercises
    WHERE  chapter = ? AND last_consulted IS NOT NULL
    ORDER BY last_consulted DESC
    LIMIT 5
    `);
    const trending_exercises = stmt.all(params.chapter)

    stmt = db.prepare(`
    UPDATE chapters
    SET last_consulted = CURRENT_TIMESTAMP
    WHERE number = ?
    `)
    stmt.run(params.chapter)

    return {chapter: params.chapter, all_exercises: all_exercises, trending_exercises: trending_exercises}
}
