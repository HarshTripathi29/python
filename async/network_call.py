import asyncio

# Define an asynchronous function that simulates a network call
async def network_call(name, delay):
    print(f"Starting task {name}")
    await asyncio.sleep(delay)  # Simulates waiting for a response without blocking
    print(f"Finished task {name}")
    return f"{name} completed"

# Main asynchronous function that runs all tasks
async def main():
    # Create tasks (these start running immediately in the background)
    task1 = asyncio.create_task(network_call("function A", 2))
    task2 = asyncio.create_task(network_call("function B", 4))
    task3 = asyncio.create_task(network_call("function C", 1))

    # Await each task result (they may already be partly/fully completed by now)
    result1 = await task1
    result2 = await task2
    result3 = await task3

    # Print results once all are done
    print("Results:", result1, result2, result3)
    print("All tasks finished.")

# Start the event loop and run the main function
asyncio.run(main())
