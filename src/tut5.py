# -*- coding: utf-8; -*-
#
# Copyright 2015, Kabuku Inc. http://www.kabuku.co.jp
#
# This repository hosts sample codes used in the articles in rinkak (https://www.rinkak.com)
#
# <The article for this code>
# https://www.rinkak.com/blog/blender-python-modeling-5
#

__author__ = "Takuro Wada"
__copyright__ = "Copyright 2015, Kabuku Inc."
__license__ = "MIT"

import bpy


def delete_all():
    for item in bpy.context.scene.objects:
        bpy.context.scene.objects.unlink(item)

    for item in bpy.data.objects:
        bpy.data.objects.remove(item)

    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

    for item in bpy.data.materials:
        bpy.data.materials.remove(item)


def add_cube_by_data():
    mesh = bpy.data.meshes.new('CubeMeshByData')
    obj = bpy.data.objects.new('CubeObjectByData', mesh)
    bpy.context.scene.objects.link(obj)

    vertices = [(x, y, z) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]]

    faces = [
        (4, 5, 1, 0),
        (0, 1, 3, 2),
        (2, 3, 7, 6),
        (6, 7, 5, 4),
        (3, 1, 5, 7),
        (0, 2, 6, 4)
    ]

    mesh.from_pydata(vertices, [], faces)
    mesh.update()


if __name__ == "__main__":
    delete_all()
    add_cube_by_data()

