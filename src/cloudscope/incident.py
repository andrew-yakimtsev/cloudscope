from enum import Enum

class HealthState(str, Enum):
    HEALTHY = "healthy"
    DEGRADING = "degraded"
    UNHEALTHY = "unhealthy"
    RECOVERING = "recovering"