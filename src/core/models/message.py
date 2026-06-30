from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Message:
    id: Optional[int] = None
    sender_pubkey: str = ''
    receiver_pubkey: str = ''
    content: str = ''
    timestamp: int = 0
    blob_id: str = ''

    @property
    def time_str(self) -> str:
        return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

