# Tmux

Tmux

Author

Benedict Thekkel

## Session

### Create a new session

``` sh
tmux
```

``` sh
tmux new
```

``` sh
tmux new -s <session name>
```

### List Session

``` sh
tmux ls
```

``` sh
tmux list-sessions
```

``` sh
tmux new -s <session name>
```

### Attach Session

``` sh
tmux a
```

``` sh
tmux at
```

``` sh
tmux a -t <session name>
```

### Kill Session

``` sh
tmux kill-session -t <session name>
```

### Rename session

`Ctrl` + `b` `$`

### Detach from session

`Ctrl` + `b` `d`

### Session and Window Preview

`Ctrl` + `b` `w`

### Move to previous session

`Ctrl` + `b` `(`

### Move to next session

`Ctrl` + `b` `)`

## Windows

### Create session with named window

``` sh
tmux new -s mysession -n mywindow
```

### Create new window

`Ctrl` + `b` `c`

### Rename current window

`Ctrl` + `b` `,`

### Close current window

`Ctrl` + `b` `&`

### List window

`Ctrl` + `b` `w`

### Previous window

`Ctrl` + `b` `p`

### Next window

`Ctrl` + `b` `n`

### Switch to window by number

`Ctrl` + `b` `0...9`

## Panes

### Split window vertically

`Ctrl` + `b` `%`

### Split window horizontally

`Ctrl` + `b` `"`

### Navigate panes

`Ctrl` + `b` `up, down, right, left`

### Close current pane

`Ctrl` + `b` `x`

### Move the current pane left

`Ctrl` + `b` `{`

### Move the current pane right

`Ctrl` + `b` `}`

### Switch to next pane

`Ctrl` + `b` `o`

### Show pane numbers

`Ctrl` + `b` `q` `0...9`

### Convert pane to window

`Ctrl` + `b` `!`

### Toggle pane zoom

`Ctrl` + `b` `z`

### Resize pane

`Ctrl` + `b` + `up, down, right, left`

Back to top
