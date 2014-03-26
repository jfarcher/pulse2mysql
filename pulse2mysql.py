import mosquitto
import MySQLdb as mdb
import sys

def on_connect(mosq, obj, rc):
    mosq.subscribe("house/power/meter/1/usage", 0)

def on_message(mosq, obj, msg):
    #print(str(msg.payload))

    con = mdb.connect('localhost', 'enmon', 'enm0np455', 'enmon');
    cur = con.cursor()
    cur.execute("UPDATE power_usage SET counter=counter+1 where meter_id='1'")

def on_log(mosq, obj, level, string):
    print(string)

# If you want to use a specific client id, use
# mqttc = mosquitto.Mosquitto("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mosquitto.Mosquitto()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
# Uncomment to enable debug messages
#mqttc.on_log = on_log
mqttc.connect("127.0.0.1", 1883, 60)

#mqttc.subscribe("string", 0)
#mqttc.subscribe(("tuple", 1))
#mqttc.subscribe([("list0", 0), ("list1", 1)])

mqttc.loop_forever()

