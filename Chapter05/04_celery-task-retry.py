# program desc
#   - show fail-retry using some task options
#     - bind, retry_backoff, retry_kwargs
#   - i fix this example to simulate failure easier w/ ZeroDivisionError
# how to run
#   - run this script
#   - run 'celery worker --app 04__celery-task-retry' in other terminal
#   - u'll see 'retry' msg in worker's terminal
#     - but there's no action after that. i'm not sure it's intended.
# todo
#   - add task has self arg, but call wo/ self 'add.delay(4, 4)
#     - i don't know when to use self for celery tasks.
import celery


app = celery.Celery('04_celery-task-retry',
                   broker='redis://localhost',
                   backend='redis://localhost')


@app.task(bind=True, retry_backoff=True,
         retry_kwargs={'max_retries': 5})
def add(self, x, y):                    # ??? self
    try:
        print('self:', self)
        n = x / 0                       # raise intentional error
        return x + y
    # except OverflowError as exc:
    except ZeroDivisionError as exc:
        print('retry')                  # can see this in workers ternimal
        self.retry(exc=exc)             # is this the purpose using 'self'???


if __name__ == '__main__':
    result = add.delay(4, 4)
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)
