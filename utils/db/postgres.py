from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

# ===================== FOYDALANUVCHILAR JADVALI =====================
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,        
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, username, telegram_id):
        sql = "INSERT INTO Users (username, telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM Users WHERE telegram_id = '{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

# ===================== MEDIALAR JADVALI =====================
    async def create_table_media(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Media (
        id SERIAL PRIMARY KEY,      
        audio VARCHAR(60) NULL,
        document VARCHAR(60) NULL,
        photo VARCHAR(60) NULL,
        video VARCHAR(60) NULL,
        voice VARCHAR(60) NULL,
        url varchar(255) NULL,
        media_group BOOLEAN DEFAULT FALSE,          
        button VARCHAR(60) NULL,
        callback VARCHAR(60) NULL,
        caption VARCHAR(4000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_audio(self, file_id, caption):
        sql = "INSERT INTO Media (audio, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_document(self, file_id, caption):
        sql = "INSERT INTO Media (document, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_photo(self, file_id, caption):
        sql = "INSERT INTO Media (photo, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_video(self, file_id, caption):
        sql = "INSERT INTO Media (video, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_voice(self, file_id, caption):
        sql = "INSERT INTO Media (voice, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_url(self, url, caption):
        sql = "INSERT INTO Media (url, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, url, caption, fetchrow=True)

