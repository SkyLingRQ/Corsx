import argparse
import aiohttp
import asyncio
import urllib.parse
from colorama import Fore, init

init()

rd = Fore.RED
g = Fore.GREEN
reset = Fore.RESET

urlMal = "http://evil.com"
headers = {
        "Origin":urlMal
}
corsFound = []

async def fetch(session, url):
    url = url.strip()
    try:
        async with session.get(url, headers=headers) as r:
            header_result = r.headers.get("Access-Control-Allow-Origin")
            header_result2 = r.headers.get("Access-Control-Allow-Credentials")
            if header_result == urlMal:
                if header_result2 and r.headers[header_result2].lower() == "true":
                    print(f"\n            {g}C O R S - S C A N\n{rd}+ {g}{url}\n{rd}+{g} Reflected Origin And Credentials Access Control Is True\n{rd}+{g} Critical{reset}\n")
                else:
                    print(f"\n            {g}C O R S - S C A N\n{rd}+ {g}{url}\n{rd}+{g} Reflected Origin\n{rd}+{g} Hight{reset}\n")
            else:
                print(f"\n            {g}C O R S - S C A N\n\n{rd}        ------CORS not found-----{reset}\n")
    except Exception:
            pass

async def fetch2(session, url):
    url = url.strip()
    try:
        async with session.get(url, headers=headers) as resp:
            header_result = resp.headers.get("Access-Control-Allow-Origin")
            header_result2 = resp.headers.get("Access-Control-Allow-Credentials")

            if header_result == urlMal:
                if header_result2 and resp.headers[header_result2].lower() == "true":
                    print(f"\n            {g}C O R S - S C A N\n{rd}+ {g}{url}\n{rd}+{g} Reflected Origin And Credentials Access Control Is True\n{rd}+{g} Critical{reset}\n")
                else:
                    print(f"\n            {g}C O R S - S C A N\n{rd}+ {g}{url}\n{rd}+{g} Reflected Origin\n{rd}+{g} Hight{reset}\n")
                corsFound.append(url)
            else:
                pass
    except Exception:
        pass


async def main():
    parse = argparse.ArgumentParser(description="C O R S - EviLight")
    parse.add_argument("-u", "--url", help="Scanning a URL")
    parse.add_argument("-f", "--file", help="Scanning using files with URLs")
    args = parse.parse_args()

    if args.url:
        async with aiohttp.ClientSession() as session:
            await fetch(session, args.url)
    
    if args.file:
        with open(args.file, "r") as file:
            urls = file.readlines()

        async with aiohttp.ClientSession() as session:
            task = [fetch2(session, url) for url in urls]
            await asyncio.gather(*task)
            print(f"\n{g}[+] {len(corsFound)} Cors vulnerability found{reset}\n")

asyncio.run(main())