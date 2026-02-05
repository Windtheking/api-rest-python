import requests
import time

URL = "http://10.9.223.84:8000/sumar/0/123"
TOTAL_REQUESTS = 1_000_000

start = time.time()

for i in range(TOTAL_REQUESTS):
    r = requests.get(URL)
    if r.status_code != 200:
        print(f"Error en request {i}: {r.status_code}")

end = time.time()

print(f"Total requests: {TOTAL_REQUESTS}")
print(f"Tiempo total: {end - start:.2f} segundos")
