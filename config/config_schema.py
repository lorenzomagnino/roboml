"""Configuration schemas using dataclasses for type safety."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ModelConfig:
    """Model architecture configuration."""

    name: str = "default_model"
    hidden_dim: int = 128
    num_layers: int = 2
    activation: str = "relu"


@dataclass
class TrainingConfig:
    """Training hyperparameters configuration."""

    learning_rate: float = 1e-3
    batch_size: int = 32
    num_epochs: int = 100
    optimizer: str = "adam"
    weight_decay: float = 1e-5


@dataclass
class WandbConfig:
    """Wandb configuration."""

    project: str = "roboml-research"
    entity: Optional[str] = None
    mode: str = "online"  # online, offline, disabled
    tags: List[str] = field(default_factory=list)


@dataclass
class Config:
    """Root configuration combining all sub-configs."""

    model: ModelConfig = field(default_factory=ModelConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    wandb: WandbConfig = field(default_factory=WandbConfig)
    seed: int = 42
    device: str = "cpu"  # cpu, cuda, mps
    experiment_name: str = "default_experiment"
