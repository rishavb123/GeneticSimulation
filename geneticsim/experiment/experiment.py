from typing import Any
from experiment_lab.core import BaseExperiment

from geneticsim.experiment.config import GSConfig


class GSExperiment(BaseExperiment):

    def __init__(self, cfg: GSConfig) -> None:
        self.cfg = cfg
        self.initialize_experiment()

    def initialize_experiment(self) -> None:
        super().initialize_experiment()

    def single_run(
        self, run_id: str, run_output_path: str, seed: int | None = None
    ) -> Any:
        pass