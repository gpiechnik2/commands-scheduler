# commands-scheduler

A simple tool to run a given command at a specific time. Created to schedule JMeter and k6 performance test runs.

## Installation

Clone the repository.

```bash
git clone https://github.com/gpiechnik2/commands-scheduler.git
```

Enter the repository directory.

```bash
cd commands-scheduler
```

Install the repository locally

```bash
pip install --editable .
```

## Usage

```bash
commands-scheduler --date '28-10-2022 00:26:38' --command 'ls'
```
