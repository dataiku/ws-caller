from enum import Enum
from typing import Callable

import aiohttp

Scenario = Enum(
    "Scenario",
    {
        scenario: scenario
        for scenario in (
            "CLOSE_IMMEDIATELY",
            "CLOSE_AFTER_FIRST_MESSAGE",
            "PRINT_RECEIVED_MESSAGES",
        )
    },
)


async def websocket_client(
    host: str,
    port: int,
    path: str,
    cookies: dict,
    scenario: Scenario,
    print_lambda: Callable[[str], None] = lambda msg: print(msg),
):
    async with aiohttp.ClientSession(cookies=cookies, raise_for_status=True) as session:
        async with session.ws_connect(f"http://{host}:{port}{path}") as ws:
            if scenario == Scenario.CLOSE_IMMEDIATELY:
                await ws.close()
            elif scenario == Scenario.CLOSE_AFTER_FIRST_MESSAGE:
                await ws.receive()
                await ws.close()
            elif scenario == Scenario.PRINT_RECEIVED_MESSAGES:
                async for message in ws:
                    print_lambda(message)
