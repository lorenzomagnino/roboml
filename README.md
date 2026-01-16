#  🧩 RoboML Research Template

A lightweight, opinionated template for running machine learning and robotics research projects. It provides a standardized structure for experiments, data handling, logging, and evaluation, with ready-to-use configs and scripts for reproducible workflows.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-package%20manager-purple.svg)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)



## Projects Built with RoboML Research Template

Projcts that used RoboML template:

<a href="https://github.com/lorenzomagnino/proteinRL" style="display: inline-block; text-decoration: none; border-radius: 3px; overflow: hidden;">
  <span style="display: inline-block; background-color: #24292e; color: white; padding: 4px 8px; font-size: 12px; font-weight: 600; vertical-align: middle;">
    <svg style="vertical-align: text-bottom; fill: currentColor; width: 12px; height: 12px; margin-right: 3px;" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
    GitHub
  </span>
  <span style="display: inline-block; background-color: #2ea44f; color: white; padding: 4px 8px; font-size: 12px; font-weight: 600; vertical-align: middle;">
    lorenzomagnino/proteinRL
  </span>
</a>


Built a project with this template? We'd love to feature it! Please open an issue or submit a pull request.


## Features

- **Hydra Configuration Management**: Modular config structure with separate files for model, training, and wandb settings
- **Type-Safe Configs**: Dataclass schemas for configuration validation and IDE support
- **Wandb Integration**: Built-in experiment tracking and logging
- **Fast Package Management**: Uses `uv` for quick dependency installation
- **Development Tools**: Pre-commit hooks with ruff and black for code quality
- **Auto-formatting**: Ruff automatically formats Python files on save (VS Code/Cursor)

## Setup

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd roboml-research-template
```

2. Install dependencies:
```bash
uv venv
source .venv/bin/activate
make install
```

**Note**: This template installs dependencies directly rather than using `pip install -e ".[dev]"` because it's structured as a template repository, not an installable Python package.

3. (Optional) Install pre-commit hooks:
```bash
make pre-commit-install
```

### Hands on
```bash
python main.py
```

### Configuration

Configuration files are located in the `config/` directory:
- `defaults.yaml`: Main defaults file that imports all configs
- `model.yaml`: Model architecture parameters
- `training.yaml`: Training hyperparameters
- `wandb.yaml`: Wandb project settings
- `config.yaml`: General experiment settings

Override config values via command line:
```bash
python main.py training.learning_rate=0.01 training.batch_size=64
```

### Development

- **Lint code**: `make lint`
- **Format code**: `make format`
- **Run tests**: `make test`
- **Clean cache**: `make clean`

## Project Structure

```
roboml-research-template/
├── config/              # Hydra configuration files
│   ├── config_schema.py # Dataclass schemas
│   ├── defaults.yaml    # Main defaults
│   ├── model.yaml       # Model config
│   ├── training.yaml    # Training config
│   ├── wandb.yaml       # Wandb config
│   └── config.yaml      # General config
├── networks/            # Network architectures
├── learner/             # Learning algorithms
├── tests/               # Test files
└── main.py              # Entry point
```



## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

See LICENSE file for details.
