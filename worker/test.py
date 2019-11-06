from worker.tasks import randomize_image

data = open('/tmp/cat.png', 'rb').read()

out = randomize_image(data)

open('/tmp/a.png', 'wb').write(out)
