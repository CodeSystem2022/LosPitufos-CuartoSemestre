
import logging as log

log.basicConfig(level= log.INFO,
               format = '%(asctime)s:%s(levelname)s [%(filename)s:%(linemo]s',
               datefmt ='%I:%M:%S %p',
               handlers=[
                   log.fileHandler('capa_datos.log', encodings='utf8'),
                   log.StreamHandler
               ])

if__name__== '__main__':
log.debug('Mensaje a nivel debug')
log.info('Mnesaje a  nivel info')
log.warning('mensaje a nivel warning')
log.error(('mensaje a nivel error'))
