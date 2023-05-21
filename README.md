# Yoosee PTZ ( TCP Only)

This custom component allows you control chinese cameras that don't fully comply with the ONVIF protocol.

This is a fork from original project available at https://github.com/carvalr/PTZ-YALL

I wanted to chinese cameras that don't work well with onvif and update the component for those that don't comply with onvif.

Apparently, these cameras do not fully comply with the ONVIF protocol and the Home Assistant integration cannot integrate them at the moment.

This is a solution to use the pan and tilt functions into Home Assistant cards.

All of these data was obtained using Wireshark.

## Disclaimer
**I only own a Yoosee , GWIPC marked camera, so if this component don't work for your camera you need to provide all the necessary data for further updates.**
**I cannot verify which cameras work, please test and open an issue telling me your experience, with the model of the camera and type of protocol**
## Considerations
1. GWIPC cameras do not require user and password to connect to PTZ TCP controls.
2. Presets are manually configured in a local json database and are not synced with the app.
3. TCP will work based in manually defined steps, so it's up to the user to figure out how many steps a camera does.
4. **This component does not integrate the video signal from your cameras, only the pan and tilt functions.**

## Setup
Download the files provided in this github and extract the folder yooseeptz inside custom_components and you should be ready to go. 
## Services
This custom component creates several services with domain yoosee_ptz. To obtain information about these services you can use “Developer Tools” > Services. It will have detailed information about the arguments to call each service.

## Camera Entity

You should use with motionEye cameras .[motionEye](https://www.home-assistant.io/integrations/motioneye/).

The MotionEye camera id will be used to add cameras.
