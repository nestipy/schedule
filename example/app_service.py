from typing import Annotated

from nestipy.common import Injectable
from nestipy.ioc import Inject

from nestipy_schedule import Cron, Interval, Timeout, SchedulerRegistry


@Injectable()
class AppService:
    registry: Annotated[SchedulerRegistry, Inject()]

    @classmethod
    async def get(cls):
        return "test"

    @classmethod
    async def post(cls, data: dict):
        return "test"

    @classmethod
    async def put(cls, id_: int, data: dict):
        return "test"

    @classmethod
    async def delete(cls, id_: int):
        return "test"

    @classmethod
    @Cron("0 0 * * *")  # all day at 00:00
    async def cron(cls):
        print("Running all day at 00:00")

    @classmethod
    @Interval(2)
    async def interval(cls):
        print("Running every 2 seconds")

    @classmethod
    @Timeout(5000)
    async def timeout(cls):
        print("Running after 5 seconds")
