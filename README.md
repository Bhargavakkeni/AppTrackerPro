#NextLabProject - Problem Set Solutions

##Problem Set I - Regex

###Task

Write a regex to extract all the numbers with an orange color background from the provided JSON text.

###Solution

The regex to extract numbers with an orange color background is:
```python
re.findall(r':(\d+)',string)
```