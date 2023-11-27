from types import TracebackType


class Solution:
    def __init__(self) -> None:
        self.__dirty_water_count: int = 0
        self.__cleen_water_count: int = 0
        self.__total_water_count: int = 0
        self.current_water_in_cleen_volume: int = 0
        self.overflow: bool = False

    def _read_user_input(self) -> str:
        return input()

    def _parse_user_input(self, user_input: str) -> None:
        dirty_water, cleen_water, total_water = user_input.strip().split()
        self.dirty_water_count = dirty_water
        self.cleen_water_count = cleen_water
        self.total_water_count = total_water

    def _check_for_zero_result(self) -> bool:
        return True if self.__cleen_water_count >= self.__dirty_water_count else False

    def _check_for_instantaneous_overflow(self) -> bool:
        return True if self.__total_water_count < self.__dirty_water_count else False

    def _calculate_overflow_result(self) -> int:
        days = 0
        while not self.overflow:
            days += 10
            self.current_water_in_cleen_volume += (
                2 * self.dirty_water_count
            ) - self.cleen_water_count
            if self.current_water_in_cleen_volume > self.__total_water_count:
                self.overflow = True
        return days

    def __call__(self) -> int:
        user_input = self._read_user_input()
        self._parse_user_input(user_input)
        if self._check_for_instantaneous_overflow():
            return 3
        if self._check_for_zero_result():
            return 0
        return self._calculate_overflow_result()

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
    def dirty_water_count(self) -> int:
        return self.__dirty_water_count

    @dirty_water_count.setter
    def dirty_water_count(self, value) -> None:
        self.__dirty_water_count = int(value)

    @property
    def cleen_water_count(self) -> int:
        return self.__cleen_water_count

    @cleen_water_count.setter
    def cleen_water_count(self, value) -> None:
        self.__cleen_water_count = int(value)

    @property
    def total_water_count(self) -> int:
        return self.__total_water_count

    @total_water_count.setter
    def total_water_count(self, value) -> None:
        self.__total_water_count = int(value)


if __name__ == "__main__":
    with Solution() as solution:
        print(solution())
