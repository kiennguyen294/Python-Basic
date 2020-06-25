from oslo_config import cfg
import oslo_messaging as msg

class TestEndpoint(object):
    target = msg.Target(namespace='control', version='2.0')

    def test(self, ctx, arg):
        print('I am testing endpoint of server')
        print(arg)

# Authentication
cfg.CONF(['--config-file', 'msg.conf'])

transport = msg.get_transport(cfg.CONF)
target = msg.Target(topic='kiennn', server='127.0.0.1')

endpoints = [TestEndpoint(), ]

server = msg.get_rpc_server(transport, target, endpoints)

server.start()
server.wait()
