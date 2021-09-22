import time

class APIClient:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def __enter__(self):
        # Open connection - takes 1 second
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Handle errors - not shown
        # Close connection - takes 1 second
        time.sleep(1)

    def send(self, data):
        time.sleep(1)
        print('Sent', data)

def main():
    print('started')
    with APIClient('user:Fred, password:Hello') as client:
        print('client created')
        client.send('Hello')
        print('End of context')

    print('Done')

main()
