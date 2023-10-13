import discord
from discord.ext import commands
from discord import app_commands

from datetime import datetime

def from_datetime(value):
    if value is not None:
        return datetime.fromisoformat(value)
    return None

class Embed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Embed erstellen")
    @app_commands.checks.has_role(1161358438765428826)
    @app_commands.describe(
        title="Titel des Embeds",
        description="Beschreibung des Embeds",
        color="Farbe des Embeds",
        url="Anklickbare Titel-URL",
        image_url="URL des Bildes",
        thumbnail_url="URL des Thumbnails",
        footer="Footer-Text",
        footer_url="Footer-Icon-URL",
        timestamp="Zeitstempel",
        field1_name="Name des 1. Feldes",
        field1_value="Inhalt des 1. Feldes",
        field2_name="Name des 2. Feldes",
        field2_value="Inhalt des 2. Feldes",
        field3_name="Name des 3. Feldes",
        field3_value="Inhalt des 3. Feldes",
        field4_name="Name des 4. Feldes",
        field4_value="Inhalt des 4. Feldes",
        field5_name="Name des 5. Feldes",
        field5_value="Inhalt des 5. Feldes",
    )
    async def embed(
            self,
            ctx,
            title: str,
            description: str = None,
            color: str = None,
            url: str = None,
            image_url: str = None,
            thumbnail_url: str = None,
            footer: str = None,
            footer_url: str = None,
            timestamp: str = None,
            field1_name: str = "", field1_value: str = "",
            field2_name: str = "", field2_value: str = "",
            field3_name: str = "", field3_value: str = "",
            field4_name: str = "", field4_value: str = "",
            field5_name: str = "", field5_value: str = "",
    ):
        embed = discord.Embed(colour=color, title=title, type='rich', url=url, description=description)

        if timestamp:
            timestamp = from_datetime(timestamp)
            embed.timestamp = timestamp

        embed.set_footer(text=footer, icon_url=footer_url)
        embed.set_image(url=image_url)
        embed.set_thumbnail(url=thumbnail_url)
        embed.add_field(name=field1_name, value=field1_value)
        embed.add_field(name=field2_name, value=field2_value)
        embed.add_field(name=field3_name, value=field3_value)
        embed.add_field(name=field4_name, value=field4_value)
        embed.add_field(name=field5_name, value=field5_value)

        await ctx.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Embed(bot))
