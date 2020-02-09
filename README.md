# tmux-helper

Scripts to run a little complex commands on tmux.

## How to use

1. Add `export HARUKAM_ENV="<env-name>"` to `~/.bash_profile`, then re-login.

```
<env-name> := HOME_DESKTOP # my desktop pc at home
            | HOME_ASUS    # my asus laptop at home
            | HOME_MAC     # my mac laptop at home
            | OFFICE       # at office
```

2. Add lines to `~/.tmux.conf` like as follows.

```
bind-key -T prefix Space run-shell "python <dir-path>/tmux-helper/main.py <command-name>"
```
