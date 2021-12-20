from _pytest.mark.structures import MARK_GEN
import Mafia_and_BR
import pytest
import unittest.mock
import os

@pytest.mark.asyncio
async def test_join_b():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_bunker.clear()
    await Mafia_and_BR.join_bunker(ctx)
    ctx.send.assert_called_with('Вы зарегистрировались на игру. Ваш номер 1')
    assert Mafia_and_BR.users_bunker == [3]
    await Mafia_and_BR.join_bunker(ctx)
    ctx.send.assert_called_with('Вы уже зарегистрированы.')
    assert Mafia_and_BR.users_bunker == [3]

@pytest.mark.asyncio
async def test_join_m():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_mafia.clear()
    await Mafia_and_BR.join_mafia(ctx)
    ctx.send.assert_called_with('Вы зарегистрировались на игру. Ваш номер 1')
    assert Mafia_and_BR.users_mafia == [3]
    await Mafia_and_BR.join_mafia(ctx)
    ctx.send.assert_called_with('Вы уже зарегистрированы.')
    assert Mafia_and_BR.users_mafia == [3]

@pytest.mark.asyncio
async def test_roles_cl():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.roles.append(3)
    await Mafia_and_BR.roles_clear(ctx)
    ctx.send.assert_called_with('Список ролей успешно очищен!')
    assert Mafia_and_BR.roles == []
    await Mafia_and_BR.roles_clear(ctx)
    ctx.send.assert_called_with('Список ролей пуст!')
    assert Mafia_and_BR.roles == []

@pytest.mark.asyncio
async def test_add_role():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    name = 'Mafia'
    k = '1'
    await Mafia_and_BR.add_role(ctx, name, k)
    ctx.send.assert_called_with('Роль "Mafia" успешно добавлена!')
    assert Mafia_and_BR.roles == ['Mafia']

@pytest.mark.asyncio
async def test_del_role():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    name = "Mirn"
    Mafia_and_BR.roles.clear()
    Mafia_and_BR.roles.append('Mirn')
    await Mafia_and_BR.del_role(ctx, name)
    ctx.send.assert_called_with('Роль с именем "Mirn" успешно удалена.')
    assert Mafia_and_BR.roles == []
    await Mafia_and_BR.del_role(ctx, name)
    ctx.send.assert_called_with('Роль с именем "Mirn" не существует.')
    assert Mafia_and_BR.roles == []

@pytest.mark.asyncio
async def test_users_bunker_clear():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_bunker.append(3)
    await Mafia_and_BR.users_bunker_clear(ctx)
    ctx.send.assert_called_with('Список игроков в бункер успешно очищен!')
    assert Mafia_and_BR.users_bunker == []
    await Mafia_and_BR.users_bunker_clear(ctx)
    ctx.send.assert_called_with('Список игроков пуст!')
    assert Mafia_and_BR.users_bunker == []

@pytest.mark.asyncio
async def test_users_mafia_clear():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_mafia.append(3)
    await Mafia_and_BR.users_mafia_clear(ctx)
    ctx.send.assert_called_with('Список игроков в мафию успешно очищен!')
    assert Mafia_and_BR.users_mafia == []
    await Mafia_and_BR.users_mafia_clear(ctx)
    ctx.send.assert_called_with('Список игроков пуст!')
    assert Mafia_and_BR.users_mafia == []

@pytest.mark.asyncio
async def test_bunker_stop():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    m = Mafia_and_BR.path
    os.makedirs(f"{m}/bunker/")
    Mafia_and_BR.users_bunker.append(3)
    await Mafia_and_BR.bunker_stop(ctx)
    ctx.send.assert_called_with('Список игроков в бункер успешно очищен!')
    assert Mafia_and_BR.users_bunker == []

@pytest.mark.asyncio
async def test_mafia_stop():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    m = Mafia_and_BR.path
    os.makedirs(f"{m}/mafia/")
    Mafia_and_BR.users_mafia.append(3)
    Mafia_and_BR.roles.append('Doctor')
    await Mafia_and_BR.mafia_stop(ctx)
    ctx.send.assert_called_with('Игра в мафию успешно завершена!')
    assert Mafia_and_BR.users_mafia == [] and Mafia_and_BR.roles == []

@pytest.mark.asyncio
async def test_party_bunker():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_bunker.append(3)
    await Mafia_and_BR.party_bunker(ctx)
    ctx.send.assert_called_with("Список игроков:\n" + "\n".join(
        [f"<@{user}>" for user in Mafia_and_BR.users_bunker]))
    assert Mafia_and_BR.users_bunker == [3]

@pytest.mark.asyncio
async def test_party_mafia():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    Mafia_and_BR.users_mafia.append(3)
    await Mafia_and_BR.party_mafia(ctx)
    ctx.send.assert_called_with("Список игроков:\n" + "\n".join(
        [f"<@{user}>" for user in Mafia_and_BR.users_mafia]))
    assert Mafia_and_BR.users_mafia == [3]