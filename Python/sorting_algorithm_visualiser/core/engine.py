from core.state import State
from core.constants import ALGO_MAP, DATASET_MAP
from services.audio import play_value

class Engine:
    def __init__(self):
        self.state = State()
 
        self.algo_name: str = "Bubble Sort"
        self.dataset: str = "Random"
        self.speed: float = 1.0
        self.muted: bool = False
        self.running: bool = False
 
        self._generator = None
 
        self.font_sans: int = 0
        self.font_mono: int = 0
 
        self.shuffle()

    def shuffle(self, dataset: str | None = None):
        if dataset is not None:
            self.dataset = dataset
 
        self.state.arr = DATASET_MAP[self.dataset](self.state.n)
        self.state.reset_markers()
        self._reset()

    def set_size(self, n: int):
        self.state.n = n
        self.shuffle()

    def set_dataset(self, dataset: str):
        self.shuffle(dataset)

    def set_algo(self, name: str):
        self.algo_name = name
        self.shuffle()

    def run(self):
        if self.running:
            self._pause()
            return False
        else:
            self.running = True
            return True

    def step(self):
        self._ensure_generator()
        return self._advance()

    def stop(self):
        self._stop()

    def tick(self, frame_count: int) -> bool:
        if not self.running:
            return False
 
        frames_per_step = max(1, int(6 / self.speed))
        if frame_count % frames_per_step != 0:
            return True
 
        self._ensure_generator()
        alive = self._advance()
 
        if not alive:
            self.running = False
 
        return alive

    def _ensure_generator(self):
        if self._generator is None:
            self.state.reset_markers()
            algo_fn = ALGO_MAP.get(self.algo_name)
            self._generator = algo_fn(self.state)

    def _play_active(self):
        for i in self.state.active:
            play_value(self.state.arr[i], self.state.n, self.speed, self.muted)

    def _advance(self) -> bool:
        try:
            next(self._generator)
            self._play_active()
            return True
        except StopIteration:
            self._generator = None
            self.state.active.clear()
            return False

    def _stop(self):
        self.running = False

    def _pause(self):
        self.running = False
        self.state.active.clear()

    def _reset(self):
        self.running = False
        self.state.active.clear()
        self._generator = None

engine = Engine()
