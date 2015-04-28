# -*- coding: utf-8; -*-
#
# Copyright 2015, Kabuku Inc. http://www.kabuku.co.jp
#
# This repository hosts sample codes used in the articles in rinkak (https://www.rinkak.com)
#
# <The article for this code>
# https://www.rinkak.com/blog/blender-python-modeling-1
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


def add_cone():
    bpy.ops.mesh.primitive_cone_add()


if __name__ == "__main__":
    delete_all()
    add_cone()
