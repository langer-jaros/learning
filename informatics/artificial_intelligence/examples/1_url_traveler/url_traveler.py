#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL Traveler - travels by links from one site to another, no jumps.

Author:     Jaroslav Langer
Modified:   2021 Feb 08
"""

import sys
import requests
import re

def get_tlds():
    # Download domains form iana.org
    resp_tlds = requests.request(method='get', url='https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    # Remove first line (date), last line (empty)
    tlds = resp_tlds.text.split('\n')[1:-1]
    return tlds

# def get_url_regex_obj():
#     tlds = get_tlds()
# 
# #     hostname = r'[(http(s)?):\/\/(www\.)?-a-zA-Z0-9@:%._\+~#=]{1,256}'
# #     domains = '|'.join(tlds)                        # domains = '|'.join(domains_list)
# #     path = r'([-a-zA-Z0-9()@:%_\+.~&//=]*)'
# #     query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'
# #
# #     pattern_url = fr'({hostname}\.({domains})\b{path}){query_fragment}'
# 
#     scheme = r'(https?)?:?\/*(www\.)?'
#     host = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}'
#     domains = '|'.join(tlds)
#     path = r'/[-a-zA-Z0-9()@:%_+.~&=/]*'
#     query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'
# 
#     pattern_url = fr'{scheme}({host}\.({domains})\b({path})?){query_fragment}'
# 
#     return re.compile(pattern_url, flags=re.IGNORECASE)

def get_url_regex_obj():
    tlds = get_tlds()

    scheme = r'(https?)?:?\/*(www\.)?'

    sou = r'(\s|\A|\(|\{|\[|\'|\")' # START OF URL''
    user = r'[-a-zA-Z0-9._+~]{1,256}@'
    host = r'[-a-zA-Z0-9._+~]{1,256}'
    port = r':[0-9]{0,5}'
    domains = '|'.join(tlds)
    path = r'/[-a-zA-Z0-9()@:%_+.~&=/]*'
    query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'
    eou = r'(\s|\Z|\)|\}|\]|\'|\")' # END OF URL

    pattern_url = fr'{sou}{scheme}(({user})?{host}({port})?\.({domains})({path})?){query_fragment}{eou}'

    return re.compile(pattern_url, flags=re.IGNORECASE)


class UrlTraveler():
    """Class for URL traveler"""

    url_regex_obj = None
    links = None
    visited = None
    end = None
    ignore_url_inside = '@'
    ignored_url_ends = [
            '.jpg', '.jpeg', '.png', '.ico', '.gif',
            '.css', '.json', '.js', '.php',
            '()', '(',
    ]


    @classmethod
    def travel_rec(cls):
        next_links = set()

        for url in cls.links:
            try:
                response = requests.request(
                        method='get', url=url,
                        # verify=False,
                )
                cls.visited.add(url); print('VISITED:', url)

                findings = cls.url_regex_obj.findall(response.text)

                # links = {f'https://{tup[2]}' for tup in findings}

                links = {f'https://{tup[3][:-1]}' if (tup[3].endswith('/'))
                        else f'https://{tup[3]}'
                                for tup in findings
                }
                # .split("www.", maxsplit=1)[-1].split("//", maxsplit=1)[-1]}'

                if any([cls.end in link for link in links]):
                    print('\n    HEUREKA!\n')
                    end = [link for link in links if (cls.end in link)]
                    print(end)
                    return end

                if any(['CavalryLogger' in link for link in links]):
                    print(response.text)
                    print(findings)
                    print('\n    DESTROY THIS SHIT!\n')
                    end = [link for link in links if ('CavalryLogger' in link)]
                    print(end)
                    return end

                # Add links, with accepted type that are not duplicated
                next_links.update([
                        link for link in links
                                if ((all(not link.endswith(s_type)
                                        for s_type in cls.ignored_url_ends))
                                and ('@' not in link)
                                and (link not in cls.links))
                ])
            except requests.exceptions.SSLError as e:
                print(f"requests.exceptions.SSLError occured, ignored: {e}")
            except requests.exceptions.ConnectionError as e:
                print(f"requests.exceptions.ConnectionError occured, ignored: {e}")
            except requests.exceptions.InvalidURL as e:
                print(f"requests.exceptions.InvalidURL occured, ignored: {e}")
            except UnicodeError as e:
                print(f"UnicodeError occured, ignored: {e}")


        print(next_links)
        # cls.links = next_links
        cls.links = [link for link in next_links if f'.{cls.end_domain}' in link]
        cls.links.extend([link for link in next_links if (link not in cls.links)])

        return cls.travel_rec()


    @classmethod
    def travel(cls, site_start, site_end):
        # print('pattern', pattern_url)
        cls.url_regex_obj = get_url_regex_obj()

        # cls.end = site_end.split('www.', maxsplit=1)[-1].split('//', maxsplit=1)[-1]
        # url = site_start.split('www.', maxsplit=1)[-1].split('//', maxsplit=1)[-1]

        end_groups = cls.url_regex_obj.findall(site_end)[0]
        cls.end = end_groups[3]
        cls.end_domain = end_groups[6]
        url = cls.url_regex_obj.findall(site_start)[0][3]
        url = f'https://{url}'

        cls.links = {url}
        cls.visited = set()

        cls.travel_rec()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
            '-s', '--start', type=str, default='www.fit.cvut.cz',
            help='site from where the travel will be started',

    )
    parser.add_argument(
            '-e', '--end', type=str, default='www.mit.edu',
            help='site where the travel should end',
    )
    parser.add_argument(
            '-d', '--debug', action='store_true', help='run in debug mode',
    )
    parser.add_argument(
            '-m', '--method', default='ids', choices=['ids', 'dfs', 'bfs'],
            help='search algorithm choice',
    )
    parser.add_argument(
            '-w', '--metadata', nargs='?', const=sys.stdout, default=None,
            type=argparse.FileType('w'),
            help='optional file for metadata information',
    )
    parser.add_argument(
            '-o', '--output', nargs=1, type=argparse.FileType('w'),
            default=sys.stdout,
            help='output file, if not given, stdout is used'
    )
    args = parser.parse_args()


    if (args.debug):
        import pdb; pdb.set_trace()

    UrlTraveler.travel(site_start=args.start, site_end=args.end)

