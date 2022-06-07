These files are deprecated as the discord lib was updated, but i leave them here to remember how they worked.

Essentially, Motion (https://motion-project.github.io/) ran on a raspberry pi with a camera and would send webhooks to a discord channel based on the event, i.e. sensing motion.
The files aboves 'listened' for Motion's webhooks and responded accordingly. 
In short, this 'bot' talks to itself (but really, Motion is talking to python via discord).

Why? Because Discord has no limit to what you can post and seems to store everything forever. This saved a ton of space on my RPi because I could delete the files produced by Motion after they'd been sent to discord (this was handled by a separate process (shell script + cron) that would delete files that were over 1 day old, so there was a little retention period in case the image/video upload failed).

I'm going to revisit and update this someday, lol.
