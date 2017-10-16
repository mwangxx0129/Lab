Installation and Configuration
## Install

```bash
sudo apt-get install terminator
```

## Configuration

```bash
cd  ~/.config/terminator/ && sudo vim config
```

```
[global_config]
  title_transmit_bg_color = "#d30102"
  focus = system
  suppress_multiple_term_dialog = True
[keybindings]
[profiles]
  [[default]]
    palette = "#2d2d2d:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#d3d0c8:#747369:#f2777a:#99cc99:#ffcc66:#6699cc:#cc99cc:#66cccc:#f2f0ec"
    background_color = "#2D2D2D" # 背景颜色
    background_image = None   
    background_darkness = 0.85 
    cursor_color = "#2D2D2D" # 光标颜色
    cursor_blink = True # 光标是否闪烁
    foreground_color = "#EEE9E9" # 文字的颜色
    use_system_font = False # 是否启用系统字体
    font = Ubuntu Mono 13  # 字体设置，后面的数字表示字体大小
    copy_on_selection = True # 选择文本时同时将数据拷贝到剪切板中
    show_titlebar = False # 不显示标题栏，也就是 terminator 中那个默认的红色的标题栏
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
