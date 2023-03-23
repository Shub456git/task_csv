import aiohttp
import asyncio
import time
import csv

start_time = time.time()

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:

        for number in range(1, 51):

            if number == 17:
                print("No data found")
                continue

            people_data = await fetch_data(session, str(f'https://swapi.dev/api/people/{number}'))

            vehicles = await asyncio.gather(
                *(fetch_data(session, vehicle_url) for vehicle_url in people_data['vehicles']))

            starships = await asyncio.gather(
                *(fetch_data(session, starships_url) for starships_url in people_data['starships']))

            films = await asyncio.gather(
                *(fetch_data(session, starships_url) for starships_url in people_data['films']))

            species = await asyncio.gather(
                *(fetch_data(session, species_url) for species_url in people_data['species']))

            data = {
                'id': people_data['url'].split('/')[-2],
                'name': people_data['name'],
                'gender': people_data['gender'],
                'film_titles': ', '.join([film['title'] for film in films]),
                'vehicle_names': ', '.join([vehicle['name'] for vehicle in vehicles]),
                'starship_names': ', '.join([starship['name'] for starship in starships]),
                'species_names': ', '.join([species['name'] for species in species]),
                'created': people_data['created'],
                'updated': people_data['edited'],
            }

            tasks.append(data)

        print(tasks)
        with open('test4.csv', 'w', newline='') as csv_file:
            fieldnames = ['id', 'name', 'gender', 'film_titles', 'vehicle_names', 'starship_names', 'species_names', 'created', 'updated']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for person in tasks:
                writer.writerow(person)

if __name__ == '__main__':
    asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
