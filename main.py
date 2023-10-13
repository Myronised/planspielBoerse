import logging
import os
from pathlib import Path
import asyncio

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('BOT-MAIN')
discord.utils.setup_logging()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.guilds = True
intents.messages = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    intents=intents,
    activity=discord.Activity(type=discord.ActivityType.playing, name='Planspiel Börse'),
    status=discord.Status.online
)

if __name__ == '__main__':
    log.info('Starting bot...')
    cogs = [p.stem for p in Path('cogs').glob('**/*.py') if not p.name.startswith('__')]
    log.info('Loading extensions...')

token = os.getenv('BOT_TOKEN')

async def main():
    async with bot:
        for cog in cogs:
            await bot.load_extension(f'cogs.{cog}')
            log.info('Loaded cogs')
        await bot.start(token)

asyncio.run(main())
