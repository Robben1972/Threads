import threading
import asyncio

def thread_task():
    while True:
        pass 

threads = []
async def create_thread():
    try:
        while True:
            thread = threading.Thread(target=thread_task)
            thread.start()
            threads.append(thread)
            print(f"Threads created: {len(threads)}")
    except Exception as e:
        print(f"Error occurred: {e}")

async def main():
    await asyncio.gather(create_thread(), create_thread())

if __name__ == "__main__":
    asyncio.run(main())
