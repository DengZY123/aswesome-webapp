import asyncio

import www.orms
from www.models import User, Blog, Comment

def test(loop):
    yield from www.orms.create_pool(loop=loop,user='root', password='123456', database='test')

    u = User(name='wang', email='qq@example.com', passwd='123456', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
for x in test(loop):
    pass
loop.close()
