vel = 61
local_carro = 90

radar_1 = 60
local_1 = 100
radar_range = 1

if vel > radar_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (local_1 - radar_range) and \
    local_carro <= (local_1 + radar_range):
    print('carro multado em radar 1')

#python py.py
#ctrl ; para comentar