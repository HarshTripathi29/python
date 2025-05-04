import asyncio

async def network_call(name, delay):
    print(f"Starting task {name}")
    await asyncio.sleep(delay)
    print(f"finished task {name}")
    return f"{name} completed"

async def main():
    task1 = asyncio.create_task(network_call("function A", 2))
    task2 = asyncio.create_task(network_call("function B", 4))
    task3 = asyncio.create_task(network_call("function C", 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print("Results ", result1, result2, result3)

    print("all tasks finished ")
    
asyncio.run(main())