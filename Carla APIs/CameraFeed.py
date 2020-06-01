#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time
import cv2
import numpy as np

def process_img(image):
	i=np.array(image.raw_data)
	i2=i.reshape((480,640,4))
	i3=i2[:,:,:3]
	cv2.imshow('',i3)
	cv2.waitKey(1)
	return i3/255.0

actor_list=[]

try:
	client = carla.Client('localhost', 2000)
	client.set_timeout(10.0)
	world = client.get_world()
	blueprint=world.get_blueprint_library()


	car=blueprint.filter('model3')[0]
	print(car)

	spawn_point=random.choice(world.get_map().get_spawn_points())

	vehicle=world.spawn_actor(car,spawn_point)
	vehicle.set_autopilot(True)
	# vehicle.apply_control(carla.VehicleControl(2,0))
	# actor_list.append(vehicle)

	cam_bp=blueprint.find('sensor.camera.rgb')
	cam_bp.set_attribute('image_size_x','640')
	cam_bp.set_attribute('image_size_y','480')
	cam_bp.set_attribute('fov','110')

	pos_camera=carla.Transform(carla.Location(x=.8,z=1.7))
	sensor=world.spawn_actor(cam_bp,pos_camera,attach_to=vehicle)
	actor_list.append(sensor)
	sensor.listen(lambda data: process_img(data))


	time.sleep(10)


finally:
	for actor in actor_list:
		actor.destroy()
		print("all clean")