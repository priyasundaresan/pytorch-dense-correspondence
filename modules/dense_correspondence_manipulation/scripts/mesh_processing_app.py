#!/usr/bin/env directorPython

import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_dir", type=str, help="(optional) dataset folder to load")
    # parser.add_argument('--current_dir', action='store_true', default=False, help="uses the current director as the data_foler")

    args = parser.parse_args()
    if args.data_dir:
        data_folder = args.data_dir
    else:
        print "running with data_dir set to current working directory . . . "
        data_folder = os.getcwd()


    run(data_folder, config_file=args.config_file)