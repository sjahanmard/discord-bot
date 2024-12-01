import discord
from modal_raid import ModalRaid
from modal_mythic import ModalMythic
from modal_level_up import ModalLevelUp
from modal_mount import ModalMount
from modal_legacy import ModalLegacy
from modal_pvp import ModalPvP
from modal_buy_gold import ModalBuyGold

class AllOptions(discord.ui.View):
    @discord.ui.button(label="Raid", style=discord.ButtonStyle.primary, custom_id="raid")
    async def raid_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalRaid(title="Raid")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Mythic+", style=discord.ButtonStyle.primary, custom_id="mythic_plus")
    async def mythic_plus_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalMythic(title="Mythic+")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Level Up", style=discord.ButtonStyle.primary, custom_id="levelup")
    async def levelup_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalLevelUp(title="Level Up")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Mount", style=discord.ButtonStyle.primary, custom_id="mount")
    async def mount_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalMount(title="Mount")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Legacy", style=discord.ButtonStyle.primary, custom_id="legacy")
    async def legacy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalLegacy(title="Legacy")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="PvP", style=discord.ButtonStyle.primary, custom_id="pvp")
    async def pvp_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalPvP(title="PvP")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Buy Gold", style=discord.ButtonStyle.primary, custom_id="buy_gold")
    async def buy_gold_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalBuyGold(title="Buy Gold")
        await interaction.response.send_modal(modal)  


