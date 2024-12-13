import queue
import threading
import requests
from bs4 import BeautifulSoup

QUE = queue.Queue(100)
RES = {}

class Producer():
    def __init__(self, que, urlList):
        self.session = requests.Session()
        
        self.urlList = urlList
        
        self.que = que
        
    def produce(self):

        for url in self.urlList:
        
            response = self.session.get(url)
            if response.ok:

                self.que.put((url, response.text))

        self.que.put(None)


class Consumer():
    def __init__(self, que, res):
        self.que = que
        self.res = res

    def consume(self):

        output = self.que.get()
        while output is not None:

            self.res[output[0]] = [] 

            soup = BeautifulSoup(output[1], 'html.parser')
            links = soup.find_all('a')

            for link in links:
                self.res[output[0]].append(link.get('href'))


            output = self.que.get()


def operations(urlsList):

    p = Producer(QUE, urlsList)
    c = Consumer(QUE, RES)

    t1 = threading.Thread(target=p.produce)
    t2 = threading.Thread(target=c.consume)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return RES   

# if __name__ == "__main__":

    # print(operations())
    