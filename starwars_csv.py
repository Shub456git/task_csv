import asyncio
import csv
import time
import aiohttp

start_time = time.time()

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_person_data(session, person_url):
    person_data = await fetch_data(session, person_url)
    films = await asyncio.gather(*(fetch_data(session, film_url) for film_url in person_data['films']))
    vehicles = await asyncio.gather(*(fetch_data(session, vehicle_url) for vehicle_url in person_data['vehicles']))
    starships = await asyncio.gather(*(fetch_data(session, starship_url) for starship_url in person_data['starships']))
    species = await asyncio.gather(*(fetch_data(session, species_url) for species_url in person_data['species']))
    return {
        'name': person_data['name'],
        'gender': person_data['gender'],
        'film_titles': ', '.join([film['title'] for film in films]),
        'vehicle_names': ', '.join([vehicle['name'] for vehicle in vehicles]),
        'starship_names': ', '.join([starship['name'] for starship in starships]),
        'species_names': ', '.join([species['name'] for species in species]),
        'created': person_data['created'],
        'updated': person_data['edited'],
    }

async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1,6):
            people_data = await fetch_data(session, f'https://swapi.dev/api/people/?page={number}')
            people_urls = [person_data['url'] for person_data in people_data['results']]
            people = await asyncio.gather(*(fetch_person_data(session, person_url) for person_url in people_urls))

            # write file in csv
            csv_file = open('test2.csv', 'a')
            fieldnames = ['name', 'gender', 'film_titles', 'vehicle_names', 'starship_names', 'species_names', 'created', 'updated']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for person in people:
                writer.writerow(person)

if __name__ == '__main__':
    asyncio.run(main())

print("--- Time taken : %s seconds ---" % (time.time() - start_time))
