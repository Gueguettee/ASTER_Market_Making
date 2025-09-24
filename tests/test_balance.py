import os
import asyncio
from dotenv import load_dotenv
from api_client import ApiClient

async def main():
    """
    Fetches and prints the available USDT balance for perpetuals trading.
    """
    load_dotenv()
    API_USER = os.getenv("API_USER")
    API_SIGNER = os.getenv("API_SIGNER")
    API_PRIVATE_KEY = os.getenv("API_PRIVATE_KEY")
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    print("--- Testing Available Balance Endpoint ---")

    try:
        client = ApiClient(API_USER, API_SIGNER, API_PRIVATE_KEY, API_KEY, API_SECRET)
    except ValueError as e:
        print(f"Initialization Error: {e}")
        return

    async with client:
        try:
            balance_data = await client.get_account_balance()
            print("\nFull balance response:")
            print(balance_data)

            usdt_balance = None
            for asset in balance_data.get('assets', []):
                if asset.get("asset") == "USDT":
                    usdt_balance = asset
                    break
            
            if usdt_balance:
                available_capital = usdt_balance.get("availableBalance")
                print(f"\nSuccessfully found USDT balance.")
                print(f"Available Capital (USDT): {available_capital}")
            else:
                print("\nCould not find USDT balance in the response.")

        except Exception as e:
            print(f"\nAn error occurred during the test: {e}")

if __name__ == "__main__":
    asyncio.run(main())
