import discord
from handle_form_submission import handle_form_submission

class ModalPvP(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.mode_input = discord.ui.TextInput(
            label="Mode",
            placeholder="Enter one of: 2v2, 3v3, RBG"
        )
        self.score_input = discord.ui.TextInput(
            label="Your Score",
            placeholder="Enter your score"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.mode_input)
        self.add_item(self.score_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "mode": self.mode_input.value, 
            "score": self.score_input.value,
            "name_realm": self.name_realm_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
