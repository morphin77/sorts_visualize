# How to contribute?
1. Make fork of this project
2. Create changes in some Your branch
3. Create Pull Request

## For adding new algorithm
1. Create new file in sort_visualize/sort/algorithms/
2. Inherit your class from Base (sort_visualize/sort/algorithms/base.py)
3. Implement logic for one iteration in method, named ``sort()``. For correct visualize it must return an array positions of elements which was touched on this iteration. You can store states in object`s properties
4. Import Your class in Global state (sort_visualize/application/state.py)


## Testing
Comming soon... may be... sometimes...
