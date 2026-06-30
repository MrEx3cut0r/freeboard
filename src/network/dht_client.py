import opendht.aio as dht
from ..core.models.blob import Blob

class DhtClient:
    def __init__(self, node: dht.DhtRunner) -> None:
        self.node = node

    async def get(self, key):
        key_hash = dht.InfoHash.get(key)
        return await self.node.getAll(key_hash)

    async def put(self, key, value) -> None:
        key_hash = dht.InfoHash.get(key)
        await self.node.put(key_hash, dht.Value(bytes(value)))

