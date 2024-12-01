import discord
from handle_form_submission import handle_form_submission

class ModalBuyGold(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)

        self.payment_method_input = discord.ui.TextInput(
            label="Payment Method",
            placeholder="Enter 'CRYPTO'"
        )
        self.gold_amount_input = discord.ui.TextInput(
            label="How Much Gold",
            placeholder="Enter the amount of gold needed"
        )
        self.name_realm_input = discord.ui.TextInput(label="Name and Realm")
        self.note_input = discord.ui.TextInput(label="Note", style=discord.TextStyle.paragraph, required=False)
        
        self.add_item(self.payment_method_input)
        self.add_item(self.gold_amount_input)
        self.add_item(self.name_realm_input)
        self.add_item(self.note_input)

    async def on_submit(self, interaction: discord.Interaction):
        form_data = {
            "payment_method": self.payment_method_input.value,
            "gold_amount": self.gold_amount_input.value,
            "name_realm": self.name_realm_input.value,
            "note": self.note_input.value
        }
        await handle_form_submission(interaction, form_data)
