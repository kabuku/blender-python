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


def add_primitives():
    # Add plane
    bpy.ops.mesh.primitive_plane_add()

    # Add cube
    bpy.ops.mesh.primitive_cube_add()

    # Add circle
    bpy.ops.mesh.primitive_circle_add()

    # Add UV sphere
    bpy.ops.mesh.primitive_uv_sphere_add()

    # Add Ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add()

    # Add cylinder
    bpy.ops.mesh.primitive_cylinder_add()

    # Add cone
    bpy.ops.mesh.primitive_cone_add()

    # Add torus
    bpy.ops.mesh.primitive_torus_add()


def add_cone():
    bpy.ops.mesh.primitive_cone_add(
        vertices=6,
        radius1=6,
        radius2=3,
        location=(3, 0, 0),
        rotation=(0.5, 0, 0)
    )


def add_sankon():
    for x in range(3):
        bpy.ops.mesh.primitive_cone_add(
            location=(x, x, 0)
        )


def add_multiple_cone():
    for x in range(32):
        for y in range(32):
            bpy.ops.mesh.primitive_cone_add(
                location=(x, y, 0),
            )


def add_multiple_cone_with_rotation():
    import random
    for x in range(10):
        for y in range(10):
            r1 = random.random()
            r2 = random.random()
            r3 = random.random()
            bpy.ops.mesh.primitive_cone_add(
                location=(x, y, 0),
                rotation=(r1, r2, r3)
            )


if __name__ == "__main__":
    delete_all()
    add_multiple_cone_with_rotation()
