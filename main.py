import click
from src.scheduler import schedule_command


@click.version_option('1.0')
@click.command()
@click.option('--date', '-d', type=str,
              help='The date of running the indicated command in the format: dd-mm-YYYY HH:MM:SS. For example: 28-10-2022 00:10:40.')
@click.option('--command', '-c', type=str,
              help='Command that will be run after the indicated time.')
def schedule(date, command):
    """commands-scheduler

    A simple tool to run a given command at a specific time. Created to schedule JMeter and k6 performance test runs.
    """
    if not date:
        print("Point the date via the '--date' or '-d' option.")
        quit()
    if not command:
        print("Point the command via the '--command' or '-c' option.")
        quit()
    schedule_command(date, command)

if __name__ == '__main__':
    schedule()
