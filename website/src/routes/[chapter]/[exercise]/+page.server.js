import {error} from '@sveltejs/kit';
import db from "$lib/server/db.js";

export function load({params}) {
    let stmt = db.prepare(`
    SELECT number, content 
    FROM exercises 
    WHERE chapter = ? AND number = ?
    `);
    const row = stmt.get(params.chapter, params.exercise);

    if (! row) 
        throw error(404);
    


    stmt = db.prepare(`
    UPDATE exercises
    SET last_consulted = CURRENT_TIMESTAMP
    WHERE chapter = ? AND number = ?
    `);
    stmt.run(params.chapter, params.exercise);

    return {chapter: params.chapter, exercise: params.exercise};
}
