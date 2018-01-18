from ebs_deploy import utcnow_isoformat


def add_arguments(parser):
    """
    adds arguments for the describe events command
    """
    parser.add_argument('-e', '--environment', help='Environment name', required=True)


def execute(helper, config, args):
    """
    Describes recent events for an environment.
    """
    environment_name = args.environment

    (events, next_token) = helper.describe_events(environment_name, start_time=utcnow_isoformat())

    # swap C-Names
    for event in events:
        print("["+event['Severity']+"] "+event['Message'])
