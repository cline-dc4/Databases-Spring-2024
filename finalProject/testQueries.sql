-- getting ingredients from a coffee drink name
SELECT ci.ingredient_name 
FROM dcbcdb.CoffeeDrink AS cd JOIN dcbcdb.IngredientList AS il JOIN dcbcdb.CoffeeIngredient AS ci
WHERE cd.drink_name = 'Mocha' AND cd.drink_id = il.drink_id AND il.ingredient_id = ci.ingredient_id;

SELECT * FROM dcbcdb.coffeedrink;