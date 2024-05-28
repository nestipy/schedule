from nestipy.common import Module

from app_controller import AppController
from app_service import AppService
from nestipy_schedule.schedule_builder import ScheduleOption
from nestipy_schedule.schedule_module import ScheduleModule


@Module(
    imports=[
        ScheduleModule.for_root(ScheduleOption())
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
