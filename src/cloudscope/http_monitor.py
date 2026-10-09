import httpx, time, math
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

def monitor_website(
    url: str,
    interval_seconds: float,
    max_checks: int
) -> list[MonitorResult]:

    if interval_seconds <= 0 or not math.isfinite(interval_seconds):
        raise ValueError("Interval must be a finite positive number")

    if type(max_checks) is not int or max_checks <= 0:
        raise ValueError("Maximum checks must be a positive integer")

    results = []

    for i in range(max_checks):
        result = check_website(url)
        results.append(result)

        if i < max_checks - 1:
            time.sleep(interval_seconds)

    return results

if __name__ == "__main__":
    url = "https://www.example.com"

    print(f"Starting monitoring: {url}")

    results = monitor_website(
        url=url,
        interval_seconds=2,
        max_checks=3
    )

    for i, result in enumerate(results, start=1):
        print(f"\nCheck {i}:")
        print(f"  Status: {result.status_code}")

        if result.response_time_ms is not None:
            print(f"  Response Time: {result.response_time_ms:.2f} ms")
        else:
            print("  Response Time: None")

        print(f"  Error: {result.error}")

    print("\nMonitoring complete.")
    print(f"Total checks: {len(results)}")