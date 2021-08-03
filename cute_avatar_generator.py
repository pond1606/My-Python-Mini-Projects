"""Cute Avatar Generator by Phan Huynh Thien Phuc
This program uses the py_avataaars module to create cute avatars.
You can go here: https://github.com/kebu/py-avataaars/ to see more features
and change the attributes (e.g. Try changing SMILE on line 17 to SAD).
Important: Make sure to install GTK or else the program won't work!
(https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)"""

import py_avataaars as pa
avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.BLACK,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    facial_hair_color=pa.HairColor.BLACK,
    top_type=pa.TopType.LONG_HAIR_STRAIGHT2,
    hat_color=pa.Color.BLACK,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.WINK,
    eyebrow_type=pa.EyebrowType.UP_DOWN,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.DEFAULT,
    clothe_type=pa.ClotheType.GRAPHIC_SHIRT,
    clothe_color=pa.Color.BLACK,
    clothe_graphic_type=pa.ClotheGraphicType.PIZZA,
)
avatar.render_png_file('PN.png')