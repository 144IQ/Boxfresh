import asyncio
import aiohttp
import datetime

async def send_question(slug, content):
    h = {'Content-Type': 'application/x-www-form-urlencoded'}
    d = {'slug': slug, 'content': content}
    global count

    while True:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://boxfresh.jp/apppage.php',headers=h,data=d) as r:
                time = datetime.datetime.now().strftime('%Y/%m/%d %I:%M(%p)')
                count += 1
                if r.status == 200:
                    print(f'{count} Successed{time}')

                else:
                    print(f'Error{time}')
                    await asyncio.sleep(3)

count = 0
if __name__ == "__main__":
    key = input('URLまたはIDを入力してください\n>>>')
    if key.startswith == "https://box-fresh.jp/index.php?id=":
        key = key.replace('https://box-fresh.jp/index.php?id=','').split('&')

    elif key.startswith == "https://boxfresh.site/":
        key = key.replace('https://boxfresh.site/','').split('&')

    content = input('\n内容を入力してください\n>>>')

    for _ in range(3):
        asyncio.ensure_future(send_question(key, content))
    asyncio.get_event_loop().run_forever()
