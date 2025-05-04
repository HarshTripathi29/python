import asyncio

# Simulate sending an email
async def send_email(user, delay):
    print(f"📨 Sending email to {user}...")
    await asyncio.sleep(delay)  # Simulate sending time
    print(f"✅ Email sent to {user}")
    return f"Email to {user} completed"

async def main():
    # Start all email tasks at once
    task1 = asyncio.create_task(send_email("Alice", 2))
    task2 = asyncio.create_task(send_email("Bob", 3))
    task3 = asyncio.create_task(send_email("Charlie", 1))

    # Wait for all of them to finish
    result1 = await task1
    result2 = await task2
    result3 = await task3

    # Print final results
    print("📬 All emails sent!")
    print("Results:", result1, result2, result3)

# Run the async program
asyncio.run(main())
