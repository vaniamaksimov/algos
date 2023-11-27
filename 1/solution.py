from types import TracebackType


class Solution:
    def __init__(self) -> None:
        self.__dirty_water_volume: int = 0
        self.__cleen_water_count: int = 0
        self.__total_water_count: int = 0

    def _read_user_input(self) -> str:
        return input()

    def _parse_user_input(self, user_input: str) -> None:
        user_input = user_input.strip().split()

    def __call__(self) -> int:
        user_input = self._read_user_input()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        ...

    @property
    def dirty_water_volume(self) -> int:
        return self.__dirty_water_volume

    @dirty_water_volume.setter
    def dirty_water_volume(self, value) -> None:
        self.__dirty_water_volume = value

    @property
    def cleen_water_count(self) -> int:
        return self.__cleen_water_count

    @cleen_water_count.setter
    def cleen_water_count(self, value) -> None:
        self.__cleen_water_count = value

    @property
    def total_water_count(self) -> int:
        return self.__total_water_count

    @total_water_count.setter
    def total_water_count(self, value) -> None:
        self.__total_water_count = value


if __name__ == "__main__":
    with Solution() as solution:
        solution()
