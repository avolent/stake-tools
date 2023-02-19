import asyncio, logging, stake
from stake import StakeClient, SessionTokenLoginRequest
from stake.constant import ASX, NYSE

# Configuration
EXCHANGE = ASX
LOG_LEVEL = logging.DEBUG

# Logging Settings
logging.basicConfig(filename='run.log' ,encoding='utf-8', level=LOG_LEVEL, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
log = logging.getLogger("app.py")
log.addHandler(logging.StreamHandler())


login_request = SessionTokenLoginRequest()

async def print_user():
    try:
        async with StakeClient(login_request) as stake_session:
            log.info(f"User ID: {stake_session.user.id}")
            log.info(f"Name: {stake_session.user.first_name} {stake_session.user.last_name}")
    except stake.client.InvalidLoginException:
        log.error("Please set your STAKE_TOKEN, more info in README.")
        quit()
    except Exception as e:
        log.error(e)
        quit()

async def show_portfolio(exchange):
    async with stake.StakeClient(exchange=exchange) as stake_session:
        my_equities = await stake_session.equities.list()
        return my_equities

async def check_market_status(exchange):
    async with stake.StakeClient(exchange=exchange) as stake_session:
        market = await stake_session.market.get()
        return market.status.current

if __name__ == "__main__":
    asyncio.run(print_user())
    print(f"Market Status: {asyncio.run(check_market_status(EXCHANGE))}")
    for i in asyncio.run(show_portfolio(EXCHANGE)).equity_positions:
        print(i)
   

