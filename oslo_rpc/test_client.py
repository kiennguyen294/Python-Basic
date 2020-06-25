from oslo_config import cfg
import oslo_messaging as msg


class TestClient(object):
    def __init__(self, transport, target):
        self.transport = transport
        self.target = target
        self._client = msg.RPCClient(self.transport, self.target)

    def test(self):
        cctxt = self._client.prepare(namespace='control', version='2.0')

        #call
        cctxt.call(ctxt={}, method='test', arg='Hello, my name is Kien')
        # Cast
        cctxt.cast(ctxt={}, method='test', arg='I am a beginer Python')

# Authentication with msg.conf

cfg.CONF(['--config-file', 'msg.conf'])
#Create Messaging Transport
transport = msg.get_transport(cfg.CONF)
# Create target
target = msg.Target(topic='kiennn')


# Create RPC client

client = TestClient(transport, target)

# Call Function
client.test()