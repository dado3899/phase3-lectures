# What is object oriented programming?
x = "Midna"
cat = "Midna"
davids_cat = "Midna"
# How do we expand it? What else does it contain? What else could it contain?
def zoomies(cat, time):
    print(f"{cat} is zooming at {time}")
zoomies(davids_cat,"2:00am")
davids_cats_hunger = 10
davids_cat = {
    "name": "Midna",
    "hunger": "Insatiable"
}
def feed_cat(cat):
    print(f"Feeding {cat['name']}")
    cat["hunger"] ="satiated"
feed_cat(davids_cat)
print(davids_cat)

# What else do we want to do with this? Thinking about oop what functions can we create
