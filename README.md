# progress bar across rounds


It embeds the progress bar to each page. Progress bar is located in `_templates\global\includes\progress.html`

The progress bar at a specific page can be switched off like that:

```python

class Demographics(Page):
    progress = False
```