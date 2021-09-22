### Code under test ###
import asyncio

async def times_two(x):
    await asyncio.sleep(0.5)
    return x * 2


### Test code ###
import pytest

@pytest.mark.asyncio
async def test_times_two():
    result = await times_two(5)
    assert result == 9
