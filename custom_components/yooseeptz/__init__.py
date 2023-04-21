DOMAIN = "yooseeptz"

#############################################################################################################

import socket
from pathlib import Path
import json
import logging
import time
from .consts import *

#############################################################################################################
_LOGGER = logging.getLogger(__name__) # Logger

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""


    if not Path(DBPATH).is_dir(): # Check if dir is bd dir is not present
        Path(DBPATH).mkdir() # if not present, create it
        
    
    def add_camera_ptz(call):
        host = call.data.get(ATTR_HOST) # get host from HA service
        port = call.data.get(ATTR_PORT) # get port from HA service
        port = int(port) # convert port to int
        protocol = call.data.get(ATTR_PROTOCOL) # get protocol from HA service
        device_id = call.data.get(ATTR_DEVICEID) # get device_id from HA service
        steps_x = call.data.get(ATTR_STEPS_X) # get steps from HA service
        steps_y = call.data.get(ATTR_STEPS_Y) # get steps from HA service
        if not call.data.get(ATTR_ONVIF_METHOD) == None:
            method = call.data.get(ATTR_ONVIF_METHOD)
        else:
            method = None

        device_qnt = range(len(device_id)) # Device quantity is the range of the device id quantity, used to make a counter, if multiple cameras are selected.

        for devices in device_qnt: # a loop for each device selected
            with open(DBPATH + device_id[devices] + '.json','a+') as f: # create the DB
                try:
                    device = json.load(f) # Try to load if it's already existing
                except:
                    device = {} # create an empty dict to be used
                if not method:
                    device.update({'camera':{\
                        'host': host,\
                            'port': port,\
                                'protocol': protocol,\
                                    'steps_x': steps_x,\
                                        'steps_y': steps_y\
                        }})  # Update the dict with the new keys and coordinates
                else:
                    device.update({'camera':{\
                        'host': host,\
                            'port': port,\
                                'protocol': protocol,\
                                    'method':method,\
                                        'steps_x': steps_x,\
                                            'steps_y': steps_y\
                        }})  # Update the dict with the new keys and coordinates
                    
                f.close() # Close the file
                Path(DBPATH+device_id[devices]+'.json').unlink() # Delete the previous file
                f = open(DBPATH + device_id[devices] + '.json','a') # Open a new one
                json.dump(device, f, ensure_ascii=False, indent=4) # Paste all the contents in the new one


    def move(call):
        """Handle the service call."""

        device_id = call.data.get(ATTR_DEVICEID) 
        direction = call.data.get(ATTR_DIRECTION)
        device_qnt = range(len(device_id))
        
        for devices in device_qnt: # executes the function for every device
            f = open(DBPATH + device_id[devices] + '.json')
            device = dict(json.load(f))
            device_camera = device.get('camera')
            protocol = device_camera.get('protocol') 
            host =  device_camera.get('host')
            port = device_camera.get('port')
            
            if protocol == "ONVIF":
                ...

            if protocol == "TCP":

                move_str = ( # TCP String used to make the request
                    f"SET_PARAMETER rtsp://{host}/onvif1 RTSP/1.0\n"
                    + TCP_PTZ_HEADERS
                    + TCP_PTZ_COMMAND
                    + direction
                )
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # TCP Requester
                    s.connect((host, port))
                    s.sendall(bytes(move_str, "utf-8"))
                    data = s.recv(1024) # Recieved data TODO make the logger work.


    
    def clear_db(call):
        device_id = call.data.get(ATTR_DEVICEID)
        device_qnt = range(len(device_id))
        
        for devices in device_qnt:
            device_index = int(devices)
            if Path(DBPATH + device_id[device_index] + '.json').exists():
                Path(DBPATH + device_id[device_index] + '.json').unlink()
        
    def go_to_preset(call):
        device_id = call.data.get(ATTR_DEVICEID) 
        preset_name = call.data.get(ATTR_PRES_NAME)
        device_qnt = range(len(device_id))

        for devices in device_qnt:
            f = open(DBPATH + device_id[devices] + '.json')
            device = dict(json.load(f))
            device_camera = device.get('camera')
            preset = device.get(preset_name)
            protocol = device_camera.get('protocol')
            host =  device_camera.get('host')
            port = device_camera.get('port')
            steps_x = device_camera.get('steps_x')
            steps_y = device_camera.get('steps_y')
            pres_pos_x = preset.get('preset_pos_x')
            pres_pos_y = preset.get('preset_pos_y')
        if not steps_x == None and not steps_y == None:
            for devices in device_qnt:
                for steps in range(steps_x): # Move to the most left of the camera
                    f = open(DBPATH + device_id[devices] + '.json')
                    device = dict(json.load(f))
                    device_camera = device.get('camera')
                    protocol = device_camera.get('protocol') 
                    host =  device_camera.get('host')
                    port = device_camera.get('port')
                    
                    if protocol == "ONVIF":
                        ...

                    if protocol == "TCP":

                        move_str = ( # TCP String used to make the request
                            f"SET_PARAMETER rtsp://{host}/onvif1 RTSP/1.0\n"
                            + TCP_PTZ_HEADERS
                            + TCP_PTZ_COMMAND
                            + 'RIGHT'
                        )
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # TCP Requester
                            s.connect((host, port))
                            s.sendall(bytes(move_str, "utf-8"))
                            time.sleep(0.25)
                for steps in range(steps_y): # Move to the most up place of the camera
                    f = open(DBPATH + device_id[devices] + '.json')
                    device = dict(json.load(f))
                    device_camera = device.get('camera')
                    protocol = device_camera.get('protocol') 
                    host =  device_camera.get('host')
                    port = device_camera.get('port')
                    
                    if protocol == "ONVIF":
                        ...

                    if protocol == "TCP":

                        move_str = ( # TCP String used to make the request
                            f"SET_PARAMETER rtsp://{host}/onvif1 RTSP/1.0\n"
                            + TCP_PTZ_HEADERS
                            + TCP_PTZ_COMMAND
                            + 'UP'
                        )
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # TCP Requester
                            s.connect((host, port))
                            s.sendall(bytes(move_str, "utf-8"))
                            time.sleep(0.25)
                for steps in range(pres_pos_x): # move to the preset position (X)
                    f = open(DBPATH + device_id[devices] + '.json')
                    device = dict(json.load(f))
                    device_camera = device.get('camera')
                    protocol = device_camera.get('protocol') 
                    host =  device_camera.get('host')
                    port = device_camera.get('port')
                    
                    if protocol == "ONVIF":
                        ...

                    if protocol == "TCP":

                        move_str = ( # TCP String used to make the request
                            f"SET_PARAMETER rtsp://{host}/onvif1 RTSP/1.0\n"
                            + TCP_PTZ_HEADERS
                            + TCP_PTZ_COMMAND
                            + 'LEFT'
                        )
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # TCP Requester
                            s.connect((host, port))
                            s.sendall(bytes(move_str, "utf-8"))
                            time.sleep(0.25)
                for steps in range(pres_pos_y): # Move to the preset position (Y)
                    f = open(DBPATH + device_id[devices] + '.json')
                    device = dict(json.load(f))
                    device_camera = device.get('camera')
                    protocol = device_camera.get('protocol') 
                    host =  device_camera.get('host')
                    port = device_camera.get('port')
                    
                    if protocol == "ONVIF":
                        ...

                    if protocol == "TCP":

                        move_str = ( # TCP String used to make the request
                            f"SET_PARAMETER rtsp://{host}/onvif1 RTSP/1.0\n"
                            + TCP_PTZ_HEADERS
                            + TCP_PTZ_COMMAND
                            + 'DWON'
                        )
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # TCP Requester
                            s.connect((host, port))
                            s.sendall(bytes(move_str, "utf-8"))
                            time.sleep(0.25)
        _LOGGER.error('Steps X and Steps Y must be defined to use Presets')
        raise Exception('Steps X and Steps Y must be defined to use Presets')
            
        


    def create_preset(call):
        device_id = call.data.get(ATTR_DEVICEID) 
        preset_name = call.data.get(ATTR_PRES_NAME)
        preset_pos_x = call.data.get(ATTR_PRES_POS_X)
        preset_pos_y =  call.data.get(ATTR_PRES_POS_Y)
        device_qnt = range(len(device_id))
        
        for devices in device_qnt:
             with open(DBPATH + device_id[devices] + '.json','r') as f:
                device = dict(json.load(f))
                device.update({preset_name:{\
                    'preset_pos_x': preset_pos_x,\
                        'preset_pos_y': preset_pos_y\
                            }})
                f.close()
                Path(DBPATH+device_id[devices]+'.json').unlink()
                f = open(DBPATH + device_id[devices] + '.json','a')
                json.dump(device, f, ensure_ascii=False, indent=4)

    hass.services.register(DOMAIN, "add_camera_ptz", add_camera_ptz)
    hass.services.register(DOMAIN, "clear_db", clear_db)
    hass.services.register(DOMAIN, "move", move)
    hass.services.register(DOMAIN, "create_preset", create_preset)
    hass.services.register(DOMAIN, "go_to_preset", go_to_preset)


    # Return boolean to indicate that initialization was successful.
    return True
