# LEAKY BUCKET

import time

class LeakyBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity  # Maximum bucket size
        self.rate = rate  # Rate at which the bucket leaks tokens
        self.tokens = 0  # Current number of tokens in the bucket
        self.last_time = time.time()

    def add_token(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_time
        self.tokens = min(self.capacity, self.tokens + time_elapsed * self.rate)
        self.last_time = current_time

    def transmit(self, packet_size):
        if self.tokens >= packet_size:
            self.tokens -= packet_size
            print(f"Transmitted {packet_size} bytes")
            return True
        else:
            print("Dropped - Insufficient tokens")
            return False

if __name__ == "__main__":
    bucket = LeakyBucket(capacity=50, rate=10)  # Example: 50 bytes capacity, 10 bytes/second rate

    for i in range(1, 11):
        print(f"Time: {i} seconds")
        bucket.add_token()
        packet_size = eval(input(" Enter the Packet size : "))  # Example: 15 bytes packet size
        bucket.transmit(packet_size)
