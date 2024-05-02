class Grouper:
    def __init__(self, url):
        assert isinstance(url, str)
        self.url = url 
        
    def get_group(self):
        parts = self.url.split('//')[-1].split('/')[0].split('.')
        if len(parts) >= 2:
            return '.'.join(parts[-2:])
        return ""

if __name__ == '__main__':
    print("Hello World")
    
    t = Grouper("https://www.example.com")
    print(t.get_group())

    t2 = Grouper("www.subdomain.example.uk")
    print(t2.get_group())
