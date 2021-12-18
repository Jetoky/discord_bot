import Mafia_and_BR
import pytest
import unittest.mock

@pytest.mark.asyncio
async def test_func():
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
async def test_func1():
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
async def test_func2():
    ctx = unittest.mock.Mock()