# pypipie
![](demo.gif)

## Inspiration
* A crypto trading engine I worked on for a year and some change. Relied heavily on websocket connections and asyncio. 
* [Classic Computer Science Problems in Python](https://www.manning.com/books/classic-computer-science-problems-in-python)
* A mix of boredom and curiosity on a Sunday afternoon

## Idea Overview:
* Python generator produces converging estimations of Pi from Leibniz's formula 
* Each update is sent (with an index corresponding to items in the series) via websocket
* Frontend produces a new row in the table for every new estimate it receives

### How to use
Uses pipenv https://github.com/pypa/pipenv

```
cd pypipie
pipenv install
pipenv shell 
python3 backend.py
```
then open frontend.html in web browser. Might have to refresh. 

Stop program via Ctrl-C on python script or exiting web page.
