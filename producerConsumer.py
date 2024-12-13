import queue
import threading
import requests
from bs4 import BeautifulSoup

QUE = queue.Queue(100)

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
    def __init__(self, que):
        self.que = que

    def consume(self):
       
        res = {}

        output = self.que.get()
        while output is not None:
            
            # print(output) 
            res[output[0]] = [] 

            soup = BeautifulSoup(output[1], 'html.parser')
            links = soup.find_all('a')

            # Get the href attributes
            for link in links:
                res[output[0]].append(link.get('href'))


            output = self.que.get()

        print(res['https://en.wikipedia.org/wiki/San_Francisco'])
        return res.items()
         

def operations(urlsList):

    p = Producer(QUE, urlsList)
    c = Consumer(QUE)

    t1 = threading.Thread(target=p.produce)
    t2 = threading.Thread(target=c.consume)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

# if __name__ == "__main__":

#     operations()
    