import httpx, time
from cloudscope.models import MonitorResult

def check_website(url:str) -> MonitorResult:

    try:
        start_time = time.perf_counter()
        response = httpx.get(url, timeout=5)
        end_time = time.perf_counter()

        return MonitorResult(url=url, status_code=response.status_code, response_time_ms=(end_time - start_time) * 1000, error=None)

    except httpx.TimeoutException:
        return MonitorResult(url=url, status_code=None, response_time_ms=None, error="Request timed out")

    except httpx.ConnectError:
        return MonitorResult(url=url, status_code=None, response_time_ms=None, error="Connection failed")

    except httpx.RequestError as exc:
        return MonitorResult(url=url, status_code=None, response_time_ms=None, error=f"Request failed: {exc}")

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://httpbin.org/status/503",
        "http://127.0.0.1:65432",
    ]

    for url in urls:
        result = check_website(url)

        print(f"Checking: {url}")
        print(f"HTTP Status: {result.status_code}")
        print(f"Response Time: {result.response_time_ms:.2f} ms" if result.response_time_ms is not None else "Response Time: None")
        print(f"Error: {result.error}\n")