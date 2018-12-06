# program desc
#   - using celery in simple way.
#     - creating celery app
#     - creating celery task w/ @app.task
#     - call task w/ delay
#       - delay is most common calling method for tasks
# how to run
#   - run this script
#   - run 'celery worker --app 03_celery-task' in other terminal
#     - app name is the arg of Celery constructor
#     - u should run worker in this module's directory
#       - otherwise u'll get below error
#         ModuleNotFoundError: No module named '03_celery-task'
#     - app name arg should be the same to module name
#       - otherwise u'll get an error
#         celery.exceptions.NotRegistered: 'other-name.add'
#   - if worker is running, this script run fully wo/ waiting
import celery


app = celery.Celery('03_celery-task',       # app name in worker's --app
    broker='redis://localhost',             #   - same to module name
    backend='redis://localhost')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add)  # add is task object

    result = add.delay(4, 4)                # call task, 4, 4 is args for task
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)
