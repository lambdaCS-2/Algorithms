#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    min_num = 100000

    for key in recipe:
        if key in ingredients:
            num_batches = ingredients[key] // recipe[key]
        else:
            min_num = 0
        if num_batches < min_num:
            min_num = num_batches

    return min_num


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
