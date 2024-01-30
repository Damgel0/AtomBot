# Imports
import requests
import random
import discord
from discord.ext import commands

token = 'YOUR_BOT_TOKEN'  # Bot token. Getting on https://discord.com/developers/

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)  # Bot prefix


@bot.event
async def on_ready():
    activity = discord.Game(name="Help: ?help", type=3)  # Activity
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'Loggined {bot.user}')  # User login message
    print('---------------------------')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except:
        print('Fail')


bot.remove_command('help')  # Delete standart command help


@bot.tree.command(name='help', description='Help.')
async def help(interaction: discord.Interaction):
    help = discord.Embed(title='Help', description='Thanks for using **AtomBot**!', color=discord.Color.darker_grey())
    help.add_field(name="Command: button", value="Present.", inline=False)
    help.add_field(name="Command: weather [city]", value="Show temperature and weather in your city.", inline=False)
    help.add_field(name="Command: creator", value="Write who created me.", inline=False)
    help.add_field(name="Command: random", value="Write random number.", inline=False)  # Fields
    help.set_footer(text="Bot version: 1.3.2")
    await interaction.response.send_message(embed=help)  # Command help


class MyView(discord.ui.View):
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)

    @discord.ui.button(label='button')
    async def example_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('We are happy to see you <3', ephemeral=True)  # Button code


@bot.tree.command(name='weather', description='Show temperature and weather in your city.')
async def weather(interaction: discord.Interaction, *, location: str):
    # Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
    api_key = 'YOUR_API_KEY'
    # Use the OpenWeatherMap API to get the current weather for the given location
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=ru&appid={api_key}'
    response = requests.get(url)
    whether = response.json()
    # Extract the current temperature and weather condition from the API response
    temperature = whether['main']['temp']
    condition = whether['weather'][0]['description']
    name = whether['name']
    # Send the current weather back to the channel
    await interaction.response.send_message(f'Now in {name} temperature {temperature}°C, {condition}.')


# Add some new commands
@bot.tree.command(name='button', description='Present.')  # Creating command in tree(slash command)
async def button(interaction: discord.Interaction):  # Creating command
    view = MyView()  # Function
    view.message = await interaction.response.send_message(view=view)  # Reply user with bot message

@bot.tree.command(name='creator', description='Write who created me.')
async def creator(interaction: discord.Interaction):
    await interaction.response.send_message('.damgel')

@bot.tree.command(name='random_number', description='Write random number.')
async def random_number(interaction: discord.Interaction, *, number: int):
    await interaction.response.send_message(f'Random number: {random.randrange(number)}') # Using package random to generate random integer for user

bot.run(token)  # Run bot
