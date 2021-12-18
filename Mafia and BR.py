# coding: utf8
from discord import channel
import config
import discord
from typing import List, Dict
from discord.ext import commands
from pathlib import Path
import time
import random
from file_creator import create
from docx import Document
import os
import shutil


#Импортируем модули для работы с помощью библиотеки pip

bot = commands.Bot(command_prefix='!')
ADMINROLES = "Админ"
SHUFFLED = []
users_bunker = []
users_mafia = []
roles = []

path = Path.cwd()
direct = os.listdir(f"{path}")


#path - получает директрорию работы бота
#direct - раскладывает ее на список

async def is_admin(author: discord.Member) -> bool:
    """
        Функция проверяет админ ли пользователь
    """
    rolenames = [i.name for i in author.roles]
    for i in rolenames:
        if i == ADMINROLES:
            return True
    return False

@bot.event
async def on_ready():
    """
        Функция запускает бота, проверяем его работоспособность с помощью вывода текста
    """
    print('Logged in as')
    print(bot.user.name)
    print('------')

@bot.command(Pass_context=True, name='FAQ')
async def FAQ(ctx):
    """
        Функция выводит информацию о сервере в ответ на сообщение пользователя
        ctx - в переменную поступает вся информация о юзере
    """
    await ctx.send(
        'FAQ:\n1) Для выбора роли напиши !Lobby {Number}(это нужно сделать перед началом игры)\n2)Для смены лобби напиши !Change {Number}\n3)Для начала игры в бункер напиши !play_bunker в чате лобби в котором находишься. Перед игрой необходимо зарегестрироваться при помощи команды !join_bunker. Для завершения игры используйте команду !bunker_stop.\n4)Для начала игры в мафию напиши !play_mafia. Перед началом игры необходимо зарегестрироваться при помощи команды !join_mafia и добавить роли при помощи команды !roles_add. Ведущим будет тот человек, который запустил игру. Для завершения игры введите !mafia_stop.\n5)Для просмотра зарегестрировавшихся игроков введите команду !party_bunker/!party_mafia.\n6)Для просмотра ролей, добавленных в мафию, введите !roles\n7)Для добавления новых ролей в мафию введите !roles_add {Название роли} {Количество ролей}\n8)Для удаления роли введите !roles_del {Название роли}\n9)Для того, что бы очистить список ролей в мафии введите !roles_clear\n10)Для того что бы очистить списко игроков используйте !users_bunker_clear/!users_mafia_clear.')


@bot.command(Pass_context=True, name='Lobby')
async def Lobby(ctx, arg):
    """
        Функция присваивает пользователю роль, подключая к выбранному лобби, в зависимости от полученного значения переменной arg
        на вход поступает: ctx - информация о пользователе
        arg - переменная для выбора лобби
        В ответ на команду, пользователь получает сообщения об успешном подключении к лобби
        команды time.sleep() - отправка сообщений с задержкой
    """
    member = ctx.message.author
    role_1 = member.guild.get_role(920782582155718687)
    role_2 = member.guild.get_role(920782624681758760)
    role_3 = member.guild.get_role(920782656449421322)
    role_4 = member.guild.get_role(920838063280758784)
    await member.remove_roles(role_1)
    await member.remove_roles(role_2)
    await member.remove_roles(role_3)
    await member.remove_roles(role_4)

    if arg == '1':
        await ctx.send('Подключение к лобби 1.')
        time.sleep(1)
        await ctx.send('Успешно подключен к Лобби 1')
        role_1 = member.guild.get_role(920782582155718687)
        await member.add_roles(role_1)

    if arg == '2':
        await ctx.send('Подключение к лобби 2.')
        time.sleep(1)
        await ctx.send('Успешно подключен к Лобби_2')
        role_2 = member.guild.get_role(920782624681758760)
        await member.add_roles(role_2)

    if arg == '3':
        await ctx.send('Подключение к лобби 3.')
        time.sleep(1)
        await ctx.send('Успешно подключен к Лобби_3')
        role_3 = member.guild.get_role(920782656449421322)
        await member.add_roles(role_3)

    if arg == '4':
        await ctx.send('Подключение к лобби 4.')
        time.sleep(1)
        await ctx.send('Успешно подключен к Лобби_4')
        role_4 = member.guild.get_role(920782656449421322)
        await member.add_roles(role_4)

@bot.command(Pass_context=True, name="roles_add")
async def add_role(ctx, name, k):
    """
        Функция добавляет новые роли по запросу пользователя для игры в мафию
        На вход поступает информация: ctx - инфо о пользователе
        name - название роли
        k - количество ролей
    """
    for i in range(int(k)):
        roles.append(name)
    await ctx.send(f"Роль \"{name}\" успешно добавлена!")

@bot.command(Pass_context=True, name="roles_del")
async def del_role(ctx, name):
    """
        Функция проверяет и удаляет роли
        на вход поступает: ctx- инфо пользователя
        name - необходимая роль
        В проверке условия просматривается существует ли указанная роль
        Если роль найдена - она удаляется, выводя сообщение о результате
    """
    if name not in roles:
        await ctx.send(f"Роль с именем \"{name}\" не существует.")
        return
    roles.remove(name)
    await ctx.send(f"Роль с именем \"{name}\" успешно удалена.")

@bot.command(Pass_context=True, name='roles_clear')
async def roles_clear(ctx):
    """
        Функция проверяет, есть ли в массиве ролей сами роли, в случае их наличия - команда удаляет роли
        На вход: ctx - инфо пользователя
    """
    if roles == []:
        await ctx.send('Список ролей пуст!')
        return
    roles.clear()
    await ctx.send('Список ролей успешно очищен!')

@bot.command(Pass_context=True, name="roles_return")
async def roles_return(ctx):
    """
        Функция выводит весь список присутствующих ролей
        На вход: ctx - инфо пользователя
    """
    await ctx.send(f'Список ролей:\n{roles}')

@bot.command(Pass_context=True, name="users_mafia_clear")
async def users_mafia_clear(ctx):
    """
        Функция проверяет наличие ролей в игре "Мафия"
        На вход: ctx - инфо пользователя
    """
    if users_mafia == []:
        await ctx.send('Список игроков пуст!')
        return
    users_mafia.clear()
    await ctx.send('Список игроков в мафию успешно очищен!')

@bot.command(Pass_context=True, name="users_bunker_clear")
async def users_bunker_clear(ctx):
    """
        Функция проверяет наличие ролей в игре "Бункер"
        На вход: ctx - инфо пользователя
    """
    if users_bunker == []:
        await ctx.send('Список игроков пуст!')
        return
    users_bunker.clear()
    await ctx.send('Список игроков в бункер успешно очищен!')

@bot.command(Pass_context=True, name='mafia_stop')
async def mafia_stop(ctx):
    """
        Функция Завершает игру "Мафия"
        На вход: ctx - инфо пользователя
    """
    shutil.rmtree(f"{path}/mafia/")
    roles.clear()
    await ctx.send('Список ролей успешно очищен!')
    users_mafia.clear()
    await ctx.send('Список игроков в мафию успешно очищен!')
    await ctx.send('Игра в мафию успешно завершена!')

@bot.command(Pass_context=True, name='bunker_stop')
async def bunker_stop(ctx):
    """
        Функция завершает игру "Бункер" и очищает список игроков
        На вход: ctx - инфо пользователя
    """
    shutil.rmtree(f"{path}/bunker/")
    users_bunker.clear()
    await ctx.send('Список игроков в бункер успешно очищен!')

@bot.command(Pass_context=True, name='Change')
async def remove_roles(ctx, arg):
    """
        Функция меняет роль пользователю и подключает к другому лобби
        На вход: ctx - инфо пользователя, arg - переменная с данными о новом лобби
    """
    member = ctx.message.author
    role_1 = member.guild.get_role(920782582155718687)
    role_2 = member.guild.get_role(920782624681758760)
    role_3 = member.guild.get_role(920782656449421322)
    role_4 = member.guild.get_role(920838063280758784)
    await member.remove_roles(role_1)
    await member.remove_roles(role_2)
    await member.remove_roles(role_3)
    await member.remove_roles(role_4)

    if arg == '1':
        await ctx.send('Отключение от Лобби...')
        time.sleep(1)
        role_1 = member.guild.get_role(920782582155718687)  # id роли которую будет получать юзер
        await member.add_roles(role_1)
        await ctx.send('Успешно подключен к Лобби_' + str(arg) + '.')

    if arg == '2':
        await ctx.send('Отключение от Лобби...')
        time.sleep(1)
        role_1 = member.guild.get_role(920782624681758760)  # id роли которую будет получать юзер
        await member.add_roles(role_1)
        await ctx.send('Успешно подключен к Лобби_' + str(arg) + '.')

    if arg == '3':
        await ctx.send('Отключение от Лобби...')
        role_1 = member.guild.get_role(920782656449421322)  # id роли которую будет получать юзер
        await member.add_roles(role_1)
        await ctx.send('Успешно подключен к Лобби_' + str(arg) + '.')

    if arg == '4':
        await ctx.send('Отключение от Лобби...')
        role_1 = member.guild.get_role(920782656449421322)  # id роли которую будет получать юзер
        await member.add_roles(role_1)
        await ctx.send('Успешно подключен к Лобби_' + str(arg) + '.')

@bot.command(name="party_bunker")
async def party_bunker(ctx):
    """
        Функция выводит список игроков
        На вход: ctx - инфо пользователя
    """
    l = users_bunker
    if not l:
        await ctx.send("Игроков нет")
        return
    content = "Список игроков:\n" + "\n".join(
        [f"<@{user}>" for user in l]
    )
    await ctx.send(content)

@bot.command(name="party_mafia")
async def party_mafia(ctx):
    """
        Функция проверяет наличие игроков в игре "Мафия"
        На вход: ctx - инфо пользователя
    """
    l = users_mafia
    if not l:
        await ctx.send("Игроков нет")
        return
    content = "Список игроков:\n" + "\n".join(
        [f"<@{user}>" for user in l]
    )
    await ctx.send(content)

@bot.command(name="join_bunker")
async def join_bunker(ctx):
    """
        Функция регистрирует пользователя на игру "Бункер"
        На вход: ctx - инфо пользователя
    """
    if ctx.author.id in users_bunker:
        await ctx.send("Вы уже зарегистрированы.")
        return
    else:
        users_bunker.append(ctx.author.id)
        number_bunker = len(users_bunker)
        await ctx.send(f"Вы зарегистрировались на игру. Ваш номер {number_bunker}")

@bot.command(name="join_mafia")
async def join_mafia(ctx):
    """
        Функция регистрирует пользователя на игру "Мафия"
        На вход: ctx - инфо пользователя
    """
    """
        if ctx.author.id in users_mafia:
        await ctx.send("Вы уже зарегистрированы.")
        return
        else:
    """
    users_mafia.append(ctx.author.id)
    number_mafia = len(users_mafia)
    await ctx.send(f"Вы зарегистрировались на игру. Ваш номер {number_mafia}")

@bot.command(Pass_context=True)
async def play_bunker(ctx):
    """
        Функция запускает игру "Бункер" и выдает пользователю сообщение о запуске игры.
        На вход: ctx - инфо пользователя
        В цикле для каждого пользователя создается и высылается отдельный файл с информацией для игры
    """
    await ctx.send(
        'Да начнётся игра! Сейчас будут отправлены файлы с вашими игровыми персонажами.(Для более интересной игры не подсматривайте)')
    try:
        os.makedirs(f"{path}/bunker")
        b = f"{path}/bunker"
    except:
        b = f"{path}/bunker"

    h = 1
    while h < len(users_bunker) + 1:
        time.sleep(0.5)
        create()
        with open(f"{b}/{h}.docx", 'w') as document_bunker:
            document_bunker = Document()
            myfile = open(f'{path}/bunker/BabyFile.txt').read()
            document_bunker.add_paragraph(myfile)
            document_bunker.save(f'{b}/' + str(h) + '.docx')
        j = str(h) + '.docx'
        await ctx.send(file=discord.File(f"{b}/{j}"))
        h += 1


@bot.command(Pass_context=True)
async def play_mafia(ctx):
    """
        Функция запускает игру "Мафия" и выдает пользователю сообщение о запуске игры.
        На вход: ctx - инфо пользователя
        В цикле для каждого пользователя создается и высылается отдельный файл с информацией для игры
    """
    if is_admin == False:
        await ctx.send('Игру может запустить только админ.')
        time.sleep(0.5)
    if len(users_mafia) <= 0:
        await ctx.send('Игроков слишком мало для начала игры!')
        time.sleep(0.5)
        return
    if len(roles) == 0:
        await ctx.send('Роли не добавлены, добавьте их через команду *!add_role* ')
        time.sleep(0.5)
        return
    if len(users_mafia) != len(roles):
        await ctx.send('Количество ролей не совпадает с количеством игроков')
        await ctx.send(party_mafia)
        await ctx.send(roles_return)
        time.sleep(0.5)
        return
    try:
        os.makedirs(f"{path}/mafia")
        m = f"{path}/mafia"
    except:
        m = f"{path}/mafia"
    random.shuffle(roles)
    h = 1
    while h < len(users_mafia) + 1:
        with open(f"{m}/{h}.docx", 'w') as document_mafia:
            document_mafia = Document()
            document_mafia.add_paragraph(str(roles[h - 1]))
            document_mafia.save(f'{m}/' + str(h) + '.docx')
            j = str(h) + '.docx'
            await ctx.send(file=discord.File(f"{m}/{j}"))
            h += 1
    await ctx.send('Начнем поиски мафии!')


bot.run(config.TOKEN)
