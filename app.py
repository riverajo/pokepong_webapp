from __future__ import absolute_import, print_function
from pokepong.app import create_app

app = create_app()
if __name__ == '__main__':
    app.run()
