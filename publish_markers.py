#!/usr/bin/env python
import rospy

from visualization_msgs.msg import Marker

rospy.init_node("publish_markers")

meter_pub = rospy.Publisher('meter_scale_marker', Marker)
decimeter_pub = rospy.Publisher('decimeter_scale_marker', Marker)
centimeter_pub = rospy.Publisher('centimeter_scale_marker', Marker)
inch_pub = rospy.Publisher('inch_scale_marker', Marker)
r = rospy.Rate(10)
while not rospy.is_shutdown():
    mesh_marker = Marker()

    mesh_marker.header.frame_id = "test"
    mesh_marker.header.stamp = rospy.Time.now()
    mesh_marker.scale.x = 1.0
    mesh_marker.scale.y = 1.0
    mesh_marker.scale.z = 1.0

    mesh_marker.type = Marker.MESH_RESOURCE

    mesh_marker.mesh_resource = "package://rviz_issue_853/collada_unit_meter.dae"
    mesh_marker.pose.position.x = 2.0
    mesh_marker.mesh_use_embedded_materials = True
    meter_pub.publish(mesh_marker)

    mesh_marker.mesh_resource = "package://rviz_issue_853/collada_unit_decimeter.dae"
    mesh_marker.pose.position.x = 1.0
    decimeter_pub.publish(mesh_marker)

    mesh_marker.mesh_resource = "package://rviz_issue_853/collada_unit_centimeter.dae"
    mesh_marker.pose.position.x = 0.0
    centimeter_pub.publish(mesh_marker)

    mesh_marker.mesh_resource = "package://rviz_issue_853/collada_unit_inch.dae"
    mesh_marker.pose.position.x = -1.0
    inch_pub.publish(mesh_marker)

    r.sleep()
