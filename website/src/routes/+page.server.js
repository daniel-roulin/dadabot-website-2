import db from "$lib/server/db.js"

export function load() {
    let stmt = db.prepare(`
    SELECT number, title, image_path
    FROM chapters
    ORDER BY number
    `);
    const all_chapters = stmt.all();

    stmt = db.prepare(`
    SELECT number, title, image_path 
    FROM chapters
    WHERE last_consulted IS NOT NULL
    ORDER BY last_consulted DESC
    LIMIT 5
    `);
    const trending_chapters = stmt.all();

    return {all_chapters: all_chapters, trending_chapters: trending_chapters}
}
