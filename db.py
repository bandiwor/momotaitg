import random as _random
import aiosqlite
from config import DB_FILENAME
from typing import Optional


async def db_init():
    async with aiosqlite.connect(DB_FILENAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chatId INTEGER NOT NULL,
                text TEXT NOT NULL,
                senderId INTEGER NOT NULL,
                isBot BOOLEAN NOT NULL,
                createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()


async def create_message(chat_id: int, text: str, sender_id: int, is_bot: bool):
    async with aiosqlite.connect(DB_FILENAME) as db:
        await db.execute('''
            INSERT INTO messages (chatId, text, senderId, isBot) 
            VALUES (?, ?, ?, ?)
        ''', (chat_id, text, sender_id, is_bot))
        await db.commit()


# Returns: id, chat_id, text, isBot, timeCreate
async def get_messages_by(chat_id: int, sender_id: Optional[int] = None, limit: Optional[int] = None,
                          random: bool = False) -> list[tuple[int, int, str, int, bool, str]]:
    async with aiosqlite.connect(DB_FILENAME) as db:
        query = 'SELECT * FROM messages WHERE chatId = ?'
        params = [chat_id]

        if sender_id:
            query += ' AND senderId = ?'
            params.append(sender_id)

        query += ' ORDER BY createdAt DESC'

        if limit:
            query += ' LIMIT ?'
            params.append(limit)

        async with db.execute(query, params) as cursor:
            rows = await cursor.fetchall()

            if random:
                _random.shuffle(rows)

            return rows
