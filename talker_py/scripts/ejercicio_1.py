#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def sergio_publisher():
    rospy.init_node('sergio_publisher', anonymous=True)
    pub = rospy.Publisher('numeros', String, queue_size=10)

    while not rospy.is_shutdown():
        try:
            entrada_usuario=input("Dame un entero para mostrar en pantalla (Ctrl+C para cerrar el programa): ")
            numero=int(entrada_usuario)
            rospy.loginfo("Entero enviado: %d", numero)
            pub.publish(str(numero))
        except ValueError:
            rospy.logwarn("Entrada no valida. Por favor introduce un entero.")

if __name__=="__main__":
    try:
        sergio_publisher()
    except rospy.ROSInterruptException:
        pass