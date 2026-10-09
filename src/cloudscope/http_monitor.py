import httpx, time

def check_website(url:str) -> tuple[int, float]:
    start_time = time.perf_counter()
    response = httpx.get(url, timeout=5)
    end_time = time.perf_counter()

    return response.status_code, (end_time - start_time) * 1000

if __name__ == "__main__":
    url = "https://example.com"

    status_code, response_time = check_website(url)

    print(f"Checking: {url}")
    print(f"HTTP Status: {status_code}")
    print(f"Response Time: {response_time:.2f} ms")