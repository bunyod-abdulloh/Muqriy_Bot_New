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
#     async def create_table_users(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS medias_user (
#         id SERIAL PRIMARY KEY,
#         username varchar(255) NULL,
#         telegram_id BIGINT NOT NULL UNIQUE
#         );
#         """
#         await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, username, telegram_id):
        sql = "INSERT INTO medias_user (username, telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM medias_user"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM medias_user WHERE telegram_id = '{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM medias_user"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE medias_user SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM medias_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE medias_user", execute=True)

# ===================== MEDIALAR JADVALI =====================
#     async def create_table_media(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS medias_media (
#         id SERIAL PRIMARY KEY,
#         category_one VARCHAR(100) NULL,
#         subcategory_one VARCHAR(100) NULL,
#         category_two VARCHAR(100) NULL,
#         subcategory_two VARCHAR(100) NULL,
#         type TEXT NULL,
#         file_id VARCHAR(100) NULL,
#         caption VARCHAR(4000) NULL,
#         description VARCHAR(4000) NULL,
#         media_group BOOLEAN DEFAULT FALSE,
#         callback VARCHAR(60) NULL
#         );
#         """
#         await self.execute(sql, execute=True)

    async def add_category_one(self, category_one):
        sql = "INSERT INTO medias_media (category_one) VALUES($1) returning *"
        return await self.execute(sql, category_one, fetchrow=True)

    async def add_subcategory_one(self, subcategory_one, category_one):
        sql = "UPDATE medias_media SET subcategory_one=$1 WHERE category_one=$2"
        return await self.execute(sql, subcategory_one, category_one, execute=True)

    async def add_category_two(self, category_two, category_one, subcategory_one):
        sql = "UPDATE medias_media SET category_two=$1 WHERE category_one=$2 AND subcategory_one=$3"
        return await self.execute(sql, category_two, category_one, subcategory_one, execute=True)

    async def add_subcategory_two(self, subcategory_two, category_two):
        sql = "UPDATE medias_media SET subcategory_two=$1 WHERE category_two=$2"
        return await self.execute(sql, subcategory_two, category_two, execute=True)

    async def add_media(self, type_, file_id, caption, category, subcategory):
        sql = "UPDATE medias_media SET type=$1, file_id=$2, caption=$3 WHERE category=$4 AND subcategory=$5"
        return await self.execute(sql, type_, file_id, caption, category, subcategory, execute=True)

    async def select_main_buttons(self):
        sql = "SELECT category_one FROM medias_media"
        return await self.execute(sql, fetch=True)

    async def drop_table_media(self):
        await self.execute("DROP TABLE medias_media", execute=True)
