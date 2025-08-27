import asyncio
import time


queue = asyncio.Queue(maxsize=5)

async def producer(customers, items):
    print(f"{time.ctime()} || {customers} has ordered {items}")
    await queue.put((customers, items))

async def consumer(name, work_time):

    while True:
        
        customers = await queue.get()
        try:
            customer_name, customer_item = customers
            print(f"{time.ctime()} || {name}: Working on {customer_name} with items {customer_item}")
            for item in customer_item:
                await asyncio.sleep(work_time)
            print(f"{time.ctime()} || {name}: done with {customer_name}'s order")
        finally:
            queue.task_done()
        print(f"{time.ctime()} || {name} has finished working")


async def main():
    customers = [('Alice', ['Apple', 'Banana', 'Milk']),
             ('Bob', ['Bread', 'Cheese']),
             ('Charlie', ['Eggs','Juice','Butter']),
             ('Ren', ['Burger', 'Fries']),
             ('John', ['Pizza', 'Fish', 'Orange']),
             ('Dave', ['Chocolate', 'Smoothie']),
             ('Edward', ['Milkshake', 'Chicken', 'Rice']),
             ('Fen', ['Hotdog', 'Pudding']),
             ('Gabriel', ['Sundae', 'Crackers', 'Cookies']),
             ('Hal', ['Marshmallow', 'Soda'])
    ]

    cashiers = [
        ("Cashier-1", 1),
        ("Cashier-2", 2)
    ]

    customer_task = [
        asyncio.create_task(producer(name, items)) 
        for name, items in customers
        ]
    cashier_task = [asyncio.create_task(consumer(cash_name, time)) for cash_name, time in cashiers
        ]
    
    await asyncio.gather(*customer_task)
    await queue.join()
    print(f"{time.ctime()} || Store has closed for the day.")    

asyncio.run(main())