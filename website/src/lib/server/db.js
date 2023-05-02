import Database from 'better-sqlite3';

// const db = new Database('/home/daniel/DADABOT/dadabot-data/database/database.db');
const db = new Database('./database/database.db');
db.pragma('journal_mode = WAL');

function shutdownGracefully() {
    console.log("Shutting down database...")
    db.close();
    console.log("Done! Goodbye...")
}

process.on('SIGINT', shutdownGracefully);
process.on('SIGTERM', shutdownGracefully);

export default db;
