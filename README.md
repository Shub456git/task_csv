Async Task -

Write a python script to create csv file that contains first 50 people from the star wars api(https://swapi.dev/) with following columns:
- id
- name
- gender
- film tiles (comma separated)
- vehicle names (comma separated)
- starships names (comma separated)
- species names (comma separated)
- created
- updated

Expectations:
- implement python asyncio module.
- implement python multithreading concept
- script should be performant and should not take several minutes.
- Integrate JMeter to check the processing and time taken to finish the task.



# For Running and create the csv file :

# Install virtual enviourment :
sudo pip3 install virtualenv 


# Create virtual enviourment :
virtualenv venv 
or
python3 -m venv myenv

# Activate virtual enviourment :
source venv/bin/activate




Reference:

for csv file creation : 
https://docs.python.org/3/library/csv.html

for asyncio :
https://realpython.com/async-io-python/
