import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from discord import InteractionResponse

class Abstimmung(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="abstimmung", description="Aktienabstimmung starten")
    @app_commands.checks.has_role(1161358438765428826)
    @app_commands.describe(aktion="Auszuführende Aktion", aktie="Name der Aktie", kurs="Aktueller Briefkurs")
    @app_commands.choices(aktion=[
        Choice(name='BUY', value=1),
        Choice(name='SELL', value=2),
        Choice(name='BUY-QUANTITY', value=3)
    ])
    async def abstimmung(self, interaction, aktion: Choice[int], aktie: str, kurs: float):
        await interaction.response.send_message(content=f'Abstimmung erstellt: Aktion: {str(aktion.name)}, Aktie: {str(aktie)}, Kurs: {str(kurs)}€')


async def setup(bot):
    await bot.add_cog(Abstimmung(bot))
