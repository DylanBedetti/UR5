import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import urlib

def get_next_pose(p):
    assert type(p) is dict
    pose = urlib.poseToList(p)
    print("Received pose: " , pose)
    pose = [-0.18, -0.61, 0.23, 0, 3.12, 0.04];
    return urlib.listToPose(pose);

server = SimpleXMLRPCServer(("192.168.1.6", 50000), allow_none=True)
print("Listening on port 50000...")
server.register_function(get_next_pose, "get_next_pose")
server.serve_forever()