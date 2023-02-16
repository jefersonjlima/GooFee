# GooFee is a GoogleFeeds for Polybar

A simple library to show the google calendar feed on polybar bar.

## Configuration

In `user_modules.ini` add this code:

```bash
[module/gAgenda]
type = custom/script
; Show the next event and forget cache automatically every 60 minutes
;format-prefix = " "
format-prefix = "%{F#61afef}%{F-} " 
exec = cd $GFEED_PATH && python src/getEvent.py -d 5 -o UPDATE
; left click to launch Google Calendar
click-left = brave https://calendar.google.com/calendar
click-right = notify-send --icon=gtk-info GFeed ""
interval = 900
```
