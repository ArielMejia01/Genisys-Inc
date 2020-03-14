# -*- coding: utf8 -*-
import datetime

class Carro:
    """ Nos representa un carro """
    def __init__ (self, num_placa = "", marca_aut = "", modelo_au = "", tipo_vehiculo = "", hora_ingreso = "", estado = ""):
        """ Inicializamos un vehiculo """
        self.creation_date = datetime.date.today()
        self.numero_placa = num_placa
        self.marca_aut = marca_aut
        self.modelo_au = modelo_au
        self.tipo_vehiculo = tipo_vehiculo
        self.hora_ingreso = datetime.date.today()  
        self.estado = True

    def buscar(self, filter):
        return filter == self.numero_placa






