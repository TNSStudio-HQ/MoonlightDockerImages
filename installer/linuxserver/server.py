import os
import aiohttp      
import asyncio  
os.system("pip install aiofiles >/dev/null 2>/dev/null")
os.system("pip3 install aiofiles >/dev/null 2>/dev/null")
import aiofiles


async def t():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://github.com/TNSStudio-HQ/MoonlightDockerImages/raw/main/installer/linuxserver/installer.sh") as resp:
            if resp.status == 200:
                f = await aiofiles.open('./installer.sh', mode='wb')
                await f.write(await resp.read())
                await f.close()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(t())
    loop.close()
    os.system("bash installer.sh")
    os.system("gotty --port {SERVER_PORT} --credential root:{PASSWORD} --permit-write --permit-arguments --title-format "WebConsole - Moonlight" bash")

if __name__ == '__main__':
    main()
