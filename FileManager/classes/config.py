class Config:
    def __init__(self, properties_file_path=''):
        self.properties_file_path = properties_file_path
        self.urls = {}
        self.properties = {}

    def urls_(self):
        # return dictionary of urls
        try:
            with open(self.properties_file_path) as urlFile:
                for urlString in urlFile:
                    if len(urlString.strip()) > 1 and not urlString.startswith('#') and not urlString.startswith('@'):
                        route, url = urlString.split('=')
                        route = route.strip()
                        url = url.strip()
                        self.urls[route] = url
        except Exception as e:
            print("FileManager.classes.config.config.urls : " + str(e))
            return {}
        return self.urls

    def properties_(self):
        # return dictionary of properties
        try:
            with open(self.properties_file_path) as propertyFile:
                for property_str in propertyFile:
                    if property_str.startswith('@') and len(property_str.strip()) > 1 and not property_str.startswith(
                            '#'):
                        p = property_str.replace('@', '').strip()
                        key, value = p.split('=')
                        key = key.strip()
                        value = value.strip()
                        self.properties[key] = value
        except Exception as e:
            print("FileManager.classes.config.config.properties : " + str(e))
            return {}
        return self.properties
