import opendht.aio as dht
import asyncio
import logging

logger = logging.getLogger(__name__)


class DhtNode:
    def __init__(self, identity: dht.Identity | None = None) -> None:
        self.node = dht.DhtRunner()
        self.identity = identity
        self._running = False

    async def run(
        self,
        port: int = 0,
        host: str = "0.0.0.0",
        threaded: bool = True,
    ) -> dht.DhtRunner:
        await self.node.run(
            port=port,
            host=host,
            threaded=threaded,
            identity=self.identity,
        )
        self._running = True
        logger.info("DHT node listening on %s:%d", host, port)
        return self.node

    async def bootstrap(self, host: str, port: int) -> dht.DhtRunner:
        if not self._running:
            await self.run()
        await self.node.bootstrap((host, port))
        logger.info("Bootstrapped from %s:%d", host, port)
        return self.node

    async def join(self, host: str, port: int) -> dht.DhtRunner:
        return await self.bootstrap(host, port)

    async def shutdown(self) -> None:
        if self._running:
            await self.node.shutdown()
            self._running = False
            logger.info("DHT node shut down")
