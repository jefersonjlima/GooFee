# GooFee is a GoogleFeeds for Polybar 

A simple library to show the google calendar feed on polybar bar.

## Google API
https://developers.google.com/calendar/quickstart/python

1. You need to create a Google API project and download your OAuth 2.0 credentials json file.
You first need to create a project here, then add Google Calendar support, then download the credentials.json file.
2. Download the credentials file to somewhere on your computer.
3. Proceed to installation phase.


## USAGE

In `user_modules.ini` add this code:

```bash
[module/GooFee]
[module/GooFee]
; Show the next event and forget cache automatically every 2 minutes
type = custom/script
format-prefix = "%{F#61afef}%{F-} " 
exec = cd /home/$USER/.config/GooFee && python src/getEvent.py -d 3 -o UPDATE
click-left = firefox https://calendar.google.com/calendar/u/2/r/week
click-right = cd /home/$USER/.config/GooFee && event=$(python src/getEvent.py -o SHOW) && notify-send GooFee "$(echo $event)"
interval = 120
```

Now in `config.ini`:

```bash
modules-center = GooFee
```

after that:

![](figures/coffee.png)

# Contributing
Read our contributing guidelines for how to get started with contributing to GooFee.

## References

- [i3-agenda](Publichttps://github.com/rosenpin/i3-agenda)


