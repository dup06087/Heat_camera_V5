# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:07:59 2021

@author: USER
"""

import socket
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np

from Cam_number import camera_num

plt.ion()

buf_socket_rx = []
for i in range(camera_num):
    buf_socket_rx.append([])
for i in range(camera_num):
    buf_socket_rx[i].append(0xAA)
    for j in range((24 * 32)):
        buf_socket_rx[i].append(0x00)
    for j in range((2 * 16)):
        buf_socket_rx[i].append(0x00)
    buf_socket_rx[i].append(0xBB)

print_mode = 0  # 0 = temperture # 1 = ascii

min_temp = 15.00
max_temp = 35.00

temperature = np.zeros([camera_num, 24, 32])
# heatmap = np.zeros([24*8,32*8,3])
aux = np.zeros([camera_num, 16])

from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.figure import Figure

thread = QThread()

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Worker(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def get_temperature(self):
        global ClientSocket
        global buf_socket_rx
        global temperature, aux
        # global canvas, chart

        ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_host = '192.168.0.22'
        server_port = 9999

        rx_array = []

        fps = 0
        now_time = time.time()
        while True:
            try:
                ClientSocket.connect((server_host, server_port))

                rx_time_out = time.time()
                while True:
                    rx_char = ClientSocket.recv(1)
                    if len(rx_char) != 0:
                        rx_array.append(rx_char[0])
                        # print(rx_char[0])
                        rx_time_out = time.time()

                    if len(rx_array) >= (2 * ((24 * 32) + (2 * 16) + 1 + 2)):
                        if (rx_array[0] * 0x10 + rx_array[1]) == 0xAA and (
                                rx_array[2 * ((24 * 32) + (2 * 16) + 1 + 1)] * 0x10 + rx_array[
                            2 * ((24 * 32) + (2 * 16) + 1 + 1) + 1]) == 0xBB and (
                                rx_array[2 * ((24 * 32) + (2 * 16) + 1)] * 0x10 + rx_array[
                            2 * ((24 * 32) + (2 * 16) + 1) + 1]) <= 0b1111:
                            # tempture <- rx_array
                            # print((rx_array[2*((24*32)+1)] * 0x10 + rx_array[2*((24*32)+1) + 1]))
                            # print(time.time())

                            slave_address = (rx_array[2 * ((24 * 32) + (2 * 16) + 1)] * 0x10 + rx_array[
                                2 * ((24 * 32) + (2 * 16) + 1) + 1])
                            for i in range(24 * 32):
                                buf_socket_rx[slave_address][1 + i] = (
                                            rx_array[2 * (1 + i)] * 0x10 + rx_array[2 * (1 + i) + 1])
                            for i in range(2 * 16):
                                buf_socket_rx[slave_address][1 + (24 * 32) + i] = (
                                            rx_array[2 * (1 + (24 * 32) + i)] * 0x10 + rx_array[
                                        2 * (1 + (24 * 32) + i) + 1])

                            for h in range(24):
                                for w in range(32):
                                    # temperature[h,w] = (float(buf_socket_rx[0][1+(h*32 + w)])) - 40.0;
                                    temperature[slave_address][h, w] = (float(
                                        buf_socket_rx[slave_address][1 + (h * 32 + w)])) - 40.0;
                            for i in range(16):
                                aux[slave_address][i] = buf_socket_rx[slave_address][1 + (24 * 32) + (2 * i)] * 100 + \
                                                        buf_socket_rx[slave_address][1 + (24 * 32) + (2 * i) + 1]

                            if slave_address == 0b0000:
                                fps = (0.5 * fps) + (0.5 * (1 / (time.time() - now_time)))
                                print(str(fps))
                                for i in range(camera_num):
                                    print("Slave " + str(i) + " (Ch0 ~ Ch3): " + str(aux[i][0]) + ", " + str(
                                        aux[i][1]) + ", " + str(aux[i][2]) + ", " + str(aux[i][3]))
                                    print("Slave " + str(i) + " (Ch4 ~ Ch7): " + str(aux[i][4]) + ", " + str(
                                        aux[i][5]) + ", " + str(aux[i][6]) + ", " + str(aux[i][7]))
                                    print("Slave " + str(i) + " (Ch8 ~ Ch11): " + str(aux[i][8]) + ", " + str(
                                        aux[i][9]) + ", " + str(aux[i][10]) + ", " + str(aux[i][11]))
                                    print("Slave " + str(i) + " (Ch12 ~ Ch15): " + str(aux[i][12]) + ", " + str(
                                        aux[i][13]) + ", " + str(aux[i][14]) + ", " + str(aux[i][15]))
                                now_time = time.time()

                            rx_array = []
                        else:
                            rx_array = rx_array[1:]

                    if time.time() > (rx_time_out + 5.0):
                        break

                ClientSocket.close()
            except:
                print('No reponse from server: ' + str(server_host) + ':' + str(server_port))
                time.sleep(1.0)

                # if time.time() > (rx_time_out + 5.0):
                #     ClientSocket.close()
                #     break


worker = Worker()
worker.moveToThread(thread)
thread.started.connect(worker.get_temperature)

thread_draw_chart = QThread()

canvas = []
chart = []

for i in range(camera_num):
    canvas.append(FigureCanvas(Figure(figsize=(10, 6), tight_layout=True)))
    chart.append(canvas[i].figure.add_subplot())

    heatmap_zero = np.zeros((24 * 8, 32 * 8))

    chart[i].clear()
    chart[i].get_xaxis().set_visible(False)
    chart[i].get_yaxis().set_visible(False)
    chart[i].imshow(heatmap_zero, cmap='jet', vmin=min_temp, vmax=max_temp)

    canvas[i].draw()

child_canvas = []
child_chart = []
for i in range(camera_num):
    child_canvas.append(FigureCanvas(Figure(figsize=(10, 6), tight_layout=True)))
    child_chart.append(child_canvas[i].figure.add_subplot())

    child_chart[i].clear()
    child_chart[i].get_xaxis().set_visible(False)
    child_chart[i].get_yaxis().set_visible(False)
    child_chart[i].imshow(heatmap_zero, cmap='jet', vmin=min_temp, vmax=max_temp)

    child_canvas[i].draw()


class Worker2(QObject):
    def __init__(self, parent=None, camera_num=camera_num):
        QObject.__init__(self, parent=parent)
        self.camera_num = camera_num
        # print("initialiezed")

    def display_plot(self):
        while True:
            try:
                for i in range(camera_num):
                    self.temperature_upscale = cv2.resize(temperature[i], None, fx=8, fy=8,
                                                          interpolation=cv2.INTER_CUBIC)
                    self.temperature_upscale = cv2.flip(self.temperature_upscale, 1)
                    self.child_temperature_upscale = self.temperature_upscale
                    chart[i].clear()

                    chart[i].get_xaxis().set_visible(False)
                    chart[i].get_yaxis().set_visible(False)
                    chart[i].imshow(self.temperature_upscale, cmap='jet', vmin=min_temp, vmax=max_temp)

                    canvas[i].draw()

                    ###child ###여기 지우자
                    child_chart[i].clear()

                    child_chart[i].get_xaxis().set_visible(False)
                    child_chart[i].get_yaxis().set_visible(False)
                    child_chart[i].imshow(self.child_temperature_upscale, cmap='jet', vmin=min_temp, vmax=max_temp)

                    child_canvas[i].draw()


            except:
                pass
            time.sleep(0.1875)


worker_draw_canvas = Worker2(camera_num=camera_num)
worker_draw_canvas.moveToThread(thread_draw_chart)
thread_draw_chart.started.connect(worker_draw_canvas.display_plot)

thread.start()
thread_draw_chart.start()