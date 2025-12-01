class Safe:
    MIN_DIAL_POSITION = 0
    MAX_DIAL_POSITION = 100
    _current_position = 0

    def __init__(self, start_position = 0):
        self._current_position = start_position

    def rotate_dial(self, movement: str):
        match movement[:1]:
            case "L":
                return self._rotate_left(int(movement[1:]))
            case "R":
                return self._rotate_right(int(movement[1:]))
            case _ as e:
                raise ValueError(f'{e} is not a valid prefix')

    def _rotate_left(self, count):
        self._current_position = (self._current_position - count % self.MAX_DIAL_POSITION) % self.MAX_DIAL_POSITION

        return self._current_position

    def _rotate_right(self, count):
        self._current_position = (self._current_position + count % self.MAX_DIAL_POSITION) % self.MAX_DIAL_POSITION

        return self._current_position
