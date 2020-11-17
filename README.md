# Aiohttp API

## For starting project on your local machine:
- add your db link to local.yaml file and use next command:<br />
**python entry.py -c local.yaml**
- for reloading project on another port you may try next command:<br />
**python entry.py --reload --port 5000 -c local.yaml**

### Basic features (examples):
- GET cars list: **/api/cars**<br />
- GET car details: **/api/cars/1**<br />
- GET filter car: **/api/cars/filter=Toyota**

### Using Postman (examples):
- POST create new car: **/api/cars?producer=Toyota&model=Corolla&year=2019&color=Green&vin_code=JN1WNYD21U0000001**<br />
- PUT update car: **/api/cars/1?color=Yellow**
- DELE**TE delete car: **/api/cars/1**