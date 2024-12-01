import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  

client = discord.Client(intents=intents)


class FormModal(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        
        self.name_input = discord.ui.TextInput(label="Your Name")
        self.email_input = discord.ui.TextInput(label="Your Email", placeholder="example@example.com")
        self.feedback_input = discord.ui.TextInput(label="Your Feedback")
        
        self.add_item(self.name_input)
        self.add_item(self.email_input)
        self.add_item(self.feedback_input)

    async def on_submit(self, interaction: discord.Interaction):
        
        await interaction.response.send_message("Thank you for completing the form!", ephemeral=True)

        
        name = self.name_input.value
        email = self.email_input.value
        feedback = self.feedback_input.value

        
        channel_id = int(os.getenv("FORM_SUBMISSION_CHANNEL_ID"))
        channel = client.get_channel(channel_id)

        
        if channel:
            await channel.send(f"New form submission:\nName: {name}\nEmail: {email}\nFeedback: {feedback}")


class TicketButtons(discord.ui.View):
    @discord.ui.button(label="Form 1", style=discord.ButtonStyle.primary, custom_id="form1")
    async def form1_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        modal = FormModal(title="Form 1")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Form 2", style=discord.ButtonStyle.secondary, custom_id="form2")
    async def form2_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        modal = FormModal(title="Form 2")
        await interaction.response.send_modal(modal)  


@client.event
async def on_ready():
    print(f'I love Sobhan!')


@client.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel) and channel.name.startswith("ticket"):
        view = TicketButtons()  
        await channel.send("Hello! This ticket channel has just been created. How can I help? 🎟️", view=view)


client.run(os.getenv("TOKEN"))
