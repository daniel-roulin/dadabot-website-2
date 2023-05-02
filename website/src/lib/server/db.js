import Database from 'better-sqlite3';

const db = new Database('./database/database.db');
db.pragma('journal_mode = WAL');

// function shutdownGracefully() {
//     db.close();
// }

// process.on('SIGINT', shutdownGracefully);
// process.on('SIGTERM', shutdownGracefully);

export default db;
