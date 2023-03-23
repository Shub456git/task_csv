import aiohttp
import asyncio
import time
import csv

start_time = time.time()

async def fetch_data(session, url):
    async with session.get(url) as resp:
        return await resp.json()


async def main():

    async with aiohttp.ClientSession() as session:
        tasks = []
        data = []
        csvheader = ['name', 'gender', 'film tiles', 'vehicle names', 'starships names', 'species names', 'created',
                         'updated']

        for number in range(1, 51):

            url = f'https://swapi.dev/api/people/{number}'

            if number == 17:
                continue

            tasks.append(asyncio.ensure_future(fetch_data(session, url)))
            people_list = await asyncio.gather(*tasks)

        for x in people_list:
            listing = [x['name'], x['gender'], x['films'], x['vehicles'], x['starships'], x['species'], x['created'], x['edited']]
            data.append(listing)
        print(data)

        with open('test1.csv', 'w', encoding='UTF8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csvheader)
                writer.writerows(data)

        print('CSV generated successfully !!!')


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
