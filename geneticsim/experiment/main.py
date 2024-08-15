"""The main experiment entry point."""

from experiment_lab.core import run_experiment

from geneticsim.experiment.config import GSConfig, register_configs
from geneticsim.experiment.experiment import GSExperiment


if __name__ == "__main__":
    run_experiment(
        experiment_cls=GSExperiment,
        config_cls=GSConfig,
        register_configs=register_configs,
        config_path=f"./configs",
        config_name="dmsp",
    )