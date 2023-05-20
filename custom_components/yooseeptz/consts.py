##### Common ################################################################################################
ATTR_HOST = "host" # Receives the host inputed in the services
ATTR_PORT = "port" # Receives the port inputed in the services
ATTR_PROTOCOL = "protocol" # Receives the protocol inputed in the services
ATTR_DIRECTION = "direction" # Receives the direction inputed in the services, used in move function
ATTR_DEVICEID= "device_id" # Receives the Device id from the target selector

##### TCP ONLY ##############################################################################################
ATTR_STEPS_X = 'x_steps' # Receives the Steps from Camera creation
ATTR_STEPS_Y = 'y_steps' # Receives the Steps from camera creation
ATTR_PRES_NAME = 'preset_name' # Receives the preset name from HA, used in create_preset function/ go_to_preset
ATTR_PRES_POS_X = 'preset_position_x' #  Receives the preset position from HA, to be stored ( go_to_preset )
ATTR_PRES_POS_Y = 'preset_position_y' # Receives the preset position from HA, to be store ( go_to_preset )
TCP_PTZ_COMMAND = "Content-length: strlen(Content-type)\n" + "Content-type: ptzCmd:" # A default TCP command extracted from wireshark
TCP_PTZ_HEADERS = ( # Default headers extracted from wireshark to make the camera move (TCP)
    "CSeq: 0\n"
    + "LibVLC/2.2.1 (LIVE555 Streaming Media v2014.07.25)\n"
    + "Accept: application/sdp\n"
) 
#### ONVIF ONLY #############################################################################################
ATTR_ONVIF_METHOD = None


#############################################################################################################
DBPATH = 'custom_components/yooseeptz/db/' # Location where the DB is Stored
#############################################################################################################
