#!/usr/bin/python3.8

"""Creats a proxy filter that filters proxies based on
some parameters"""

import requests
import csv
from proxyscrape import create_collector, get_collector
from proxyscrape.proxyscrape import Collector
from proxyscrape.shared import Proxy
import concurrent.futures

class Proxy_filter():
    """Filters proxies based on different paramaters
    """

    def __new__(cls, proxies):
        """Check if the parameters passed are equal before 
	creating the instance"""
        if not isinstance(proxies, list):
            return None
        if not all(isinstance(proxy, Proxy) for proxy in proxies):
            return None
        return super().__new__(Proxy_filter)

    def __init__(self, proxies):
        """Stores the prox list as a class variable"""
        self.__proxies = proxies

    def uniqueCountry(self):
        """Returns a list of proxies whose country id unique 
	to each other"""
        proxies = []
        countries = []
        for proxy in self.__proxies:
            if proxy.country not in countries and proxy.country != None:
                countries += [proxy.country]
                proxies += [proxy]
        return proxies

    def workingProxies(self, timeout=3, test_url='https://httpbin.org/ip'):
        """Concurrently checks if the proxies are
	accessible from your network, and returns a list
	of the working once. 

	@timout: could be set to determine the waiting time, 6 is the default
        @test_url: test_url is the site used to test the proxies, 'https://httpbin.org/pi' is the default
	"""
        proxies = []
        def test_proxy(proxy):
            """Takes a proxy object and checks if it works for 
            test_url in timeout time"""
            proxy_port = ":".join([proxy.host, proxy.port])
            try:
                r = requests.get(test_url, proxies={'http':proxy_port, 'https':proxy_port}, timeout=timeout)
                print(r.status_code, r)
                proxies.append(proxy)
            except Exception:
                pass
        with concurrent.futures.ThreadPoolExecutor() as exector:
            exector.map(test_proxy, self.__proxies)
        return proxies

    def get_proxies(self):
        return self.__proxies

    def set_proxies(self, new_proxy_list):
        """set the __proxies private varaibel"""
        if not isinstance(new_proxy_list, list):
            return
        if not all(isinstance(proxy, Proxy) for proxy in new_proxy_list):
            return
        self.__proxies = new_proxy_list
    proxies = property(get_proxies, set_proxies)
       

def export_proxy2csv(proxies, filename="proxies.txt"):
    """Exports proxy object in a proper proxy format to
    a csv file"""
    with open(filename,'w') as proxy_file:
        for proxy in proxies:
            proxy_str = ":".join([proxy.host, proxy.port])
            proxy_file.write(proxy_str)
            proxy_file.write('\n')
def generate_proxys(filename="proxies.txt"):
    """generates and stroes proxies in a text file
    """
    filename = "proxies.txt"
    collector = create_collector('Proxy_collector', ['https', 'http'])
    proxies = collector.get_proxies()
    #print(len(proxies))
    #filterer = Proxy_filter(proxies)
    #working_proxies = filterer.workingProxies()
    #print(len(working_proxies))
    export_proxy2csv(proxies, filename)

if __name__ == '__main__':
    generate_proxys("Noproxy.txt")

