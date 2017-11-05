#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging

def json_for(data):
    """
    Serialize data to JSON.
    """
    return json.dumps(data, indent=4, sort_keys=True)

def save(data, outfile):
    """
    Save data to a file.
    """
    try:
        with open(outfile, 'w') as f:
            f.write(data + '\n')
            logging.warning("Wrote results to %s.", outfile)
    except Exception as e:
        logging.warning(e)
