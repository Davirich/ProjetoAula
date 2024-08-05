#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(7):
                    lista_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    lista_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return lista_bg
