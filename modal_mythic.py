import discord
from handle_form_submission import handle_form_submission

class ModalMythic(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.mythic_level_input = discord.ui.TextInput(
            label="Mythic+ Level",
            placeholder="Enter a level (0, 1, 2, ..., 16)"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm")
        self.run_count_input = discord.ui.TextInput(label="How Many Runs")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.mythic_level_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.run_count_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "mythic_level": self.mythic_level_input.value, 
            "name_realm": self.name_realm_input.value,
            "run_count": self.run_count_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
