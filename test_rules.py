#!/usr/bin/env python

import subprocess
import json

RULE_TESTER = 'rule_tester'

def run_events(events, rules_dir):

    args = [RULE_TESTER]
    args.extend(['-input_events', json.dumps(events)])
    args.extend(['-rules_directory', rules_dir])

    sp = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()

    print out
    print err


events = [
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 10, 'time': 0},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 20, 'time': 60},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 40, 'time': 120},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 45, 'time': 180},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 45, 'time': 240},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 20, 'time': 300},
    {'host': 'foo.org', 'service': 'requests_rate', 'metric': 10, 'time': 360}]

run_events(events, 'build')
