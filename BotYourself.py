# BotYourself.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import time
from datetime import datetime as dt
import random

from kaamelott import kaamelott
from worldlist import worldlist

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
channels = ["botchannel"]

print("\n-----------------------------")
print("---Ravi de vous revoir Sky---")
print("--------Lancement ...--------")
print("-----------------------------\n")

#====================================================================================#

#====================================================================================#

@client.event
async def on_ready():
	print("""################################################""")
	print(f'## {client.user} has connected to Discord! ##')
	print("""################################################""")
	print("\n-----------------------------")
	print("------Et c'est parti !!------")
	print("-----------------------------\n")

#====================================================================================#

#====================================================================================#

#====================================================================================#

#====================================================================================#

@client.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	if message_id == :
		server = client.get_guild() 
		role = None

        # on crée les associations emoji/role a l'aide de leur code point
        # on peut l'obtenir en tapant dans discord :
        #              \:poop:

		if payload.emoji.name == '💻':
			role = discord.utils.get(server.roles, name='Licence Info')
		elif payload.emoji.name == '💯':
			role = discord.utils.get(server.roles, name='Licence Math')
		elif payload.emoji.name == '🐊':
			role = discord.utils.get(server.roles, name='Licence SVT')
		elif payload.emoji.name == '📜':
			role = discord.utils.get(server.roles, name='Licence Autre')
		elif payload.emoji.name == '⚙️':
			role = discord.utils.get(server.roles, name='Master')
		elif payload.emoji.name == 'prof':
			role = discord.utils.get(server.roles, name='Prof')
		elif payload.emoji.name == 'lol':
			role = discord.utils.get(server.roles, name='Lol')
		elif payload.emoji.name == 'CC':
			role = discord.utils.get(server.roles, name='Magic')
		elif payload.emoji.name == 'overwatch':
			role = discord.utils.get(server.roles, name='Overwatch')
		elif payload.emoji.name == 'apex':
			role = discord.utils.get(server.roles, name='Apex')
		elif payload.emoji.name == 'wow':
			role = discord.utils.get(server.roles, name='Wow')
		elif payload.emoji.name == '7daytodie':
			role = discord.utils.get(server.roles, name='7Day To Die')
		elif payload.emoji.name == 'wot':
			role = discord.utils.get(server.roles, name='WoT')
		elif payload.emoji.name == 'redstone':
			role = discord.utils.get(server.roles, name='Minecraft')
		elif payload.emoji.name == 'factorio':
			role = discord.utils.get(server.roles, name='Factorio')


		if role is not None:  # si le role choisi ne fait pas parti des ci-dessus
			member = discord.utils.find(lambda m: m.id == payload.user_id, server.members)
			await member.add_roles(role)
		print("done")


@client.event
async def on_raw_reaction_remove(payload):
	message_id = payload.message_id
	if message_id == :
		server = client.get_guild()
		role = None

		if payload.emoji.name == '💻':
			role = discord.utils.get(server.roles, name='Licence Info')
		elif payload.emoji.name == '💯':
			role = discord.utils.get(server.roles, name='Licence Math')
		elif payload.emoji.name == '🐊':
			role = discord.utils.get(server.roles, name='Licence SVT')
		elif payload.emoji.name == '📜':
			role = discord.utils.get(server.roles, name='Licence Autre')
		elif payload.emoji.name == '⚙️':
			role = discord.utils.get(server.roles, name='Master')
		elif payload.emoji.name == 'prof':
			role = discord.utils.get(server.roles, name='Prof')
		elif payload.emoji.name == 'lol':
			role = discord.utils.get(server.roles, name='Lol')
		elif payload.emoji.name == 'CC':
			role = discord.utils.get(server.roles, name='Magic')
		elif payload.emoji.name == 'overwatch':
			role = discord.utils.get(server.roles, name='Overwatch')
		elif payload.emoji.name == 'apex':
			role = discord.utils.get(server.roles, name='Apex')
		elif payload.emoji.name == 'wow':
			role = discord.utils.get(server.roles, name='Wow')
		elif payload.emoji.name == '7daytodie':
			role = discord.utils.get(server.roles, name='7Day To Die')
		elif payload.emoji.name == 'wot':
			role = discord.utils.get(server.roles, name='WoT')
		elif payload.emoji.name == 'redstone':
			role = discord.utils.get(server.roles, name='Minecraft')
		elif payload.emoji.name == 'factorio':
			role = discord.utils.get(server.roles, name='Factorio')

		if role is not None:  # si le role est choisi fait parti des 5 ci-dessus
			member = discord.utils.find(lambda m: m.id == payload.user_id, server.members)
			await member.remove_roles(role)
		print("done")


@client.event
async def on_member_join(member):
	for channel in member.guild.channels:
		if str(channel) == "": # We check to make sure we are sending the message in the general channel
			await channel.send(f"""Bienvenue {member.mention} dans l'antre de comput!""")
			role = discord.utils.get(member.guild.roles, name = 'Non Membre')
			await member.add_roles(role)
			print(f"""Event : on_member_join \n 	Bienvenue {member.name} dans l'antre de comput!""")

#====================================================================================#

#====================================================================================#

#====================================================================================#

#====================================================================================#

@client.event
async def on_message(message):

	if str(message.channel) in channels :
	
	#Kaamelott
		if any(Kaamelott in message.content for Kaamelott in worldlist().liste_Kaamelott) and message.author != message.guild.me:
			time.sleep(2)
			nbrandom = random.randint(0,22)
			perceval = kaamelott().tabkaamelott[nbrandom]
			await message.channel.send(perceval)
			print('Event : on_message \n 	Kaamelott')

	#BOT
		if any(bot in message.content for bot in worldlist().liste_bot) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Oui ?'.format(message)
			await message.channel.send(msg)
			print('Event : on_message \n 	Oui ?')

	#NON RIEN   
		if any(non_rien in message.content for non_rien in worldlist().liste_non_rien) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Me parle pas alors'
			await message.channel.send(msg)
			print('Event : on_message \n 	Me parle pas alors')

	#42
		if any(perdu in message.content for perdu in worldlist().liste_perdu) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Perdu!'
			await message.channel.send(msg)
			print('Event : on_message \n 	Perdu!')

	#STARK
		if any(stark in message.content for stark in worldlist().liste_stark) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Je suis à vos ordres Mr Stark'
			await message.channel.send(msg)
			print('Event : on_message \n 	Je suis à vos ordres Mr Stark')

	#PING
		if any(ping in message.content for ping in worldlist().liste_ping) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Ping'
			await message.channel.send(msg)
			print('Event : on_message \n 	Ping')

	#PONG
		if any(pong in message.content for pong in worldlist().liste_pong) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Pong'
			await message.channel.send(msg)
			print('Event : on_message \n 	Pong')

	#CHAT
		if any(chat in message.content for chat in worldlist().liste_chat) and message.author != message.guild.me:
			time.sleep(2)
			msg= 'Miaou'.format(message)
			await message.channel.send(msg)
			print('Event : on_message \n 	Miaou')

	#star wars
		if any(generalkenobi in message.content for generalkenobi in worldlist().liste_generalkenobi) and message.author != message.guild.me :
			time.sleep(2)
			await message.channel.send(file=discord.File('./picture_movie/generalkenobi.jpg'))
			print('Event : on_message \n 	star wars')


		if any(obiwan in message.content for obiwan in worldlist().liste_obiwan) and message.author != message.guild.me:
			time.sleep(2)
			await message.channel.send(file=discord.File('./picture_movie/hellothere2.jpg'))
			print('Event : on_message \n 	star wars')

#====================================================================================#

#====================================================================================#

client.run(token)