# Aiohttp API

## For start project using local settings:
- add your db link to local.yaml file and use next command:<br />
**python entry.py -c local.yaml**

### Basic features (examples):
- GET cars list: **/api/cars**<br />
- GET car details: **/api/cars/1**<br />
- GET filter car: **/api/cars/filter=Toyota**

### Using Postman (examples):
- POST create new car: **/api/cars?producer=Toyota&model=Corolla&year=2019&color=Green&vin_code=T-C-G-2019**<br />
- PUT update car: **/api/cars/1?color=Yellow**
- DELETE delete car: **/api/cars/1**