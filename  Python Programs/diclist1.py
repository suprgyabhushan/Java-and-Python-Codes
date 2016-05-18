result = {}
for widget_type, app in widgets:
    result[widget_type] = result.get(widget_type, []) + [app]
