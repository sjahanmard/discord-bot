import discord
from utils import add_to_sheet
from utils.service_account_key import service_account_key
from datetime import datetime
import json
import uuid


async def handle_form_submission(interaction: discord.Interaction, form_data:dict ):
    await interaction.response.send_message("Thank you for completing the form, we will contact you asap!", ephemeral=True)

    channel = interaction.channel
    
    if channel:
        submission_details = "\n".join(f"{key.capitalize()}: {value}" for key, value in form_data.items())
        id =str(uuid.uuid4()).replace('-','')
        await channel.send(
            f"Summary of your order **{interaction.user.name}** with id: **{id}**: \n\n{submission_details}"
        )
        row_data = [
        id,
        datetime.now().isoformat(), 
        "OK",
         interaction.user.name,     
        *[f"{key}:{value}" for key, value in form_data.items()] 
        ]
        
        add_to_sheet(
            service_account_key,
            "wow_orders",
             [row_data]
        )
        print(f"Order with id: {id} successfully added.")
        
