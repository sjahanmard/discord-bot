import discord
from utils import get_channel_id

async def handle_form_submission(interaction: discord.Interaction, form_data:dict ):
    await interaction.response.send_message("Thank you for completing the form, we will contact you asap!", ephemeral=True)

    user_name = interaction.user.name
    ticket_channel_name= interaction.channel.name
    ticket_channel_d= interaction.channel.id

    channel_id = get_channel_id()
    channel = interaction.client.get_channel(channel_id)
    
    if channel:
        submission_details = "\n".join(f"{key.capitalize()}: {value}" for key, value in form_data.items())
        await channel.send(
            f"New Ticket by **{interaction.user.name}** in **{interaction.channel.name}** (Channel ID: {interaction.channel.id}):\n\n{submission_details}"
        )