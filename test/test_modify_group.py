# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_for_delete_group"))
    app.group.modify_group(Group(name="modify_name"))
