from onl.sim import Environment
from onl.netdev import Wire
from sender import GBNSender
from receiver import GBNReceiver

seqno_width = 2
window_size = 3
loss_rate = 0.2
timeout = 30.0 
message = "this is ab"
env = Environment()
sender = GBNSender(
    env,
    seqno_width=seqno_width,
    timeout=timeout,
    window_size=window_size,
    message=message,
    debug=True,
)
receiver = GBNReceiver(
    env,
    seqno_width=seqno_width,
    window_size=window_size,
    debug=True
)
wire1 = Wire(env, delay_dist=lambda: 20, loss_rate=0.2)
wire2 = Wire(env, delay_dist=lambda: 20, loss_rate=0.2)
sender.out = wire1
wire1.out = receiver
receiver.out = wire2
wire2.out = sender

env.run(sender.proc)

print(receiver.message)
assert receiver.message == message
