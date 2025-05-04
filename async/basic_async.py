import asyncio

# Define an async function that waits for 2 seconds
async def wait_and_print():
    print("Start")               # This prints immediately
    await asyncio.sleep(2)       # This waits for 2 seconds asynchronously
    print("End")                 # Prints after the wait

# Run the async function using asyncio.run
asyncio.run(wait_and_print())
