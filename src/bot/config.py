"""
Contains all configuration data for the bot
"""
import os


class Config:

    # auth tokens for bot gateway
    bot_token = os.getenv("TOKEN")

    # base default role for new members assigned with
    # tribe role, Copy role ID and paste between ""
    default_role_id = "1015647831861768273"

    # welcome channel ID
    # id for the channel where the bot will send the welcome message
    # that includes the button to start the quiz.
    # It wil only send once on first boot up if the message does not already exist
    welcome_channel_id = "1015648629886832740"

    # twitter oauth url
    # this is the external url that will be attached to the quiz complete message
    twitter_oauth_url = "https://text.com"

    # configure this section for the tribes
    # add the ID for each tribes role by replacing the 0000s
    # you can also update the icon_url for each tribe so that the correct image is attached to the quiz complete embed
    tribes = {
        "Zuberi": {
            "role_id": 1015650116071342201,
            "description": "Brave, intellects, explorers, travelers, grounded, arrogant",
            "icon_url": "https://cdn.discordapp.com/attachments/1015647327039537248/1015665882493636618/Zuberi_Tribe.png",
            "summary": "Zuberi Hammada navigated the original brigade to Gisana. Upon their trek through the soon-to-be-founded Zuberi Territory, it was not long before Zuberi and her group discovered this land was home to many mysteries. The group settled in Azar Village in the Auraq Desert.",
        },
        "Panuk": {
            "role_id": 1015650158588985366,
            "description": "Leaders, caring, decision makers, hunters/resourceful, seamstresses, kind, reliant",
            "icon_url": "https://cdn.discordapp.com/attachments/1015647327039537248/1015665850163941466/Panuk_Tribe.png",
            "summary": "This arctic tribe prides itself on being caring and welcoming to all who pass by. Your founder is Panuk Uki, the youngest and friendliest of the Founding Four. When the tribespeople travelled by boat to Gisana, Panuk helped comfort nerves by telling stories, offering warm drinks, and singing songs.",
        },
        "Briar": {
            "role_id": 1015650266546180186,
            "description": "Chefs, farmers, jolly, confident, funny, weak, hard workers, loyal, fair",
            "icon_url": "https://cdn.discordapp.com/attachments/1015647327039537248/1015665922490519703/Briar_Tribe.png",
            "summary": "This most playful of tribes is known for their humour and loyalty. They are naturally hardworking and have one of the hardest jobs of all: making sure all four tribes stay well fed and healthy. During the headway to Gisana, Briar Barrow, founder of this Tribe, made sure to cook for all four ships, keeping them strong and in good shape.",
        },
        "Mira": {
            "role_id": 1015650232454893619,
            "description": "Clever/witty, curious, observant, fishers, ambitious, adventurous, sneaky",
            "icon_url": "https://cdn.discordapp.com/attachments/1015647327039537248/1015665900835307620/Mira_Tribe.png",
            "summary": "Mira people are natural-born adventurers and seamen. Led by its founder Mira Mako, this tribe has a knack for thinking outside the box thanks to their intellect and studiousness. Mira is responsible for the entire expedition to Gisana, as she sailed the ships to Gisana, so these fishermen feel at home by any body of water.",
        },
    }

