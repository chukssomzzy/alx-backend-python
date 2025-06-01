#!/usr/bin/env python3

"""Concurrently execute sql queries"""
import asyncio
import aiosqlite


async def async_fetch_users():
    """Fetches all users asynchroneously"""
    async with aiosqlite.connect("users.db") as db:
        await db.execute("SELECT * FROM users")

        return await db.execute_fetchall()


async def async_fetch_older_users():
    """Fetch older users"""
    async with aiosqlite.connect("users.db") as db:
        await db.execute("SELECT * FROM users WHERE age > 40")

        return await db.execute_fetchall()


async def fetch_concurrently():
    """Fetch users concurrently"""
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
