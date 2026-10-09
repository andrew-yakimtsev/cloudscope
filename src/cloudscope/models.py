from dataclasses import dataclass

@dataclass
class MonitorResult:
    url: str
    status_code: int | None
    response_time_ms: float | None
    error: str | None