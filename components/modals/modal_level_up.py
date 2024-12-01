import discord
from utils.handle_form_submission import handle_form_submission

class ModalLevelUp(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.level_input = discord.ui.TextInput(
            label="Which Level",
            placeholder="1-70 or 70-80..."
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm",placeholder="name-realm")
        self.faction_input = discord.ui.TextInput(
            label="Ally or Horde",
            placeholder="Enter 'Ally' or 'Horde'"
        )
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.level_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.faction_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "level": self.level_input.value, 
            "name_realm": self.name_realm_input.value,
            "faction": self.faction_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
