from dataclasses import dataclass, field
import time


@dataclass
class Header:
    version: int = 1
    timestamp: int = field(default_factory = lambda: int(time.time()))
    ttl: int = 300
