from stake import StakeClient, SessionTokenLoginRequest, CredentialsLoginRequest
import asyncio

login_request = SessionTokenLoginRequest()
async def print_user():
    async with StakeClient(login_request) as stake_session:
        print(stake_session.user.first_name)
        print(stake_session.headers.stake_session_token)

asyncio.run(print_user())