import discord
from handle_form_submission import handle_form_submission

class ModalMount(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.mount_name_input = discord.ui.TextInput(
            label="Mount Name",
            placeholder="Enter the mount name"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.mount_name_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "mount_name": self.mount_name_input.value, 
            "name_realm": self.name_realm_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
