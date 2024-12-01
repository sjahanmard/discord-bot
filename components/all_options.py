import discord
from components.modals.modal_raid import ModalRaid
from components.modals.modal_mythic import ModalMythic
from components.modals.modal_delves import ModalDelves
from components.modals.modal_level_up import ModalLevelUp
from components.modals.modal_mount import ModalMount
from components.modals.modal_legacy import ModalLegacy
from components.modals.modal_pvp import ModalPvP
from components.modals.modal_buy_gold import ModalBuyGold
from components.modals.modal_sell_gold import ModalSellGold

class AllOptions(discord.ui.View):
    @discord.ui.button(label="Raid", style=discord.ButtonStyle.primary, custom_id="raid")
    async def raid_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalRaid(title="Raid")
        await interaction.response.send_modal(modal)  

    @discord.ui.button(label="Mythic+", style=discord.ButtonStyle.primary, custom_id="mythic_plus")
    async def mythic_plus_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalMythic(title="Mythic+")
        await interaction.response.send_modal(modal)  
        
    @discord.ui.button(label="Delves", style=discord.ButtonStyle.primary, custom_id="delves_plus")
    async def delves_plus_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalDelves(title="Delves")
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
        
    @discord.ui.button(label="Sell Gold", style=discord.ButtonStyle.primary, custom_id="sell_gold")
    async def sell_gold_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = ModalSellGold(title="Sell Gold")
        await interaction.response.send_modal(modal)  


