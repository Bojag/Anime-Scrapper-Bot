import discord
from discord.ext import commands
import requests

base_url = "https://kitsu.io/api/edge/"
filter_url = "anime?filter[text]="
info_url = "https://kitsu.io/anime/"
headers = {
    "Content-Type": "application/vnd.api+json",
    "Accept": "application/vnd.api+json"
}

class Anime(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def anime(self, ctx,*, name: str):
        await ctx.send("Fetching the Info, Please wait....")
        animation = name
        complete_url = base_url + filter_url + animation
        response = requests.get(complete_url)
        x = response.json()


        channel = ctx.message.channel
        async with channel.typing():

            _id = x["data"][0]["id"]
            _type = x["data"][0]["type"]

            y = x["data"][0]["attributes"]
            name = y["titles"]["en_jp"]
            details = y["synopsis"]
            _create = y["createdAt"]
            _update = y["updatedAt"]
            image = y["posterImage"]["large"]
            _status = y["status"]
            _rating = y["averageRating"]
            _rank = y["ratingRank"]
            _episodes = y["episodeCount"]
            _type = y["subtype"]

            embed = discord.Embed(title =name, url=(info_url + _id), description = details, colour = ctx.author.colour)
            embed.set_thumbnail(url=image)
            embed.add_field(name = ":sparkles: Status", value=_status)
            embed.add_field(name = ":diamond_shape_with_a_dot_inside: Type", value=_type)
            embed.add_field(name = ":calendar_spiral: Created At", value = _create)
            embed.add_field(name = ":calendar_spiral: Updated At", value = _update)
            embed.add_field(name=":cd: Total Episodes", value=_episodes)
            embed.add_field(name = ":star2: Average Rating", value = _rating)
            embed.add_field(name = ":trophy: Rank", value=_rank)
            
            await ctx.send(embed = embed)
    
def setup(client):
    client.add_cog(Anime(client))
    print("Anime File Loaded.....")