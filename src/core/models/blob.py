from dataclasses import dataclass, field
from typing import Optional
import hashlib

from .metadata import Metadata
from .header import Header

@dataclass
class Blob:
    ciphertext: bytes = b''
    signature: Optional[bytes] = None
    metadata: Metadata
    header: Header

    @property
    def blob_id(self) -> bytes:
        data = self.sender_pubkey + self.receiver_pubkey + \
            self.timestamp.to_bytes(8, 'big') + self.nonce
        return hashlib.sha256(data).digest()
