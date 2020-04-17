# What is getgdelt&usegdelt？

GDELT(**Global Database of Events, Language, and Tone**), monitors the world's news media from nearly every corner of every country in print, broadcast, and web formats, in over 100 languages, every moment of every day.

``getgdelt``is a Python based framework that calls the browser to download and format GDELT data.

# Why do we use getgdelt&usegdelt？

Existing frameworks, such as [gdeltPyR](https://github.com/linwoodc3/gdeltPyR), provide us with many conveniences for calling GDELT data using python, but as mentioned by [linwoodc3](https://github.com/linwoodc3): ['The only limitation with data pulls``gdeltPyR`` is you hardware. '](https://pypi.org/project/gdelt/) 

Using non-professional hardware or using existing python packages to call GDELT data in regions and countries where the network is restricted will encounter many errors. ``getgdelt``  downloads GDELT data by calling the browser. It makes the data calling process simpler and more visual. 

For users who use non-professional hardware or in countries and regions with limited networks, it will be very convenient to use ``getgdelt`` to obtain GDELT data.

# How do we use getgdelt&usegdelt?

## Installation

`getgdelt` can be installed via pip

```
pip install getgdelt
```

## Basic Examples

### Get GDELT

```python
import getgdelt
getgdelt(year_start,month_start,day_start,year_end,month_end,day_end)
```

### Use GDELT

```python
import getgdelt
gdelt = usegdelt(download_file_directory,output_file_directory)
```

