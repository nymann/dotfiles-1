c_bg = "#282828"
c_fg = "#dbdbb2"
c_bg_hl = "#504945"
c_fg_hl = "#fbf1c7"
c_bg_red = "#cc241d"
c_fg_red = "#fb4934"
c_bg_green = "#98971a"
c_fg_green = "#b8bb26"
c_bg_yellow = "#d79921"
c_fg_yellow = "#fabd2f"
c_bg_blue = "#458588"
c_fg_blue = "#83a598"
c_bg_purple = "#b16286"
c_fg_purple = "#d3869b"

# Aliases
c.aliases["tor-on"] = "set content.proxy socks://localhost:9050/"

# UA
config.set("content.headers.user_agent", "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}", "https://web.whatsapp.com/")
config.set("content.headers.user_agent", "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0", "https://accounts.google.com/*")
config.set("content.headers.user_agent", "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36", "https://*.slack.com/*")
config.set("content.headers.user_agent", "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0", "https://docs.google.com/*")

# Content flags
config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "qute://*/*")

# Bindings
config.bind("yp", "spawn mpv --force-window yes {url}")
config.bind("yh", "hint links spawn mpv --force-window yes {hint-url}")
config.bind(";", "set-cmd-text :")
config.bind("<Ctrl-s>", "download")
config.bind("<Ctrl-i>", "inspector")
config.bind(".", "tab-next")
config.bind(",", "tab-prev")
config.bind("<Ctrl-Shift-p>", "spawn --userscript ~/.scripts/qute-bitwarden")
config.bind(" z", "spawn --userscript ~/.scripts/qute-goyo")
# config.bind(""", "enter-mode jump_mark")
# config.bind("+", "zoom-in")
# config.bind("-", "zoom-out")
# config.bind(".", "repeat-command")
# config.bind("/", "set-cmd-text /")
# config.bind(":", "set-cmd-text :")
# config.bind(";I", "hint images tab")
# config.bind(";O", "hint links fill :open -t -r {hint-url}")
# config.bind(";R", "hint --rapid links window")
# config.bind(";Y", "hint links yank-primary")
# config.bind(";b", "hint all tab-bg")
# config.bind(";d", "hint links download")
# config.bind(";f", "hint all tab-fg")
# config.bind(";h", "hint all hover")
# config.bind(";i", "hint images")
# config.bind(";o", "hint links fill :open {hint-url}")
# config.bind(";r", "hint --rapid links tab-bg")
# config.bind(";t", "hint inputs")
# config.bind(";y", "hint links yank")
# config.bind("<Alt-1>", "tab-focus 1")
# config.bind("<Alt-2>", "tab-focus 2")
# config.bind("<Alt-3>", "tab-focus 3")
# config.bind("<Alt-4>", "tab-focus 4")
# config.bind("<Alt-5>", "tab-focus 5")
# config.bind("<Alt-6>", "tab-focus 6")
# config.bind("<Alt-7>", "tab-focus 7")
# config.bind("<Alt-8>", "tab-focus 8")
# config.bind("<Alt-9>", "tab-focus -1")
# config.bind("<Alt-m>", "tab-mute")
# config.bind("<Ctrl-A>", "navigate increment")
# config.bind("<Ctrl-Alt-p>", "print")
# config.bind("<Ctrl-B>", "scroll-page 0 -1")
# config.bind("<Ctrl-D>", "scroll-page 0 0.5")
# config.bind("<Ctrl-F5>", "reload -f")
# config.bind("<Ctrl-F>", "scroll-page 0 1")
# config.bind("<Ctrl-N>", "open -w")
# config.bind("<Ctrl-PgDown>", "tab-next")
# config.bind("<Ctrl-PgUp>", "tab-prev")
# config.bind("<Ctrl-Q>", "quit")
# config.bind("<Ctrl-Return>", "follow-selected -t")
# config.bind("<Ctrl-Shift-N>", "open -p")
# config.bind("<Ctrl-Shift-T>", "undo")
# config.bind("<Ctrl-Shift-Tab>", "nop")
# config.bind("<Ctrl-Shift-W>", "close")
# config.bind("<Ctrl-T>", "open -t")
# config.bind("<Ctrl-Tab>", "tab-focus last")
# config.bind("<Ctrl-U>", "scroll-page 0 -0.5")
# config.bind("<Ctrl-V>", "enter-mode passthrough")
# config.bind("<Ctrl-W>", "tab-close")
# config.bind("<Ctrl-X>", "navigate decrement")
# config.bind("<Ctrl-^>", "tab-focus last")
# config.bind("<Ctrl-h>", "home")
# config.bind("<Ctrl-p>", "tab-pin")
# config.bind("<Ctrl-s>", "stop")
# config.bind("<Escape>", "clear-keychain ;; search ;; fullscreen --leave")
# config.bind("<F11>", "fullscreen")
# config.bind("<F5>", "reload")
# config.bind("<Return>", "follow-selected")
# config.bind("<back>", "back")
# config.bind("<forward>", "forward")
# config.bind("=", "zoom")
# config.bind("?", "set-cmd-text ?")
# config.bind("@", "run-macro")
# config.bind("B", "set-cmd-text -s :quickmark-load -t")
# config.bind("D", "tab-close -o")
# config.bind("F", "hint all tab")
# config.bind("G", "scroll-to-perc")
# config.bind("H", "back")
# config.bind("J", "tab-next")
# config.bind("K", "tab-prev")
# config.bind("L", "forward")
# config.bind("M", "bookmark-add")
# config.bind("N", "search-prev")
# config.bind("O", "set-cmd-text -s :open -t")
# config.bind("PP", "open -t -- {primary}")
# config.bind("Pp", "open -t -- {clipboard}")
# config.bind("R", "reload -f")
# config.bind("Sb", "open qute://bookmarks#bookmarks")
# config.bind("Sh", "open qute://history")
# config.bind("Sq", "open qute://bookmarks")
# config.bind("Ss", "open qute://settings")
# config.bind("T", "tab-focus")
# config.bind("ZQ", "quit")
# config.bind("ZZ", "quit --save")
# config.bind("[[", "navigate prev")
# config.bind("]]", "navigate next")
# config.bind("`", "enter-mode set_mark")
# config.bind("ad", "download-cancel")
# config.bind("b", "set-cmd-text -s :quickmark-load")
# config.bind("cd", "download-clear")
# config.bind("co", "tab-only")
# config.bind("d", "tab-close")
# config.bind("f", "hint")
# config.bind("g$", "tab-focus -1")
# config.bind("g0", "tab-focus 1")
# config.bind("gB", "set-cmd-text -s :bookmark-load -t")
# config.bind("gC", "tab-clone")
# config.bind("gD", "tab-give")
# config.bind("gO", "set-cmd-text :open -t -r {url:pretty}")
# config.bind("gU", "navigate up -t")
# config.bind("g^", "tab-focus 1")
# config.bind("ga", "open -t")
# config.bind("gb", "set-cmd-text -s :bookmark-load")
# config.bind("gd", "download")
# config.bind("gf", "view-source")
# config.bind("gg", "scroll-to-perc 0")
# config.bind("gi", "hint inputs --first")
# config.bind("gl", "tab-move -")
# config.bind("gm", "tab-move")
# config.bind("go", "set-cmd-text :open {url:pretty}")
# config.bind("gr", "tab-move +")
# config.bind("gt", "set-cmd-text -s :buffer")
# config.bind("gu", "navigate up")
# config.bind("h", "scroll left")
# config.bind("i", "enter-mode insert")
# config.bind("j", "scroll down")
# config.bind("k", "scroll up")
# config.bind("l", "scroll right")
# config.bind("m", "quickmark-save")
# config.bind("n", "search-next")
# config.bind("o", "set-cmd-text -s :open")
# config.bind("pP", "open -- {primary}")
# config.bind("pp", "open -- {clipboard}")
# config.bind("q", "record-macro")
# config.bind("r", "reload")
# config.bind("sf", "save")
# config.bind("sk", "set-cmd-text -s :bind")
# config.bind("sl", "set-cmd-text -s :set -t")
# config.bind("ss", "set-cmd-text -s :set")
# config.bind("tIH", "config-cycle -p -u *://*.{url:host}/* content.images ;; reload")
# config.bind("tIh", "config-cycle -p -u *://{url:host}/* content.images ;; reload")
# config.bind("tIu", "config-cycle -p -u {url} content.images ;; reload")
# config.bind("tPH", "config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload")
# config.bind("tPh", "config-cycle -p -u *://{url:host}/* content.plugins ;; reload")
# config.bind("tPu", "config-cycle -p -u {url} content.plugins ;; reload")
# config.bind("tSH", "config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload")
# config.bind("tSh", "config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload")
# config.bind("tSu", "config-cycle -p -u {url} content.javascript.enabled ;; reload")
# config.bind("th", "back -t")
# config.bind("tiH", "config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload")
# config.bind("tih", "config-cycle -p -t -u *://{url:host}/* content.images ;; reload")
# config.bind("tiu", "config-cycle -p -t -u {url} content.images ;; reload")
# config.bind("tl", "forward -t")
# config.bind("tpH", "config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload")
# config.bind("tph", "config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload")
# config.bind("tpu", "config-cycle -p -t -u {url} content.plugins ;; reload")
# config.bind("tsH", "config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload")
# config.bind("tsh", "config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload")
# config.bind("tsu", "config-cycle -p -t -u {url} content.javascript.enabled ;; reload")
# config.bind("u", "undo")
# config.bind("v", "enter-mode caret")
# config.bind("wB", "set-cmd-text -s :bookmark-load -w")
# config.bind("wO", "set-cmd-text :open -w {url:pretty}")
# config.bind("wP", "open -w -- {primary}")
# config.bind("wb", "set-cmd-text -s :quickmark-load -w")
# config.bind("wf", "hint all window")
# config.bind("wh", "back -w")
# config.bind("wi", "inspector")
# config.bind("wl", "forward -w")
# config.bind("wo", "set-cmd-text -s :open -w")
# config.bind("wp", "open -w -- {clipboard}")
# config.bind("xO", "set-cmd-text :open -b -r {url:pretty}")
# config.bind("xo", "set-cmd-text -s :open -b")
# config.bind("yD", "yank domain -s")
# config.bind("yM", "yank inline [{title}]({url}) -s")
# config.bind("yP", "yank pretty-url -s")
# config.bind("yT", "yank title -s")
# config.bind("yY", "yank -s")
# config.bind("yd", "yank domain")
# config.bind("ym", "yank inline [{title}]({url})")
# config.bind("yp", "yank pretty-url")
# config.bind("yt", "yank title")
# config.bind("yy", "yank")
# config.bind("{{", "navigate prev -t")
# config.bind("}}", "navigate next -t")

## Bindings for caret mode
# config.bind("$", "move-to-end-of-line", mode="caret")
# config.bind("0", "move-to-start-of-line", mode="caret")
# config.bind("<Ctrl-Space>", "drop-selection", mode="caret")
# config.bind("<Escape>", "leave-mode", mode="caret")
# config.bind("<Return>", "yank selection", mode="caret")
# config.bind("<Space>", "toggle-selection", mode="caret")
# config.bind("G", "move-to-end-of-document", mode="caret")
# config.bind("H", "scroll left", mode="caret")
# config.bind("J", "scroll down", mode="caret")
# config.bind("K", "scroll up", mode="caret")
# config.bind("L", "scroll right", mode="caret")
# config.bind("Y", "yank selection -s", mode="caret")
# config.bind("[", "move-to-start-of-prev-block", mode="caret")
# config.bind("]", "move-to-start-of-next-block", mode="caret")
# config.bind("b", "move-to-prev-word", mode="caret")
# config.bind("c", "enter-mode normal", mode="caret")
# config.bind("e", "move-to-end-of-word", mode="caret")
# config.bind("gg", "move-to-start-of-document", mode="caret")
# config.bind("h", "move-to-prev-char", mode="caret")
# config.bind("j", "move-to-next-line", mode="caret")
# config.bind("k", "move-to-prev-line", mode="caret")
# config.bind("l", "move-to-next-char", mode="caret")
# config.bind("o", "reverse-selection", mode="caret")
# config.bind("v", "toggle-selection", mode="caret")
# config.bind("w", "move-to-next-word", mode="caret")
# config.bind("y", "yank selection", mode="caret")
# config.bind("{", "move-to-end-of-prev-block", mode="caret")
# config.bind("}", "move-to-end-of-next-block", mode="caret")

## Bindings for command mode
# config.bind("<Alt-B>", "rl-backward-word", mode="command")
# config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="command")
# config.bind("<Alt-D>", "rl-kill-word", mode="command")
# config.bind("<Alt-F>", "rl-forward-word", mode="command")
# config.bind("<Ctrl-?>", "rl-delete-char", mode="command")
# config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="command")
# config.bind("<Ctrl-B>", "rl-backward-char", mode="command")
# config.bind("<Ctrl-C>", "completion-item-yank", mode="command")
# config.bind("<Ctrl-D>", "completion-item-del", mode="command")
# config.bind("<Ctrl-E>", "rl-end-of-line", mode="command")
# config.bind("<Ctrl-F>", "rl-forward-char", mode="command")
# config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="command")
# config.bind("<Ctrl-K>", "rl-kill-line", mode="command")
# config.bind("<Ctrl-N>", "command-history-next", mode="command")
# config.bind("<Ctrl-P>", "command-history-prev", mode="command")
# config.bind("<Ctrl-Return>", "command-accept --rapid", mode="command")
# config.bind("<Ctrl-Shift-C>", "completion-item-yank --sel", mode="command")
# config.bind("<Ctrl-Shift-Tab>", "completion-item-focus prev-category", mode="command")
# config.bind("<Ctrl-Tab>", "completion-item-focus next-category", mode="command")
# config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="command")
# config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="command")
# config.bind("<Ctrl-Y>", "rl-yank", mode="command")
# config.bind("<Down>", "completion-item-focus --history next", mode="command")
# config.bind("<Escape>", "leave-mode", mode="command")
# config.bind("<Return>", "command-accept", mode="command")
# config.bind("<Shift-Delete>", "completion-item-del", mode="command")
# config.bind("<Shift-Tab>", "completion-item-focus prev", mode="command")
# config.bind("<Tab>", "completion-item-focus next", mode="command")
# config.bind("<Up>", "completion-item-focus --history prev", mode="command")

## Bindings for hint mode
# config.bind("<Ctrl-B>", "hint all tab-bg", mode="hint")
# config.bind("<Ctrl-F>", "hint links", mode="hint")
# config.bind("<Ctrl-R>", "hint --rapid links tab-bg", mode="hint")
# config.bind("<Escape>", "leave-mode", mode="hint")
# config.bind("<Return>", "follow-hint", mode="hint")

## Bindings for insert mode
# config.bind("<Ctrl-E>", "open-editor", mode="insert")
# config.bind("<Escape>", "leave-mode", mode="insert")
# config.bind("<Shift-Ins>", "insert-text -- {primary}", mode="insert")

## Bindings for passthrough mode
# config.bind("<Shift-Escape>", "leave-mode", mode="passthrough")

## Bindings for prompt mode
# config.bind("<Alt-B>", "rl-backward-word", mode="prompt")
# config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="prompt")
# config.bind("<Alt-D>", "rl-kill-word", mode="prompt")
# config.bind("<Alt-F>", "rl-forward-word", mode="prompt")
# config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="prompt")
# config.bind("<Alt-Y>", "prompt-yank", mode="prompt")
# config.bind("<Ctrl-?>", "rl-delete-char", mode="prompt")
# config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="prompt")
# config.bind("<Ctrl-B>", "rl-backward-char", mode="prompt")
# config.bind("<Ctrl-E>", "rl-end-of-line", mode="prompt")
# config.bind("<Ctrl-F>", "rl-forward-char", mode="prompt")
# config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="prompt")
# config.bind("<Ctrl-K>", "rl-kill-line", mode="prompt")
# config.bind("<Ctrl-P>", "prompt-open-download --pdfjs", mode="prompt")
# config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="prompt")
# config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="prompt")
# config.bind("<Ctrl-X>", "prompt-open-download", mode="prompt")
# config.bind("<Ctrl-Y>", "rl-yank", mode="prompt")
# config.bind("<Down>", "prompt-item-focus next", mode="prompt")
# config.bind("<Escape>", "leave-mode", mode="prompt")
# config.bind("<Return>", "prompt-accept", mode="prompt")
# config.bind("<Shift-Tab>", "prompt-item-focus prev", mode="prompt")
# config.bind("<Tab>", "prompt-item-focus next", mode="prompt")
# config.bind("<Up>", "prompt-item-focus prev", mode="prompt")

## Bindings for register mode
# config.bind("<Escape>", "leave-mode", mode="register")

## Bindings for yesno mode
# config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="yesno")
# config.bind("<Alt-Y>", "prompt-yank", mode="yesno")
# config.bind("<Escape>", "leave-mode", mode="yesno")
# config.bind("<Return>", "prompt-accept", mode="yesno")
# config.bind("N", "prompt-accept --save no", mode="yesno")
# config.bind("Y", "prompt-accept --save yes", mode="yesno")
# config.bind("n", "prompt-accept no", mode="yesno")
# config.bind("y", "prompt-accept yes", mode="yesno")

# Layout
c.tabs.position = "top"

# Font
c.fonts.default_family = "Source Code Pro"
c.fonts.default_size = "14px"
c.fonts.web.family.standard = "Source Code Pro"
c.fonts.web.size.default = 16

# Colors
c.colors.contextmenu.menu.bg = c_bg
c.colors.contextmenu.menu.fg = c_fg
c.colors.contextmenu.selected.bg = c_bg_hl
c.colors.contextmenu.selected.fg = c_fg_hl

c.colors.downloads.bar.bg = c_bg
c.colors.downloads.error.bg = c_bg
c.colors.downloads.error.fg = c_fg_red
c.colors.downloads.start.bg = c_bg
c.colors.downloads.start.fg = c_fg_blue
c.colors.downloads.stop.bg = c_bg
c.colors.downloads.stop.fg = c_fg_yellow

c.colors.hints.bg = c_bg
c.colors.hints.fg = c_fg
c.colors.hints.match.fg = c_bg

c.colors.messages.error.bg = c_bg
c.colors.messages.error.fg = c_fg_red
c.colors.messages.error.border = c_fg_red
c.colors.messages.info.bg = c_bg
c.colors.messages.info.fg = c_fg_blue
c.colors.messages.info.border = c_fg_blue
c.colors.messages.warning.bg = c_bg
c.colors.messages.warning.fg = c_fg_yellow
c.colors.messages.warning.border = c_fg_yellow

c.colors.prompts.bg = c_bg
c.colors.prompts.border = c_bg_hl
c.colors.prompts.fg = c_fg
c.colors.prompts.selected.bg = c_bg_hl
c.colors.statusbar.caret.bg = c_bg_purple
c.colors.statusbar.caret.fg = c_fg
c.colors.statusbar.caret.selection.bg = c_fg_purple
c.colors.statusbar.caret.selection.fg = c_fg
c.colors.statusbar.command.bg = c_bg_blue
c.colors.statusbar.command.fg = c_fg
c.colors.statusbar.command.private.bg = c_fg_blue
c.colors.statusbar.command.private.fg = c_fg
c.colors.statusbar.insert.bg = c_bg_green
c.colors.statusbar.insert.fg = c_fg

# Appearance
c.statusbar.padding = { "top": 1, "bottom": 1, "left": 5, "right": 5}

c.tabs.max_width = -1
c.tabs.min_width = -1

# Behavior
c.auto_save.session = True
c.content.default_encoding = "utf-8"
c.content.geolocation = False
c.search.ignore_case = "smart"
c.tabs.position = "top"
c.downloads.location.directory = "~/dl"
