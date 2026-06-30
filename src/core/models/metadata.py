from dataclasses import dataclass
from typing import Optional

@dataclass
class Metadata:
    sender_pubkey: bytes = b''
    receiver_pubkey: bytes = b''
    prev_hash: Optional[bytes] = None
    nonce: bytes = b''


