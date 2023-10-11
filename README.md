## Prototype Plans

The intention of this project is to explore the possibilities of creating a simple keyboard/mouse sharing application. It should provide basic functionality similar to synergy.

High level overview:

- Ability to share keyboard and mouse between client computers.
- Basic configuration to define where screens are positioned relative to one another.
- Basic configuration to define which host's keyboard/mouse is shared.
- When mouse goes across edge of monitor on host 1 it automatically triggers control of pointer on host 2 etc.
- Key and mouse actions transferred over https or sockets?

Questions:

- How can you control a host's mouse or keyboard from software?
- How can you allow the pointer to go off the screen?
- Does any of this require admin (will still require an IT ticket to install on mac if so)
- Is screen scaling something we need to think about, or just hard limits.
- What sets the mouse speed across devices.


### Proposed Structure

Client 1:

- Software running on client communicates to another host with software running on it over specific port
- The client used to connect to another is the `primary` host who's peripherals will be used unless otherwise configured afterwards.


### Packages to research for solution

- mouse
- pyautogui (anything useful in here?)
- 


### The mouse package

Initial exploration of the mouse package yields some useful information.

- The usage to obtain screen position is simple, but obviously stops at edges of screens (at least for now)
- The positions start at x=0 where the mouse is at the left most position and y=o where the mouse is at the highest most position across **all screens** in whatever arrangement they have. As such, for my current arrangement, 0,0 is not accessible onscreen.
- The position coordinates are cumulative for all screens, there is no metadata here to say which screen you are on...

Suggestions based on this information:

- specify where to switch hosts based on specific x,y range as entered into system by a calibration run where the user is guided to outline the limits of their monitors
- when the specified limit is touched, movement is frozen (like in a video game) and captured to be passed to the client on the other host
- failsafes need to be thought up here, such as, special key combination to crash out of the program or a timeout for no respnse from remote system
- the secondary host client needs to be configured similarly before it will accept a connection from a primary host
- when starting the program, it pops up with a count-down to confirm all is working where the use if prompted to test accessing all areas of the screens on both hosts before clicking to keep the configuration

More low-level package `pynput` might be better here as it allows you to block inputs to the system... ah ballax, it only supports up to python3.9..? TBC

`evdev` looks useful for Linux

`kybonet` is a linux only implimentation of a KVM similar to what I'm trying to do so might be a useful reference point, it uses evdev

`interception` is for windows and may work for that side of things... untested as of yet

this is annoyingly looking a little more complicated than I'd hoped...

different packages exist with differing capabilities but often with limitations such as platform and version

an interface based OOP approach may be best here

All we really need is the follow high level API design:

- Capture mouse movements in a blocking fashion on each platform
- Control mouse movements
- define a region of the screen to trigger the context switch between hosts