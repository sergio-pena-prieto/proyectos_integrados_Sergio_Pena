#!/usr/bin/env python 
# license removed for brevity
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Mensaje recibido: %s", msg.data)

def memory_suscriber():
    rospy.init_node("suscriptor_basico_sergio", anonymous=True)
    #Nos suscribimos al topic 'numeros' que uso en el ejercicio 1
    rospy.Subscriber("numeros",String,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        memory_suscriber()
    except rospy.ROSInterruptException:
        pass