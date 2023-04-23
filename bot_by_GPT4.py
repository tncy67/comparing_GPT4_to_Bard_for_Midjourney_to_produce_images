import os
import csv
import discord
import pandas as pd
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
midjourney_bot_id = os.getenv("MIDJOURNEY_BOT_ID")
channel_id = os.getenv("CHANNEL_ID")

# Initialize the client
client = discord.Client()

async def send_midjourney_prompt(channel, prompt):
    # midjourney_bot_id = 123456789012345678  # Replace with the Midjourney bot's user ID
    midjourney_bot = await client.fetch_user(midjourney_bot_id)
    await channel.send(f'{midjourney_bot.mention} {prompt}')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # Read prompts from the CSV file
    df = pd.read_csv('prompts.csv')

    if df.empty:
        print("There is no prompt provided in the CSV file.")
        return

    for _, row in df.iterrows():
        prompt = row['Prompt']

        # Replace the following line with the desired channel ID
        # channel_id = 987654321098765432
        channel = await client.fetch_channel(channel_id)

        await send_midjourney_prompt(channel, prompt)

    await client.close()

client.run(TOKEN)
