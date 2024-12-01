import discord
from utils.handle_form_submission import handle_form_submission

class ModalRaid(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.mode_input = discord.ui.TextInput(
            label="Mode",
            placeholder="Enter one of: Saved, Unsaved, Mythic"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm",placeholder="name-realm")
        self.time_input = discord.ui.TextInput(label="Time", placeholder="Server time")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.mode_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.time_input)
        self.add_item(self.note_input)


            
    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "mode": self.mode_input.value, 
            "name_realm": self.name_realm_input.value,
            "time": self.time_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction=interaction, form_data=form_data)
