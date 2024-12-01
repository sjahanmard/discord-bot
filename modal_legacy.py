import discord
from handle_form_submission import handle_form_submission

class ModalLegacy(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.legacy_name_input = discord.ui.TextInput(
            label="Legacy Name",
            placeholder="Enter the legacy name"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.legacy_name_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "legacy_name": self.legacy_name_input.value, 
            "name_realm": self.name_realm_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
