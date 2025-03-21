class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        recipe_idx = {recipe: i for i, recipe in enumerate(recipes)}
        graph = defaultdict(list)
        in_degree = [0] * len(recipes)
        
        for i, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient in recipe_idx:
                    graph[ingredient].append(recipes[i])
                    in_degree[i] += 1

                elif ingredient not in available:
                    in_degree[i] += 1
        
        queue = deque([recipes[i] for i in range(len(recipes)) if in_degree[i] == 0])

        result = []
        while queue:
            recipe = queue.popleft()
            result.append(recipe)
            
            available.add(recipe)
            
            for dependent in graph[recipe]:
                dependent_idx = recipe_idx[dependent]
                in_degree[dependent_idx] -= 1
                
                if in_degree[dependent_idx] == 0:
                    queue.append(dependent)
        
        return result