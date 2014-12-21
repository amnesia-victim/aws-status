#!/usr/bin/env python

import argparse
from aws_status import status_page

#main() function that can be used outside the script
def main():
    #parse arguments
    parser = argparse.ArgumentParser(description='List available AWS status feeds')
    parser.add_argument('-r', '--regions', action='store_true', help='only list regions')
    parser.add_argument('-s', '--services', action='store_true', help='only list services')
    args = parser.parse_args()

    if args.regions and args.services:
        raise ValueError("cannot have '--regions' AND '--services' at the same time")

    page = status_page.AWSStatusPage()

    #output the result
    if args.regions:
        items = page.regions
    elif args.services:
        items = page.services
    else:
        items = page.rss_urls

    for i in sorted(items):
        print i

#if the script is launched directly...
if __name__ == "__main__":
    main()
