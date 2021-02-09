# Web

`2021 Feb 08, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Domain Name](#domain-name)
* [Uniform Resource Locator (URL)](#uniform-resource-locator-url)
* [Hostname](#hostname)
* [Port](#port)

<!-- /TOC -->

## Domain Name

* [Domain name (wikipedia.org)](https://en.wikipedia.org/wiki/Domain_name)

Any name registered in the Domain Name System (DNS) is a domain name.

All domains are subdomains of the DNS root domain which is nameless.
Top level domains TLDs such as com, org, ...

* [TLD List (wiki.mozilla.org)](https://wiki.mozilla.org/TLD_List)
* [List of TLDs in the root DNS](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

## Uniform Resource Locator (URL)

* [URL (wikipedia.org)](https://en.wikipedia.org/wiki/URL)

```
URI = scheme:[//authority]path[?query][#fragment]
```

```
authority = [userinfo@]host[:port]
```

## Hostname

Hostnames are composed of a sequence of labels concatenated with dots. For example, "en.wikipedia.org" is a hostname. Each label must be from 1-63 characters long. The entire hostname, including the dots, has a maximum of 253 characters.

The Internet standards (Requests for Comments)  specify that labels may contain only `[a-zA-Z0-9]`.

* [Hostname (wikipedia.org)](https://en.wikipedia.org/wiki/Hostname)

## Port

A port number is a 16-bit unsigned integer, thus ranging from 0 to 65535.

* [Port (computer networking)](https://en.wikipedia.org/wiki/Port_(computer_networking))

