"""File for all the config and config registration for gs experiments."""

from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from experiment_lab.core import BaseConfig


@dataclass
class GSConfig(BaseConfig):
    """The config for the gs experiment."""

    population_size: int = 1
    n_agents: int = 1
    n_iterations: int = 1
    n_children: int = 1
    keep_top_n: int = 0

    def __post_init__(self) -> None:
        return super().__post_init__()


def register_configs():
    """Registers the configs created."""
    cs = ConfigStore.instance()
    cs.store(name="gs_config", node=GSConfig)
