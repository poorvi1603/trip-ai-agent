from mcp_client import get_all_tools
import asyncio 

if __name__ == "__main__":
    query = "latest news abt AI"
    asyncio.run(get_all_tools())
    