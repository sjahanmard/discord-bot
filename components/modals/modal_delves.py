import discord
from utils.handle_form_submission import handle_form_submission

class ModalDelves(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.delves_level_input = discord.ui.TextInput(
            label="Delves Level",
            placeholder="Enter a level (0, 1, 2, ..., 16)"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm",placeholder="name-realm")
        self.run_count_input = discord.ui.TextInput(label="How Many Runs")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False , placeholder="Armor stack or specific key...")
        
        self.add_item(self.delves_level_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.run_count_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "delves_level": self.delves_level_input.value, 
            "name_realm": self.name_realm_input.value,
            "run_count": self.run_count_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
