tell application "System Preferences"
    activate
    reveal anchor "Hearing" of pane id "com.apple.preference.universalaccess"
end tell
delay 1
tell application "System Events" to tell process "System Preferences"
    click checkbox 2 of window 1
end tell
quit application "System Preferences"
display notification with title "Mono Mode has been toggled" subtitle "Carry on."
