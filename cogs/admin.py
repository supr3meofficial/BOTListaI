from discord.ext import commands

class AdminTools(commands.Cog):
    """Admin only tools"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def moduleload(self, ctx, *, module: str):
        # Ativa um módulo
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.message.add_reaction('\N{CROSS MARK}')
            await ctx.send(f'**ERROR**: {e.__class__.__name__} - {e}')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def moduleunload(self, ctx, *, module: str):
        # Desativa um módulo
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.message.add_reaction('\N{CROSS MARK}')
            await ctx.send(f'**ERROR**: {e.__class__.__name__} - {e}')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def modulereload(self, ctx, *, module: str):
        # Recarrega um módulo
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.message.add_reaction('\N{CROSS MARK}')
            await ctx.send(f'**ERROR**: {e.__class__.__name__} - {e}')
        else:
            await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

def setup(bot):
	bot.add_cog(AdminTools(bot))
