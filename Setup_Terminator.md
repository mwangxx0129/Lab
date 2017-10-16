# Terminator
- Installation and Configuration
- Uninstall and clear 

## Install

```bash
sudo apt-get install terminator
```

## Configuration

```bash
cd  ~/.config/terminator/ && sudo vim config
```
### default config
```
[global_config]
  window_state = fullscreen
[keybindings]
[layouts]
  [[default]]
    [[[child1]]]
      parent = window0
      type = Terminal
    [[[window0]]]
      parent = ""
      type = Window
[plugins]
[profiles]
  [[default]]
```

```config
[global_config]
  title_transmit_bg_color = "#d30102"
  focus = system
  suppress_multiple_term_dialog = True
[keybindings]
[profiles]
  [[default]]
    palette = "#2d2d2d:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#d3d0c8:#747369:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#f2f0ec"
    background_color = "#2D2D2D"
    background_image = None   
    background_darkness = 0.85 
    cursor_color = "#2D2D2D"
    # cursor_blink = True
    foreground_color = "#EEE9E9"
    use_system_font = False
    font = Ubuntu Mono 13 
    copy_on_selection = True 
    show_titlebar = False
[layouts]
  [[default]]
    [[[child1]]]
      type = Terminal
      parent = window0
      profile = default
    [[[window0]]]
      type = Window
      parent = ""
[plugins]
```


```
Ctrl+Shift+E    垂直分割窗口
Ctrl+Shift+O    水平分割窗口
F11             全屏
Ctrl+Shift+C    复制
Ctrl+Shift+V    粘贴
Ctrl+Shift+N    或者 Ctrl+Tab 在分割的各窗口之间切换
Ctrl+Shift+X    将分割的某一个窗口放大至全屏使用
Ctrl+Shift+Z    从放大至全屏的某一窗口回到多窗格界面
Ctrl+Shift+W  关闭当前终端
Ctrl+Shift+Q   退出Terminator
Ctrl+Shift+up left right down   扩展当前窗口
```


## Uninstall just terminator
```bash
sudo apt-get remove terminator
```

## Uninstall terminator and its dependencies
```bash
sudo apt-get remove --auto-remove terminator
```

## Purging your config/data too
```
sudo apt-get purge terminator

sudo apt-get purge --auto-remove terminator
```
