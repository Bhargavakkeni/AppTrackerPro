<h1>NextLabProject - Problem Set Solutions</h1>

<h2>Problem Set I - Regex</h2>

<h3>Task</h3>

Write a regex to extract all the numbers with an orange color background from the provided JSON text.

<h3>Solution</h3>

The regex to extract numbers with an orange color background is:
```python
re.findall(r':(\d+)',string)
```
