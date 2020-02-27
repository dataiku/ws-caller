import asyncio

import click
from ws_caller import Scenario, websocket_client


@click.command()
@click.option("--host", "-h", default="localhost")
@click.option("--port", "-p", type=int, default=80)
@click.option("--path", required=True)
@click.option("--clients", "-c", default=5)
@click.option("--repeat", "-r", default=1)
@click.option("--cookie", "-C", multiple=True)
@click.option(
    "--scenario", type=click.Choice([x.name for x in Scenario], case_sensitive=False)
)
def ws_caller(
    host: str,
    port: int,
    path: str,
    clients: int,
    repeat: int,
    cookie: list,
    scenario: str,
):
    """Connect to a websocket endpoint and behave according to a scenario"""
    scenario = Scenario(scenario)
    cookies = {k: v for k, v in (h.split("=") for h in cookie)}
    for _ in range(repeat):
        try:
            asyncio.get_event_loop().run_until_complete(
                asyncio.gather(
                    *(
                        websocket_client(
                            host, port, path, cookies, scenario, click.echo
                        )
                        for _ in range(clients)
                    )
                )
            )
        except Exception as e:
            click.secho(str(e), fg="red")
